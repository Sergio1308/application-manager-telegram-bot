from aiogram.utils import executor
from config import dp
from bot.modules.handlers import message_handler, callback_handler, application_creation, application_deletion
from bot.db.database import create_table


async def on_startup(_):
    # connection to db, create tables, etc
    create_table()
    print('Bot is now available')


if __name__ == '__main__':
    # todo
    message_handler.init_message_handler(dp)
    callback_handler.init_callback_handlers(dp)
    application_creation.init_app_creation_handlers(dp)
    application_deletion.init_app_deletion_handlers(dp)
    #
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
