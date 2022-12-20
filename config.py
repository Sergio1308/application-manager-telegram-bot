from env_loading import load_env_variable
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

m_storage = MemoryStorage()

BOT_TOKEN = load_env_variable("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=m_storage)
