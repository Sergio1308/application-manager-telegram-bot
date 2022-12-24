from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_reply_keyboard(texts: list, request_contact=False, request_location=False) -> ReplyKeyboardMarkup:
    """
    A method that creates reply keyboard markup with specified text as a list, so we can use this method
    to create 1 or more buttons in a markup.

    :param texts: button text list
    :param request_contact: request contact after pressing on the button, by default is False
    :param request_location: request location after pressing on the button, by default is False
    :return: ReplyKeyboardMarkup
    """
    row = [
        KeyboardButton(text=text, request_contact=request_contact, request_location=request_location) for text in texts
    ]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True, one_time_keyboard=True)
