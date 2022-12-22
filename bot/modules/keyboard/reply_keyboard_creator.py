from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_reply_keyboard(texts: list) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=text) for text in texts]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
