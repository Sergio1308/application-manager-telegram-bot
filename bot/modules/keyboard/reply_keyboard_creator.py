from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_reply_keyboard(texts: list, request_contact=False, request_location=False) -> ReplyKeyboardMarkup:
    row = [
        KeyboardButton(text=text, request_contact=request_contact, request_location=request_location) for text in texts
    ]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
