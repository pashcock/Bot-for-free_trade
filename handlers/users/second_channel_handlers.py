
from aiogram import types
from aiogram.dispatcher import FSMContext


from data import config
from keyboards.Inline.admin_key import key_sec_chn, key_add_second_channel_back
from loader import bot, dp, db
from state import SecChn


@dp.message_handler(state=SecChn.Cr)
async def get_chat(message: types.Message):
    try:
        k = await bot.get_chat(message.forward_from_chat.id)
        config.additional_channel = message.forward_from_chat.id
        await message.answer(text='Успешно: бот является админом канала'
                                  '\n\nНазвание: {}\nТип чата: {}'
                                  '\n\n\nПришлите ссылку приглашения на канал:\n'
                                  '<code>https://t.me/joinchat/.......</code>'.format(k.title, k.type),
                             reply_markup=key_add_second_channel_back)
        await SecChn.Wr.set()
    except Exception as e:
        await message.answer(f'Повторите попытку, бот не является админом канала\n\n{e}',
                             reply_markup=key_add_second_channel_back)


@dp.message_handler(state=SecChn.Wr)
async def get_link_chat(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.__contains__('https://t.me/joinchat/'):
        config.channel_link = answer
        await message.answer('Канал успешно добавлен', reply_markup=key_add_second_channel_back)
        await state.finish()
        await db.update_add_channel()
    else:
        await message.answer('Ошибка - ссылка на канал должна быть формата приватной ссылки(канал '
                             'при этом не обязан быть приватным\n\n'
                             'Повторите попытку',
                             reply_markup=key_add_second_channel_back)


@dp.callback_query_handler(text='second_channel', user_id=config.admins)
async def second_channel_edit(call: types.CallbackQuery):
    await call.answer()
    text = '''🕸<b>Второй канал</b>
    
<b>Добавить канал</b> - добавьте бот в администраторы канала и пришлите ссылку для приглашения на канал
<b>Удалить канал</b> - канал удалиться даже если его там не было(просто чтобы не писать лишний код)
            '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_sec_chn)


@dp.callback_query_handler(text='second_channel', user_id=config.admins, state=SecChn.Cr)
async def second_channel_edit(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    text = '''🕸<b>Второй канал</b>
    
<b>Добавить канал</b> - добавьте бот в администраторы канала и пришлите ссылку для приглашения на канал
<b>Удалить канал</b> - канал удалиться даже если его там не было(просто чтобы не писать лишний код)
                '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_sec_chn)


@dp.callback_query_handler(text='second_channel', user_id=config.admins, state=SecChn.Wr)
async def second_channel_edit(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    text = '''🕸<b>Второй канал</b>
    
<b>Добавить канал</b> - добавьте бот в администраторы канала и пришлите ссылку для приглашения на канал
<b>Удалить канал</b> - канал удалиться даже если его там не было(просто чтобы не писать лишний код)
                '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_sec_chn)


@dp.callback_query_handler(text='add_second_channel', user_id=config.admins)
async def add_second_channel(call: types.CallbackQuery):
    await call.answer()
    await SecChn.Cr.set()
    text = 'Перешлите сообщение из канала, которы хотите добавить\n\nБот должен быть там админом\n\n' \
           'В случае ошибки бот сообщит об этом'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_add_second_channel_back)


@dp.callback_query_handler(text='del_second_channel', user_id=config.admins)
async def second_channel_del(call: types.CallbackQuery):
    config.additional_channel = ''
    await db.del_add_channel()
    await call.answer('Второй канал удален', show_alert=True)
