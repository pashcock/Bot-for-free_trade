from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data import config
from keyboards.Inline.admin_caption import key_caption, key_caption_back
from loader import dp, bot, db
from state import CreateCaption


@dp.message_handler(state=CreateCaption.C1)
async def get_key_del(message: types.Message, state: FSMContext):
    config.caption = message.text
    if config.caption.__contains__('_'):
        tex = config.caption
        config.caption = tex.replace('_', '\\_')
    text = 'Подпись изменена на:\n\n'+str(config.caption)
    await db.update_caption()
    await message.answer(text=text, reply_markup=key_caption)
    await state.finish()


@dp.callback_query_handler(text='word_caption', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    text = '📝<b>Подпись</b>\n\nРедактирование подписи к сообщению, которое получает пользователь'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_caption)


@dp.callback_query_handler(text='word_caption', user_id=config.admins, state=CreateCaption.C1)
async def call_add_link(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer()
    text = '📝<b>Подпись</b>\n\nРедактирование подписи к сообщению, которое получает пользователь'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_caption)


@dp.callback_query_handler(text='change_caption', user_id=config.admins)
async def change_captions(call: CallbackQuery):
    await call.answer()
    await CreateCaption.C1.set()
    text = 'Введите подпись\nРазметка: Markdown\nНе рекомендуется делать подпись больше 255 символов.'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_caption_back)


@dp.callback_query_handler(text='del_caption', user_id=config.admins)
async def del_captions(call: CallbackQuery):
    config.caption = ''
    await call.answer(text='Подпись удалена', show_alert=True)
    await db.caption_del()
