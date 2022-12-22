from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_inline_keyboard(texts: list, callbacks: list, row_width=1) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=row_width).add(
        *[InlineKeyboardButton(text=text, callback_data=callback) for text, callback in zip(texts, callbacks)]
    )
