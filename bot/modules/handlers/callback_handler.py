from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_app_callback(callback: types.CallbackQuery):
    await callback.message.edit_text('Укажите раздел:')
    await callback.message.edit_reply_markup(InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text='Склад', callback_data='specified_section'),
        InlineKeyboardButton(text='Магазин', callback_data='specified_section'),
        InlineKeyboardButton(text='Офис', callback_data='specified_section')
    ))


async def specified_section(callback: types.CallbackQuery):
    await callback.message.edit_text('Введите название точки:')


def init_callback_handler(disp: Dispatcher):
    disp.register_callback_query_handler(create_app_callback, text='create_app_btn')
    disp.register_callback_query_handler(specified_section, text='specified_section')
