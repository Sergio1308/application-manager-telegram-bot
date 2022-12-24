from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_inline_keyboard(texts: list, callbacks: list, row_width=1) -> InlineKeyboardMarkup:
    """
    A method that creates inline keyboard markup with specified text and callbacks data as a list, so we can
    use this method to create 1 or more buttons in a markup.

    :param texts: button text list
    :param callbacks: callback_data text
    :param row_width: markup row width, by default = 1
    :return: InlineKeyboardMarkup
    """
    return InlineKeyboardMarkup(row_width=row_width).add(
        *[InlineKeyboardButton(text=text, callback_data=callback) for text, callback in zip(texts, callbacks)]
    )
