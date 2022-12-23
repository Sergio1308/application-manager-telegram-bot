from .inline_keyboard_creator import create_inline_keyboard
from bot.modules.handlers.callback_data_vars import *


def inline_start_keyboard():
    return create_inline_keyboard(['Создать заявку', 'Удалить заявку'],
                                  [CREATE_APPLICATION, DELETE_APPLICATION])
