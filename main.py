import logging

from bot.modules.handlers import message_handler, callback_handler
from bot.db.database import create_table
from aiogram.utils import executor
from bot.config import dp

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    create_table()
    logging.info('Bot in now available.')


if __name__ == '__main__':
    message_handler.init_message_handler(dp)
    callback_handler.init_callback_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
