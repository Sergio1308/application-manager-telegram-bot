import aiogram.utils.markdown as md

from aiogram import types, Dispatcher
from bot.modules.keyboard import create_inline_keyboard, create_reply_keyboard
from aiogram.dispatcher import FSMContext
from bot.modules.states import Forms
from bot.db.models.application import Application
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from .callback_data_vars import *


def inline_start_keyboard():
    return create_inline_keyboard(['Создать заявку', 'Удалить заявку'],
                                  [CREATE_APPLICATION, DELETE_APPLICATION])


async def start_command(message: types.Message):
    await message.reply('Выберите пункт 👇', reply_markup=inline_start_keyboard())


# region CREATE_APPLICATION
async def share_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['section_name'] = message.text
    await message.reply('Отправь мне свой номер телефона, используя кнопку ниже:',
                        reply_markup=create_reply_keyboard(
                            ['Отправить свой номер'], request_contact=True
                        ))
    await Forms.next()


async def share_location(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number.replace('+', '')
    await message.reply('Отправь мне свое местоположение, используя кнопку ниже:',
                        reply_markup=create_reply_keyboard(
                            ['Отправить свое местоположение'], request_location=True
                        ))
    await Forms.next()


async def confirm_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['location'] = message.location
        data['application_model'] = Application(
            data['section'], data['section_name'], data['phone_number'], data['location']
        )
        app_model = data['application_model']
        print(app_model)
        await message.answer(
            md.text(
                md.text(md.bold('Раздел:'), app_model.getSection()),
                md.text(md.bold('Название:'), app_model.getSectionName()),
                md.text(md.bold('Номер:'), app_model.getPhoneNumber()),
                md.text(md.bold('Местоположение:'), f'Широта: {message.location.latitude} '
                                                    f'Долгота: {message.location.longitude}'),
                sep='\n'
            ),
            reply_markup=create_inline_keyboard(
                ['Подтвердить', 'Отклонить'], [INSERT_DATA, MAIN_MENU]
            ),
            parse_mode=ParseMode.MARKDOWN)
    await Forms.next()


async def check_contact(message: types.Message):
    await message.reply('Отправьте свой контактный номер, воспользуйтесь кнопкой ниже под полем ввода.')


async def check_location(message: types.Message):
    await message.reply('Отправьте свое местоположение, воспользуйтесь кнопкой ниже под полем ввода.')
# endregion


async def cancel_handler(message: types.Message, state: FSMContext):
    """Exit from finite-state machine"""
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply('Отменено.')
    await state.finish()


async def send_other_text(message: types.Message):
    await message.reply('Неизвестная команда. Пользуйтесь кнопками под сообщением или введите /start.')


def init_message_handler(disp: Dispatcher):
    disp.register_message_handler(start_command, commands=['start', 'help'])
    disp.register_message_handler(cancel_handler, state='*', commands=['cancel', 'отмена'])
    disp.register_message_handler(cancel_handler, Text(equals=['cancel', 'отмена'], ignore_case=True), state='*')
    disp.register_message_handler(check_contact, lambda message: not message.contact, state=Forms.phone_number)
    disp.register_message_handler(check_location, lambda message: not message.location, state=Forms.location)
    disp.register_message_handler(share_phone_number, state=Forms.section_name)
    disp.register_message_handler(share_location, content_types=['contact'], state=Forms.phone_number)
    disp.register_message_handler(confirm_data, content_types=['location'], state=Forms.location)
    disp.register_message_handler(send_other_text)
