from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inlineKeyboard_markup = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Создать заявку', callback_data='create_application'),
    InlineKeyboardButton(text='Удалить заявку', callback_data='delete_application')
)
