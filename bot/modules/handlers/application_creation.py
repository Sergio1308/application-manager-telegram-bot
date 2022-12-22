from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from bot.db.models.application import Application
from bot.db.database import add_new_column
from bot.modules.handlers.callback_handler import main_menu
# TODO: move funcs to message/callback handlers/other classes, rewrite


class FSMCreation(StatesGroup):
    # todo: states class
    selected_section = State()
    section_name = State()
    phone_number = State()
    location = State()
    data_filling = State()


async def sm_start(call: types.CallbackQuery):
    await FSMCreation.selected_section.set()
    await call.message.reply('Укажите раздел:', reply_markup=InlineKeyboardMarkup(row_width=3).add(
        InlineKeyboardButton(text='Склад', callback_data='Склад'),
        InlineKeyboardButton(text='Магазин', callback_data='Магазин'),
        InlineKeyboardButton(text='Офис', callback_data='Офис')
    ))


async def enter_section_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['selected_section'] = call.data
    await FSMCreation.next()
    await call.message.reply('Введите название точки:')


async def share_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['section_name'] = message.text
    await FSMCreation.next()
    await message.reply('Отправь мне свой номер телефона, используя кнопку ниже:',
                        reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
                            KeyboardButton(text='Отправить свой номер', request_contact=True)
                        ))


async def share_location(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await FSMCreation.next()
    await message.reply('Отправь мне свое местоположение, используя кнопку ниже:',
                        reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
                            KeyboardButton(text='Отправить свое местоположение', request_location=True)
                        ))


async def confirm_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # todo
        data['location'] = message.location
        current_section = data['selected_section']
        current_section_name = data['section_name']
        current_phone_number = data['phone_number']
        current_location = data['location']
        current_application = Application(
            str(current_section), str(current_section_name), str(current_phone_number), str(current_location)
        )
        print(current_application)
        #
        await FSMCreation.next()
        await message.reply(
            md.text(
                md.text('Раздел:', md.bold(current_section)),
                md.text('Название:', md.bold(current_section_name)),
                md.text('Номер:', md.bold(current_phone_number)),
                md.text('Местоположение:', md.bold(f'Широта: {current_location.latitude} '
                                                   f'Долгота: {current_location.longitude}')),
                sep='\n'
            ),
            # reply_markup=types.ReplyKeyboardRemove(), todo
            reply_markup=InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text='Подтвердить', callback_data='insert_query'),
                InlineKeyboardButton(text='Отклонить', callback_data='main_menu')
            ),
            parse_mode=ParseMode.MARKDOWN)
    # await state.finish()


async def insert_data(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'main_menu':
        await state.finish()
        await main_menu(call)
    else:
        async with state.proxy() as data:
            print('inserting data...')
            current_section = data['selected_section']
            current_section_name = data['section_name']
            current_phone_number = data['phone_number']
            current_location = data['location']
            current_application = Application(
                str(current_section), str(current_section_name), str(current_phone_number), current_location
            )
            add_new_column(current_application)
        await state.finish()
        await main_menu(call)


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отменено.')


def init_app_creation_handlers(disp: Dispatcher):
    disp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    disp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    disp.register_callback_query_handler(sm_start, text='create_application', state=None)
    disp.register_callback_query_handler(enter_section_name, state=FSMCreation.selected_section)
    disp.register_message_handler(share_phone_number, state=FSMCreation.section_name)
    disp.register_message_handler(share_location, content_types=['contact'], state=FSMCreation.phone_number)
    disp.register_message_handler(confirm_data, content_types=['location'], state=FSMCreation.location)
    disp.register_callback_query_handler(insert_data, text='insert_query', state=FSMCreation.data_filling)
