from aiogram.dispatcher.filters.state import State, StatesGroup
from bot.db.models.application import Application


class Forms(StatesGroup):
    """
    A class that represents states of finite state machine
    """
    section = State()
    section_name = State()
    phone_number = State()
    location = State()
    application_model: Application = State()  # POPO object (db model)

    application_models_messages: dict = State()
    selected_message = State()
