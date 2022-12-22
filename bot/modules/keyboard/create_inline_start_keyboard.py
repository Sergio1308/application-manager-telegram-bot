from bot.modules.keyboard.inline_keyboard_creator import create_inline_keyboard


def inline_start_keyboard():
    return create_inline_keyboard(['Создать заявку', 'Удалить заявку'],
                                  ['create_application', 'delete_application'])
