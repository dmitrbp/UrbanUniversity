from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api='7444786549:AAGQqDYFQpApu_qBoqhp7u_481xv3Ca7iF4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text = ['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')

@dp.message_handler(commands = ['start'])
async def start_message(message):
    print('Start message')

@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)