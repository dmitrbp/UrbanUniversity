from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Token import key

api = key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

api = key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(State):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.address)
async def send_colories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = data['weight'] * 10 +  data['growth'] * 6,25 + data['age'] * 5 + 5
    await message.answer(f"Калорий: {calories}")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

