from aiogram import types, Dispatcher
from bot.modules.keyboard import inline_start_keyboard


async def main_menu(call: types.CallbackQuery):
    await call.message.edit_text('Вы вернулись в главное меню\nВыберите пункт 👇', reply_markup=inline_start_keyboard())


def init_callback_handlers(disp: Dispatcher):
    disp.register_callback_query_handler(main_menu, text='main_menu')
