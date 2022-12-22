from aiogram import types, Dispatcher
from bot.modules.keyboard import inline_start_keyboard, inline_keyboard_creator
from aiogram.dispatcher import FSMContext
from bot.modules.states import Forms
from bot.db.database import add_new_column

sections = ['Склад', 'Магазин', 'Офис']


async def main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Вы вернулись в главное меню\nВыберите пункт 👇', reply_markup=inline_start_keyboard())
    await state.finish()


async def specify_section(call: types.CallbackQuery):
    await call.message.answer('Укажите раздел:', reply_markup=inline_keyboard_creator.
                              create_inline_keyboard(sections, sections, row_width=3))
    await Forms.section.set()


async def enter_section_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['section'] = call.data
    await call.message.answer('Введите название точки:')
    await Forms.next()


async def insert_data(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        add_new_column(data['application_model'])
    await main_menu(call, state)


def init_callback_handlers(disp: Dispatcher):
    disp.register_callback_query_handler(main_menu, text='main_menu', state='*')
    disp.register_callback_query_handler(specify_section, text='create_application', state=None)
    disp.register_callback_query_handler(enter_section_name, text=sections, state=Forms.section)
    disp.register_callback_query_handler(insert_data, text='insert_query', state=Forms.application_model)
