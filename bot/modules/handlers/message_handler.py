from aiogram import types, Dispatcher
from bot.modules.inlinekeyboard import inlineKeyboard_markup


async def start_command(message: types.Message):
    await message.reply('Выберите пункт 👇', reply_markup=inlineKeyboard_markup)


async def main_menu(call: types.CallbackQuery):
    await call.message.edit_text('Вы вернулись в главное меню\nВыберите пункт 👇', reply_markup=inlineKeyboard_markup)


async def send_other_text(message: types.Message):
    await message.reply('Неизвестная команда. Пользуйтесь кнопками под сообщением или введите /start.')


def init_message_handler(disp: Dispatcher):
    disp.register_message_handler(start_command, commands=['start', 'help'])
    disp.register_message_handler(send_other_text)

    disp.register_callback_query_handler(main_menu, text='main_menu')
