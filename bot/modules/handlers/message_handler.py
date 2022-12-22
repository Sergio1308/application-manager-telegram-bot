from aiogram import types, Dispatcher
from bot.modules.keyboard import inline_start_keyboard


async def start_command(message: types.Message):
    await message.reply('Выберите пункт 👇', reply_markup=inline_start_keyboard())


async def send_other_text(message: types.Message):
    await message.reply('Неизвестная команда. Пользуйтесь кнопками под сообщением или введите /start.')


def init_message_handler(disp: Dispatcher):
    disp.register_message_handler(start_command, commands=['start', 'help'])
    disp.register_message_handler(send_other_text)
