from aiogram.utils import executor
from config import dp
from bot.modules.handlers import message_handler as msg, callback_handler as c, application_creation as ac, \
                                    application_deletion as ad  # todo
from bot.db.database import create_table


async def on_startup(_):
    # connection to db, create tables, etc
    create_table()
    print('Bot is now available')


if __name__ == '__main__':
    # todo
    msg.init_message_handler(dp)
    ac.init_app_creation_handlers(dp)
    ad.init_app_deletion_handlers(dp)
    c.init_callback_handler(dp)
    #
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
