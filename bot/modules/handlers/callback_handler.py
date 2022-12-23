from aiogram import types, Dispatcher
from bot.modules.keyboard import inline_keyboard_creator
from aiogram.dispatcher import FSMContext
from bot.modules.states import Forms
from bot.db.database import add_new_column, get_all_columns, delete_column
from .callback_data_vars import *

sections = ['Склад', 'Магазин', 'Офис']
application_models_messages = {}


# region CREATE_APPLICATION
async def main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Вы вернулись в главное меню.', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await call.answer()


async def specify_section(call: types.CallbackQuery):
    await call.message.answer('Укажите раздел:', reply_markup=inline_keyboard_creator.
                              create_inline_keyboard(sections, sections, row_width=3))
    await Forms.section.set()
    await call.answer()


async def enter_section_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['section'] = call.data
    await call.message.answer('Введите название точки:')
    await Forms.next()
    await call.answer()


async def insert_data(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        add_new_column(data['application_model'])
    await main_menu(call, state)
    await call.answer()
# endregion


# region DELETE_APPLICATION
async def show_data(call: types.CallbackQuery, state: FSMContext):
    data = get_all_columns()
    for entry in data:
        msg = f'{entry[1]}: {entry[2]}\nКонтактный номер: {entry[3]}'
        m = await call.message.answer(msg, reply_markup=inline_keyboard_creator.create_inline_keyboard(
            ['Удалить запись'], [DELETE_ENTRY]
        ))
        application_models_messages.update({m.message_id: entry[0]})
    async with state.proxy() as data:
        data['application_models_messages'] = application_models_messages
    await call.answer()


async def delete_selected_column(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['selected_message'] = call.message
    await call.message.edit_text(
        'Вы уверены, что хотите удалить данную запись?', reply_markup=inline_keyboard_creator.create_inline_keyboard(
            ['Да', 'Нет'], [DELETE_COLUMN, CANCEL_COLUMN_DELETION]
        ))
    await call.answer()


async def cancel_deletion(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        prev_msg = data['selected_message']
        await call.message.edit_text(prev_msg.text, reply_markup=prev_msg.reply_markup)
    await call.answer()


async def execute_deletion(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['application_models_messages'] = application_models_messages
    delete_column(application_models_messages.get(call.message.message_id))
    await call.message.edit_text('Удалено !')
    await call.answer()
# endregion


def init_callback_handlers(disp: Dispatcher):
    disp.register_callback_query_handler(main_menu, text=MAIN_MENU, state=Forms.application_model)
    disp.register_callback_query_handler(specify_section, text=CREATE_APPLICATION, state=None)
    disp.register_callback_query_handler(enter_section_name, text=sections, state=Forms.section)
    disp.register_callback_query_handler(insert_data, text=INSERT_DATA, state=Forms.application_model)

    disp.register_callback_query_handler(show_data, text=DELETE_APPLICATION)
    disp.register_callback_query_handler(delete_selected_column, text=DELETE_ENTRY)
    disp.register_callback_query_handler(cancel_deletion, text=CANCEL_COLUMN_DELETION)
    disp.register_callback_query_handler(execute_deletion, text=DELETE_COLUMN)
