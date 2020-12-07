from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from keyboards.Inline.admin_blurb import key_blurb, \
    key_blurb_back_1, key_blurb_back_3, key_blurb_back_2, key_blurb_back_4, key_addKey, key_addKey_back
from loader import bot, dp, r, db
from state import CreateBlurb
from utils.key_split import key_split
from utils.rewriting import rewriting_for_stat


@dp.message_handler(state=CreateBlurb.Blurb1)
async def get_blurb_text(message: types.Message):
    try:
        answer = message.text
        if answer.__contains__('_') and config.parse_blurb == 'Markdown':
            config.text_blurb = answer.replace('_', '\\_')
        else:
            config.text_blurb = answer
        text = '{}'.format(config.text_blurb)
        if config.preview_blurb == 1:
            await message.answer(text, parse_mode=config.parse_blurb,
                                 disable_web_page_preview=True, reply_markup=key_addKey)
        else:
            await message.answer(text, parse_mode=config.parse_blurb,
                                 disable_web_page_preview=False, reply_markup=key_addKey)
        await CreateBlurb.text.set()
    except Exception as e:
        if config.parse_blurb == 'Markdown':
            if config.preview_blurb == 0:
                key_blurb_back = key_blurb_back_1
            else:
                key_blurb_back = key_blurb_back_2
        else:
            if config.preview_blurb == 0:
                key_blurb_back = key_blurb_back_3
            else:
                key_blurb_back = key_blurb_back_4
        await message.answer(f'Ошибка в разметке, попробуйте снова {e}', reply_markup=key_blurb_back)


@dp.message_handler(state=CreateBlurb.text_key)
async def add_key_for_text(message: types.Message):
    if await key_split(message.text):
        await CreateBlurb.text.set()
        key_under_blurb = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
        j = InlineKeyboardButton(text='Удалить кнопку', callback_data='del_key_blurb')
        m = InlineKeyboardButton(text='Сохранить', callback_data='save_blurb')
        n = InlineKeyboardButton(text='Назад', callback_data='add_blurb')
        key_under_blurb.insert(k)
        key_under_blurb.insert(j)
        key_under_blurb.insert(m)
        key_under_blurb.insert(n)
        text = '{}'.format(config.text_blurb)
        if config.preview_blurb == 1:
            await message.answer(text=text, parse_mode=config.parse_blurb,
                                 disable_web_page_preview=True, reply_markup=key_under_blurb)
        else:
            await message.answer(text=text, parse_mode=config.parse_blurb,
                                 disable_web_page_preview=False, reply_markup=key_under_blurb)
    else:
        await message.answer('Не правильно переданы параметры, повторите попытку', reply_markup=key_addKey_back)


@dp.message_handler(state=CreateBlurb.Blurb1, content_types=ContentType.PHOTO)
async def get_blurb_photo(message: types.Message):
    try:
        config.photo_blurb = message.photo[-1].file_id
        answer = message.caption
        if answer.__contains__('_') and config.parse_blurb == 'Markdown':
            config.caption_blurb = answer.replace('_', '\\_')
        else:
            config.caption_blurb = answer
        await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb, caption=config.caption_blurb,
                             parse_mode=config.parse_blurb, disable_notification=True, reply_markup=key_addKey)
        await CreateBlurb.photo.set()
    except Exception as e:
        if config.parse_blurb == 'Markdown':
            if config.preview_blurb == 0:
                key_blurb_back = key_blurb_back_1
            else:
                key_blurb_back = key_blurb_back_2
        else:
            if config.preview_blurb == 0:
                key_blurb_back = key_blurb_back_3
            else:
                key_blurb_back = key_blurb_back_4
        await message.answer(f'Ошибка в обработке фото, попробуйте снова {e}', reply_markup=key_blurb_back)


@dp.message_handler(state=CreateBlurb.photo_key)
async def add_key_for_text(message: types.Message):
    if await key_split(message.text):
        await CreateBlurb.photo.set()
        key_under_blurb = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
        j = InlineKeyboardButton(text='Удалить кнопку', callback_data='del_key_blurb')
        m = InlineKeyboardButton(text='Сохранить', callback_data='save_blurb')
        n = InlineKeyboardButton(text='Назад', callback_data='add_blurb')
        key_under_blurb.insert(k)
        key_under_blurb.insert(j)
        key_under_blurb.insert(m)
        key_under_blurb.insert(n)
        await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb, caption=config.caption_blurb,
                             parse_mode=config.parse_blurb,
                             disable_notification=True, reply_markup=key_under_blurb)
    else:
        await message.answer('Не правильно переданы параметры, повторите попытку', reply_markup=key_addKey_back)


@dp.message_handler(state=CreateBlurb.Blurb1, content_types=ContentType.VIDEO)
async def get_blurb_photo(message: types.Message):
    try:
        config.video_blurb = message.video.file_id
        answer = message.caption
        if answer.__contains__('_') and config.parse_blurb == 'Markdown':
            config.caption_blurb = answer.replace('_', '\\_')
        else:
            config.caption_blurb = answer
        await bot.send_video(chat_id=message.chat.id, video=config.video_blurb, caption=config.caption_blurb,
                             parse_mode=config.parse_blurb, disable_notification=True, reply_markup=key_addKey)
        await CreateBlurb.video.set()
    except Exception as e:
        if config.parse_blurb == 'Markdown':
            if config.preview_blurb == 0:
                key_blurb_back = key_blurb_back_1
            else:
                key_blurb_back = key_blurb_back_2
        else:
            if config.preview_blurb == 0:
                key_blurb_back = key_blurb_back_3
            else:
                key_blurb_back = key_blurb_back_4
        await message.answer(f'Ошибка в обработке фото, попробуйте снова {e}', reply_markup=key_blurb_back)


@dp.message_handler(state=CreateBlurb.video_key)
async def add_key_for_text(message: types.Message):
    if await key_split(message.text):
        await CreateBlurb.video.set()
        key_under_blurb = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
        j = InlineKeyboardButton(text='Удалить кнопку', callback_data='del_key_blurb')
        m = InlineKeyboardButton(text='Сохранить', callback_data='save_blurb')
        n = InlineKeyboardButton(text='Назад', callback_data='add_blurb')
        key_under_blurb.insert(k)
        key_under_blurb.insert(j)
        key_under_blurb.insert(m)
        key_under_blurb.insert(n)
        await bot.send_video(chat_id=message.chat.id, video=config.video_blurb, caption=config.caption_blurb,
                             parse_mode=config.parse_blurb,
                             disable_notification=True, reply_markup=key_under_blurb)
    else:
        await message.answer('Не правильно переданы параметры, повторите попытку', reply_markup=key_addKey_back)


@dp.callback_query_handler(text='blurb', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    text = '''<b>Дополнительное сообщение</b>
    
Каждый пользователь может получить сообщение только один раз
Всё интуитивно должно быть понятно - инструкция не прилагается

У тебя будет возможность редактировать разметку/препросмотр и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью можно редактировать

В базу данных эти изменения тоже не попадут

<b>Обязательно удалять сообщение перед созданием нового</b>

'''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_blurb)


@dp.callback_query_handler(text='blurb', user_id=config.admins, state=CreateBlurb.Blurb1)
async def call_add_link(call: CallbackQuery, state: FSMContext):
    await state.finish()
    config.photo_blurb = ''
    config.caption_blurb = ''
    config.text_blurb = ''
    config.parse_blurb = 'Markdown'
    config.url_text_blurb = ''
    config.url_link_blurb = ''
    config.notification_blurb = 0
    config.save_blurb = 0
    await call.answer()
    text = '''<b>Дополнительное сообщение</b>

Каждый пользователь может получить сообщение только один раз
Всё интуитивно должно быть понятно - инструкция не прилагается

У тебя будет возможность редактировать разметку/препросмотр и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью можно редактировать

В базу данных эти изменения тоже не попадут

<b>Обязательно удалять сообщение перед созданием нового</b>

    '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_blurb)


@dp.callback_query_handler(text='add_blurb', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await CreateBlurb.Blurb1.set()
    await call.answer()
    text = '<b>Добавление поста</b>\n\n' \
           'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_blurb_back)


@dp.callback_query_handler(text='add_blurb', user_id=config.admins, state=CreateBlurb.text)
async def call_add_link(call: CallbackQuery):
    await CreateBlurb.Blurb1.set()
    await call.answer()
    text = '<b>Добавление поста</b>\n\n' \
           'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_blurb_back)


@dp.callback_query_handler(text='add_blurb', user_id=config.admins, state=CreateBlurb.photo)
async def call_add_link(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await CreateBlurb.Blurb1.set()
    await call.answer()
    text = '<b>Добавление поста</b>\n\n' \
           'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_blurb_back)


@dp.callback_query_handler(text='add_blurb', user_id=config.admins, state=CreateBlurb.video)
async def call_add_link(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await CreateBlurb.Blurb1.set()
    await call.answer()
    text = '<b>Добавление поста</b>\n\n' \
           'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_blurb_back)


@dp.callback_query_handler(text='del_blurb', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    config.photo_blurb = ''
    config.caption_blurb = ''
    config.text_blurb = ''
    config.parse_blurb = 'Markdown'
    config.url_text_blurb = ''
    config.url_link_blurb = ''
    config.preview_blurb = 0
    config.save_blurb = 0
    await db.blurb_del()
    await call.answer(text='Доп сообщение удалено', show_alert=True)


@dp.callback_query_handler(text='parse_m', user_id=config.admins, state=CreateBlurb.Blurb1)
async def p_mark(call: CallbackQuery):
    await call.answer()
    config.parse_blurb = 'Markdown'
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_blurb_back)


@dp.callback_query_handler(text='parse_h', user_id=config.admins, state=CreateBlurb.Blurb1)
async def p_mark(call: CallbackQuery):
    await call.answer()
    config.parse_blurb = 'HTML'
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_blurb_back)


@dp.callback_query_handler(text='preview_off', user_id=config.admins, state=CreateBlurb.Blurb1)
async def p_mark(call: CallbackQuery):
    await call.answer()
    config.preview_blurb = 1
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_blurb_back)


@dp.callback_query_handler(text='preview_on', user_id=config.admins, state=CreateBlurb.Blurb1)
async def p_mark(call: CallbackQuery):
    await call.answer()
    config.preview_blurb = 0
    if config.parse_blurb == 'Markdown':
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_1
        else:
            key_blurb_back = key_blurb_back_2
    else:
        if config.preview_blurb == 0:
            key_blurb_back = key_blurb_back_3
        else:
            key_blurb_back = key_blurb_back_4
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_blurb_back)


@dp.callback_query_handler(text='add_key_blurb', user_id=config.admins, state=CreateBlurb.text)
async def p_mark(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await CreateBlurb.text_key.set()
    await bot.send_message(chat_id=call.message.chat.id, text='Отправьте текст кнопки в формате:\n\n'
                                                              'Текст кнопки - ссылка\n\nКнопка может быть только одна',
                           reply_markup=key_addKey_back)


@dp.callback_query_handler(text='add_key_blurb', user_id=config.admins, state=CreateBlurb.photo)
async def p_mark(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await CreateBlurb.photo_key.set()
    await bot.send_message(chat_id=call.message.chat.id, text='Отправьте текст кнопки в формате:\n\n'
                                                              'Текст кнопки - ссылка\n\nКнопка может быть только одна',
                           reply_markup=key_addKey_back)


@dp.callback_query_handler(text='add_key_blurb', user_id=config.admins, state=CreateBlurb.video)
async def p_mark(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await CreateBlurb.video_key.set()
    await bot.send_message(chat_id=call.message.chat.id, text='Отправьте текст кнопки в формате:\n\n'
                                                              'Текст кнопки - ссылка\n\nКнопка может быть только одна',
                           reply_markup=key_addKey_back)


@dp.callback_query_handler(text='add_key_back', user_id=config.admins, state=CreateBlurb.text_key)
async def back_key(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    text = '{}'.format(config.text_blurb)
    if config.preview_blurb == 1:
        await bot.send_message(chat_id=call.message.chat.id, text=text, parse_mode=config.parse_blurb,
                               disable_web_page_preview=True, reply_markup=key_addKey)
    else:
        await bot.send_message(chat_id=call.message.chat.id, text=text, parse_mode=config.parse_blurb,
                               disable_web_page_preview=False, reply_markup=key_addKey)
    await CreateBlurb.text.set()


@dp.callback_query_handler(text='add_key_back', user_id=config.admins, state=CreateBlurb.photo_key)
async def back_key(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.send_photo(chat_id=call.message.chat.id, photo=config.photo_blurb, caption=config.caption_blurb,
                         parse_mode=config.parse_blurb, disable_notification=True, reply_markup=key_addKey)
    await CreateBlurb.photo.set()


@dp.callback_query_handler(text='add_key_back', user_id=config.admins, state=CreateBlurb.video_key)
async def back_key(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.send_video(chat_id=call.message.chat.id, video=config.video_blurb, caption=config.caption_blurb,
                         parse_mode=config.parse_blurb, disable_notification=True, reply_markup=key_addKey)
    await CreateBlurb.video.set()


@dp.callback_query_handler(text='del_key_blurb', user_id=config.admins, state=CreateBlurb.text)
async def del_key_blurb(call: CallbackQuery):
    config.url_text_blurb = ''
    config.url_link_blurb = ''
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_addKey)


@dp.callback_query_handler(text='del_key_blurb', user_id=config.admins, state=CreateBlurb.photo)
async def del_key_blurb(call: CallbackQuery):
    config.url_text_blurb = ''
    config.url_link_blurb = ''
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_addKey)


@dp.callback_query_handler(text='del_key_blurb', user_id=config.admins, state=CreateBlurb.video)
async def del_key_blurb(call: CallbackQuery):
    config.url_text_blurb = ''
    config.url_link_blurb = ''
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_addKey)


@dp.callback_query_handler(text='save_blurb', user_id=config.admins, state=CreateBlurb.text)
async def p_mark(call: CallbackQuery, state: FSMContext):
    await r.param_blurb()
    await db.update_blurb()
    await rewriting_for_stat(del_us=1)
    config.video_blurb = ''
    config.photo_blurb = ''
    config.caption_blurb = ''
    await call.answer(text='Пост успешно сохранен', show_alert=True)
    if len(config.url_text_blurb) > 1:
        key_under_blurb = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
        key_under_blurb.insert(k)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=key_under_blurb)
    else:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=None)
    config.save_blurb = 1
    text = '''<b>Дополнительное сообщение</b>

Каждый пользователь может получить сообщение только один раз
Всё интуитивно должно быть понятно - инструкция не прилагается

У тебя будет возможность редактировать разметку/препросмотр и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью можно редактировать

В базу данных эти изменения тоже не попадут

<b>Обязательно удалять сообщение перед созданием нового</b>

        '''
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_blurb)
    await state.finish()


@dp.callback_query_handler(text='save_blurb', user_id=config.admins, state=CreateBlurb.photo)
async def p_mark(call: CallbackQuery, state: FSMContext):
    await r.param_blurb()
    await db.update_blurb()
    await rewriting_for_stat(del_us=1)
    config.video_blurb = ''
    config.text_blurb = ''
    await call.answer(text='Пост успешно сохранен', show_alert=True)
    if len(config.url_text_blurb) > 1:
        key_under_blurb = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
        key_under_blurb.insert(k)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=key_under_blurb)
    else:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=None)
    config.save_blurb = 1
    text = '''<b>Дополнительное сообщение</b>

Каждый пользователь может получить сообщение только один раз
Всё интуитивно должно быть понятно - инструкция не прилагается

У тебя будет возможность редактировать разметку/препросмотр и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью можно редактировать

В базу данных эти изменения тоже не попадут

<b>Обязательно удалять сообщение перед созданием нового</b>

        '''
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_blurb)
    await state.finish()


@dp.callback_query_handler(text='save_blurb', user_id=config.admins, state=CreateBlurb.video)
async def p_mark(call: CallbackQuery, state: FSMContext):
    await r.param_blurb()
    await db.update_blurb()
    await rewriting_for_stat(del_us=1)
    config.photo_blurb = ''
    config.text_blurb = ''
    await call.answer(text='Пост успешно сохранен', show_alert=True)
    if len(config.url_text_blurb) > 1:
        key_under_blurb = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
        key_under_blurb.insert(k)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=key_under_blurb)
    else:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=None)
    config.save_blurb = 1
    text = '''<b>Дополнительное сообщение</b>

Каждый пользователь может получить сообщение только один раз
Всё интуитивно должно быть понятно - инструкция не прилагается

У тебя будет возможность редактировать разметку/препросмотр и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью можно редактировать

В базу данных эти изменения тоже не попадут

<b>Обязательно удалять сообщение перед созданием нового</b>

        '''
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_blurb)
    await state.finish()
