from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from bot.db.database import get_all_columns, delete_column

application_models_messages = {}


class FSMDeletion(StatesGroup):
    deletion_msg = State()


async def show_data(call: types.CallbackQuery):
    data = get_all_columns()
    for c in data:
        msg = f'{c[1]}: {c[2]}\nКонтактный номер: {c[3]}'
        m = await call.message.answer(msg, reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(text='Удалить запись', callback_data='deletion_confirmation')
        ))
        print(m.message_id)
        application_models_messages.update({m.message_id: c[0]})


async def delete_selected_column(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['deletion_msg'] = call.message
        print(data['deletion_msg'])
    await call.message.edit_text(
        'Вы уверены, что хотите удалить данную запись?', reply_markup=InlineKeyboardMarkup(row_width=2).add(
            InlineKeyboardButton(text='Да', callback_data='delete_column'),
            InlineKeyboardButton(text='Нет', callback_data='cancel_deletion')
        )
    )


async def cancel_deletion(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        prev_msg = data['deletion_msg']
        await call.message.edit_text(prev_msg.text, reply_markup=prev_msg.reply_markup)


async def execute_deletion(call: types.CallbackQuery):
    delete_column(application_models_messages.get(call.message.message_id))
    await call.message.edit_text('Удалено !')


def init_app_deletion_handlers(disp: Dispatcher):
    disp.register_callback_query_handler(show_data, text='delete_application')
    disp.register_callback_query_handler(delete_selected_column, text='deletion_confirmation')
    disp.register_callback_query_handler(cancel_deletion, text='cancel_deletion')
    disp.register_callback_query_handler(execute_deletion, text='delete_column')
