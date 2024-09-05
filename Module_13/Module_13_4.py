from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Token import key

api = key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

api = '7444786549:AAGQqDYFQpApu_qBoqhp7u_481xv3Ca7iF4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(State):
    age = State()
    growth = State()
    weight = State()

