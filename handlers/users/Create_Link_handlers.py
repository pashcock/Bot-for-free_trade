from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data import config
from keyboards.Inline.admin_create_post import key_return_link, key_link, key_after_create_post, key_after_start
from loader import dp, db, bot
from state import CreatePost, EditPost, BanPost
from utils.argument_generation import generation


@dp.message_handler(state=CreatePost.Q1)
async def get_post(message: types.Message, state: FSMContext):
    try:
        text = message.text
        arg = '11111111'
        while await db.check_link(arg=arg):
            arg = await generation()
        try:
            await message.answer(text, parse_mode='Markdown', disable_web_page_preview=True, disable_notification=True)
            await message.answer('Вот ссылка для получения поста:'
                                 '\nhttps://t.me/f_trade_bot?start={}\n\nАктивируйте, '
                                 'чтобы проверить'.format(arg), disable_web_page_preview=True,
                                 disable_notification=True)
            await db.write_post(text=str(text), random_text='{}'.format(arg))
            await state.finish()
            await message.answer('Сообщение подготовлено',
                                 reply_markup=key_after_create_post)
        except Exception as e:
            await message.answer(f'Ошибка в понимании разметки\n\n{e}', reply_markup=key_return_link)
    except Exception as e:
        await message.answer(f'Перехвачена ошибка:\n\n{e}', reply_markup=key_return_link)


@dp.message_handler(state=EditPost.E1)
async def get_key(message: types.Message, state: FSMContext):
    argument = message.text
    arg = ''
    if len(argument) <= 8:
        arg = argument
    else:
        try:
            arg = (argument.split('='))[1]
        except:
            pass
    if await db.check_link(arg):
        await state.update_data(arg=arg)
        text = '''<b>Пришлите текст поста</b>

Рекомендуется присылать не готовый пост с канала с его форматированием, а сокращенный.

Единственная ошибка которая может возникнуть это ошибка с разметкой курсивом.
Когда в ссылке есть нижнее подчеркивание, оно воспринимается как часть незавершенной разметки.

<b>Все ссылки рекомендуется прятать в текст:</b>
<code>[текст](ссылка)</code>
В таком случае ошибок точно не будет

<b>Бот в любом случае сообщит об ошибке</b>

Разметка: Markdown
Аргумент: {}
            '''.format(arg)
        await message.answer(text, reply_markup=key_return_link)
        await EditPost.next()
    else:
        text = 'Ошибка\n\nПришлите действительный аргумент(start=аргумент)'
        await message.answer(text=text, reply_markup=key_return_link)


@dp.message_handler(state=EditPost.E2)
async def get_key_post(message: types.Message, state: FSMContext):
    data = await state.get_data()
    arg = data.get("arg")
    edit_text = message.text
    try:
        await message.answer(edit_text, parse_mode='Markdown', disable_web_page_preview=True, disable_notification=True)
        await message.answer('Пост изменен\n\nАктивируйте бота по ссылке для проверки:'
                             '\nhttps://t.me/f_trade_bot?start={}'.format(arg), disable_web_page_preview=True,
                             disable_notification=True)
        await db.update_post(edit_text, arg)
        await message.answer('Сообщение подготовлено', reply_markup=key_after_create_post)
        await state.finish()
    except Exception as e:
        await message.answer(f'Ошибка в понимании разметки\n\n{e}', reply_markup=key_return_link)


@dp.message_handler(state=BanPost.B1)
async def get_key_del(message: types.Message, state: FSMContext):
    argument = message.text
    arg = ''
    if len(argument) <= 8:
        arg = argument
    else:
        try:
            arg = (argument.split('='))[1]
        except:
            pass
    if await db.check_link(arg):
        await db.ban_post(arg)
        await message.answer('Пост заблокирован\n\nАктивируйте бота по ссылке для проверки:'
                             '\nhttps://t.me/f_trade_bot?start={}'.format(arg))
        await message.answer('Сообщение подготовлено', reply_markup=key_after_create_post)
        await state.finish()
    else:
        text = 'Ошибка\n\nПришлите действительный аргумент(start=аргумент)'
        await message.answer(text=text, reply_markup=key_return_link)


@dp.callback_query_handler(text='create_link', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    text = '''<b>Работа со ссылками</b>

<b>Добавить ссылку</b> - сделать ссылку для нового поста
<b>Изменить ссылку</b> - исправить пост
<b>Заблокировать ссылку</b> - заброкировать в случае ебки мозга правообладателем

Заблокированную ссылку можно изменить через изменение ссылки

<b>Максимальная длина поста 1000 символов</b>
    '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_link)


@dp.callback_query_handler(text='create_link', user_id=config.admins, state=CreatePost.Q1)
async def call_add_link(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer()
    text = '''<b>Работа со ссылками</b>

<b>Добавить ссылку</b> - сделать ссылку для нового поста
<b>Изменить ссылку</b> - исправить пост
<b>Заблокировать ссылку</b> - заброкировать в случае ебки мозга правообладателем

Заблокированную ссылку можно изменить через изменение ссылки

<b>Максимальная длина поста 1000 символов</b>
        '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_link)


@dp.callback_query_handler(text='create_link', user_id=config.admins, state=EditPost.E1)
async def call_add_link(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer()
    text = '''<b>Работа со ссылками</b>

<b>Добавить ссылку</b> - сделать ссылку для нового поста
<b>Изменить ссылку</b> - исправить пост
<b>Заблокировать ссылку</b> - заброкировать в случае ебки мозга правообладателем

Заблокированную ссылку можно изменить через изменение ссылки

<b>Максимальная длина поста 1000 символов</b>
        '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_link)


@dp.callback_query_handler(text='create_link', user_id=config.admins, state=EditPost.E2)
async def call_add_link(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer()
    text = '''<b>Работа со ссылками</b>
    
<b>Добавить ссылку</b> - сделать ссылку для нового поста
<b>Изменить ссылку</b> - исправить пост
<b>Заблокировать ссылку</b> - заброкировать в случае ебки мозга правообладателем

Заблокированную ссылку можно изменить через изменение ссылки

<b>Максимальная длина поста 1000 символов</b>
        '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_link)


@dp.callback_query_handler(text='create_link', user_id=config.admins, state=BanPost.B1)
async def call_add_link(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer()
    text = '''<b>Работа со ссылками</b>

<b>Добавить ссылку</b> - сделать ссылку для нового поста
<b>Изменить ссылку</b> - исправить пост
<b>Заблокировать ссылку</b> - заброкировать в случае ебки мозга правообладателем

Заблокированную ссылку можно изменить через изменение ссылки

<b>Максимальная длина поста 1000 символов</b>
        '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_link)


@dp.callback_query_handler(text='add_link', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    await CreatePost.Q1.set()
    text = '''<b>Пришлите текст поста</b>
    
Рекомендуется присылать не готовый пост с канала с его форматированием, а сокращенный.

Единственная ошибка которая может возникнуть это ошибка с разметкой курсивом.
Когда в ссылке есть нижнее подчеркивание, оно воспринимается как часть незавершенной разметки.

<b>Все ссылки рекомендуется прятать в текст:</b>
<code>[текст](ссылка)</code>
В таком случае ошибок точно не будет

<b>Бот в любом случае сообщит об ошибке</b>

Разметка: Markdown
    '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_return_link)


@dp.callback_query_handler(text='edit_link', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    await EditPost.E1.set()
    text = 'Вы можете прислать аргумент<b>(start=аргумент)</b> или прислать саму ссылку с аргументом'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_return_link)


@dp.callback_query_handler(text='block_link', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    await BanPost.B1.set()
    text = 'Вы можете прислать аргумент<b>(start=аргумент)</b> или прислать саму ссылку с аргументом'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_return_link)


@dp.callback_query_handler(text='start_return', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
        '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_after_start)
