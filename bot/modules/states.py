from aiogram.dispatcher.filters.state import State, StatesGroup


class Forms(StatesGroup):
    section = State()
    section_name = State()
    phone_number = State()
    location = State()

    application_model = State()  # POPO object (db model)
    application_models_messages = State()  # dict
