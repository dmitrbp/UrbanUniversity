from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Token import key

api = key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_reply = ReplyKeyboardMarkup(resize_keyboard=True)
reply_button_calc = KeyboardButton(text='Рассчитать')
reply_button_info = KeyboardButton(text='Информация')
reply_button_buy = KeyboardButton(text='Купить')
kb_reply.add(reply_button_calc, reply_button_info, reply_button_buy)

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
inline_button_calc = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(inline_button_calc, inline_button_formulas)

kb_inline_buy = InlineKeyboardMarkup(resize_keyboard=True)
inline_buttons_buy = [
    InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
    InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
    InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
    InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
]
kb_inline_buy.add(*inline_buttons_buy)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_reply)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберете опцию', reply_markup=kb_inline)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f'Название: Product {i} | Описание: описание {i} | Цена: {i * 100}' )
        with open(f'pics/pic{i}.jpg', 'rb') as pic:
            await message.answer_photo(pic)
    await message.answer('Выберите продукт для покупки', reply_markup=kb_inline_buy)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(text='10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(f'Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        calories = float(data['weight']) * 10 + float(data['growth']) * 6.25 + float(data['age']) * 5 + 5
        await message.answer(f'Ваша норма калорий: {calories}')
    except ValueError:
        await message.answer(f'Неверные исходные данные')
    finally:
        await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
