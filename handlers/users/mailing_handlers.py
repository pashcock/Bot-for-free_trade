from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from keyboards.Inline.admin_key import key_mailing, key_addKey_mail, key_addKey_mail_back, key_conf_mailing, \
    key_confirm, key_promotion
from loader import bot, dp, r, db
from state import CreateMail, ConfMail
from utils.func_up_mes import update_key, s_mes
from utils.key_split import key_split_mail
from utils.mail_process import send_mail
from utils.rewriting import rewriting_for_stat


@dp.message_handler(state=CreateMail.Mail)
async def get_mail_text(message: types.Message):
    try:
        answer = message.text
        if answer.__contains__('_') and config.parse_mail == 'Markdown':
            config.text_mail = answer.replace('_', '\\_')
        else:
            config.text_mail = answer
        text = '{}'.format(config.text_mail)
        if config.preview_mail == 1:
            await message.answer(text, parse_mode=config.parse_mail,
                                 disable_web_page_preview=True, reply_markup=key_addKey_mail)
        else:
            await message.answer(text, parse_mode=config.parse_mail,
                                 disable_web_page_preview=False, reply_markup=key_addKey_mail)
        await CreateMail.text.set()
    except Exception as e:
        await s_mes(message.chat.id, e)


@dp.message_handler(state=CreateMail.text_key)
async def add_key_for_text(message: types.Message):
    if await key_split_mail(message.text):
        await CreateMail.text.set()
        key_under_mail = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
        j = InlineKeyboardButton(text='Удалить кнопку', callback_data='del_key_mail')
        m = InlineKeyboardButton(text='Сохранить', callback_data='save_mail')
        n = InlineKeyboardButton(text='Назад', callback_data='add_mail')
        key_under_mail.insert(k)
        key_under_mail.insert(j)
        key_under_mail.insert(m)
        key_under_mail.insert(n)
        text = '{}'.format(config.text_mail)
        if config.preview_mail == 1:
            await message.answer(text=text, parse_mode=config.parse_mail,
                                 disable_web_page_preview=True, reply_markup=key_under_mail)
        else:
            await message.answer(text=text, parse_mode=config.parse_mail,
                                 disable_web_page_preview=False, reply_markup=key_under_mail)
    else:
        await message.answer('Не правильно переданы параметры, повторите попытку', reply_markup=key_addKey_mail_back)


@dp.message_handler(state=CreateMail.Mail, content_types=ContentType.PHOTO)
async def get_mail_photo(message: types.Message):
    try:
        config.photo_mail = message.photo[-1].file_id
        answer = message.caption
        if answer.__contains__('_') and config.parse_mail == 'Markdown':
            config.caption_mail = answer.replace('_', '\\_')
        else:
            config.caption_mail = answer
        await bot.send_photo(chat_id=message.chat.id, photo=config.photo_mail, caption=config.caption_mail,
                             parse_mode=config.parse_mail, disable_notification=True, reply_markup=key_addKey_mail)
        await CreateMail.photo.set()
    except Exception as e:
        await s_mes(message.chat.id, e)


@dp.message_handler(state=CreateMail.photo_key)
async def add_key_for_text(message: types.Message):
    if await key_split_mail(message.text):
        await CreateMail.photo.set()
        key_under_mail = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
        j = InlineKeyboardButton(text='Удалить кнопку', callback_data='del_key_mail')
        m = InlineKeyboardButton(text='Сохранить', callback_data='save_mail')
        n = InlineKeyboardButton(text='Назад', callback_data='add_mail')
        key_under_mail.insert(k)
        key_under_mail.insert(j)
        key_under_mail.insert(m)
        key_under_mail.insert(n)
        await bot.send_photo(chat_id=message.chat.id, photo=config.photo_mail, caption=config.caption_mail,
                             parse_mode=config.parse_mail,
                             disable_notification=True, reply_markup=key_under_mail)
    else:
        await message.answer('Не правильно переданы параметры, повторите попытку', reply_markup=key_addKey_mail_back)


@dp.message_handler(state=CreateMail.Mail, content_types=ContentType.VIDEO)
async def get_mail_video(message: types.Message):
    try:
        config.video_mail = message.video.file_id
        answer = message.caption
        if answer.__contains__('_') and config.parse_mail == 'Markdown':
            config.caption_mail = answer.replace('_', '\\_')
        else:
            config.caption_mail = answer
        await bot.send_video(chat_id=message.chat.id, video=config.video_mail, caption=config.caption_mail,
                             parse_mode=config.parse_mail, disable_notification=True, reply_markup=key_addKey_mail)
        await CreateMail.video.set()
    except Exception as e:
        await s_mes(message.chat.id, e)


@dp.message_handler(state=CreateMail.video_key)
async def add_key_for_text(message: types.Message):
    if await key_split_mail(message.text):
        await CreateMail.video.set()
        key_under_mail = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
        j = InlineKeyboardButton(text='Удалить кнопку', callback_data='del_key_mail')
        m = InlineKeyboardButton(text='Сохранить', callback_data='save_mail')
        n = InlineKeyboardButton(text='Назад', callback_data='add_mail')
        key_under_mail.insert(k)
        key_under_mail.insert(j)
        key_under_mail.insert(m)
        key_under_mail.insert(n)
        await bot.send_video(chat_id=message.chat.id, video=config.video_mail, caption=config.caption_mail,
                             parse_mode=config.parse_mail,
                             disable_notification=True, reply_markup=key_under_mail)
    else:
        await message.answer('Не правильно переданы параметры, повторите попытку', reply_markup=key_addKey_mail_back)


@dp.callback_query_handler(text='add_key_mail', user_id=config.admins, state=CreateMail.text)
async def p_mark(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await CreateMail.text_key.set()
    await bot.send_message(chat_id=call.message.chat.id, text='Отправьте текст кнопки в формате:\n\n'
                                                              'Текст кнопки - ссылка\n\nКнопка может быть только одна',
                           reply_markup=key_addKey_mail_back)


@dp.callback_query_handler(text='add_key_mail', user_id=config.admins, state=CreateMail.photo)
async def p_mark(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await CreateMail.photo_key.set()
    await bot.send_message(chat_id=call.message.chat.id, text='Отправьте текст кнопки в формате:\n\n'
                                                              'Текст кнопки - ссылка\n\nКнопка может быть только одна',
                           reply_markup=key_addKey_mail_back)


@dp.callback_query_handler(text='add_key_mail', user_id=config.admins, state=CreateMail.video)
async def p_mark(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await CreateMail.video_key.set()
    await bot.send_message(chat_id=call.message.chat.id, text='Отправьте текст кнопки в формате:\n\n'
                                                              'Текст кнопки - ссылка\n\nКнопка может быть только одна',
                           reply_markup=key_addKey_mail_back)


@dp.callback_query_handler(text='add_key_back_mail', user_id=config.admins, state=CreateMail.text_key)
async def back_key(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    text = '{}'.format(config.text_mail)
    if config.preview_mail == 1:
        await bot.send_message(chat_id=call.message.chat.id, text=text, parse_mode=config.parse_mail,
                               disable_web_page_preview=True, reply_markup=key_addKey_mail)
    else:
        await bot.send_message(chat_id=call.message.chat.id, text=text, parse_mode=config.parse_mail,
                               disable_web_page_preview=False, reply_markup=key_addKey_mail)
    await CreateMail.text.set()


@dp.callback_query_handler(text='add_key_back_mail', user_id=config.admins, state=CreateMail.photo_key)
async def back_key(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.send_photo(chat_id=call.message.chat.id, photo=config.photo_mail, caption=config.caption_mail,
                         parse_mode=config.parse_mail, disable_notification=True, reply_markup=key_addKey_mail)
    await CreateMail.photo.set()


@dp.callback_query_handler(text='add_key_back_mail', user_id=config.admins, state=CreateMail.video_key)
async def back_key(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.send_video(chat_id=call.message.chat.id, video=config.video_mail, caption=config.caption_mail,
                         parse_mode=config.parse_mail, disable_notification=True, reply_markup=key_addKey_mail)
    await CreateMail.video.set()


@dp.callback_query_handler(text='del_key_mail', user_id=config.admins, state=CreateMail.text)
async def del_key_mail(call: CallbackQuery):
    await call.answer()
    config.url_text_mail = ''
    config.url_link_mail = ''
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_addKey_mail)


@dp.callback_query_handler(text='del_key_mail', user_id=config.admins, state=CreateMail.photo)
async def del_key_mail(call: CallbackQuery):
    await call.answer()
    config.url_text_mail = ''
    config.url_link_mail = ''
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_addKey_mail)


@dp.callback_query_handler(text='del_key_mail', user_id=config.admins, state=CreateMail.video)
async def del_key_mail(call: CallbackQuery):
    await call.answer()
    config.url_text_mail = ''
    config.url_link_mail = ''
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=key_addKey_mail)


@dp.callback_query_handler(text='save_mail', user_id=config.admins, state=CreateMail.text)
async def p_mark(call: CallbackQuery, state: FSMContext):
    await r.param_mail()
    await db.update_mail()
    await rewriting_for_stat(del_us=0)
    config.video_mail = ''
    config.photo_mail = ''
    config.caption_mail = ''
    await call.answer(text='Пост успешно сохранен', show_alert=True)
    if len(config.url_text_mail) > 1:
        key_under_mail = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
        key_under_mail.insert(k)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=key_under_mail)
    else:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=None)
    config.save_mail = 1
    text = '''<b>Рассылка></b>
    
Инструкций по созданию сообщения нема - всё так же как в доп сообщении

Удалять также можно бесконечное кол-во раз

У тебя будет возможность редактировать разметку/препросмотр/звук и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью/звук можно редактировать

В базу данных эти изменения тоже не попадут - тут база не так важна, 
ибо бот не контролирует завершение рассылки - в случае сбоя рассылка не продолжится
(в теории могу сделать, но не думаю что это необходимо)

<b>Обязательно удалять сообщение перед созданием нового</b>
    '''
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_mailing)
    await state.finish()


@dp.callback_query_handler(text='save_mail', user_id=config.admins, state=CreateMail.photo)
async def p_mark(call: CallbackQuery, state: FSMContext):
    await r.param_mail()
    await db.update_mail()
    await rewriting_for_stat(del_us=0)
    config.video_mail = ''
    config.text_mail = ''
    await call.answer(text='Пост успешно сохранен', show_alert=True)
    if len(config.url_text_mail) > 1:
        key_under_mail = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
        key_under_mail.insert(k)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=key_under_mail)
    else:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=None)
    config.save_mail = 1
    text = '''<b>Рассылка></b>

Инструкций по созданию сообщения нема - всё так же как в доп сообщении

Удалять также можно бесконечное кол-во раз

У тебя будет возможность редактировать разметку/препросмотр/звук и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью/звук можно редактировать

В базу данных эти изменения тоже не попадут - тут база не так важна, 
ибо бот не контролирует завершение рассылки - в случае сбоя рассылка не продолжится
(в теории могу сделать, но не думаю что это необходимо)

<b>Обязательно удалять сообщение перед созданием нового</b>
        '''
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_mailing)
    await state.finish()


@dp.callback_query_handler(text='save_mail', user_id=config.admins, state=CreateMail.video)
async def p_mark(call: CallbackQuery, state: FSMContext):
    await r.param_mail()
    await db.update_mail()
    await rewriting_for_stat(del_us=0)
    config.photo_mail = ''
    config.text_mail = ''
    await call.answer(text='Пост успешно сохранен', show_alert=True)
    if len(config.url_text_mail) > 1:
        key_under_mail = InlineKeyboardMarkup(row_width=1)
        k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
        key_under_mail.insert(k)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=key_under_mail)
    else:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=None)
    config.save_mail = 1
    text = '''<b>Рассылка></b>

Инструкций по созданию сообщения нема - всё так же как в доп сообщении

Удалять также можно бесконечное кол-во раз

У тебя будет возможность редактировать разметку/препросмотр/звук и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью/звук можно редактировать

В базу данных эти изменения тоже не попадут - тут база не так важна, 
ибо бот не контролирует завершение рассылки - в случае сбоя рассылка не продолжится
(в теории могу сделать, но не думаю что это необходимо)

<b>Обязательно удалять сообщение перед созданием нового</b>
        '''
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_mailing)
    await state.finish()


@dp.callback_query_handler(text='mailing', user_id=config.admins)
async def mailing(call: types.CallbackQuery):
    await call.answer()
    text = '''<b>Рассылка></b>

Инструкций по созданию сообщения нема - всё так же как в доп сообщении

Удалять также можно бесконечное кол-во раз

У тебя будет возможность редактировать разметку/препросмотр/звук и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью/звук можно редактировать

В базу данных эти изменения тоже не попадут - тут база не так важна, 
ибо бот не контролирует завершение рассылки - в случае сбоя рассылка не продолжится
(в теории могу сделать, но не думаю что это необходимо)

<b>Обязательно удалять сообщение перед созданием нового</b>
        '''
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=text, reply_markup=key_mailing)


@dp.callback_query_handler(text='mailing', user_id=config.admins, state=CreateMail.Mail)
async def mailing(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    text = '''<b>Рассылка></b>

Инструкций по созданию сообщения нема - всё так же как в доп сообщении

Удалять также можно бесконечное кол-во раз

У тебя будет возможность редактировать разметку/препросмотр/звук и после создания поста.
Однако это не рекомендуется(разметка может сломать сообщение) - бот не упадет, но пользователи сообщение не получат.
Превью/звук можно редактировать

В базу данных эти изменения тоже не попадут - тут база не так важна, 
ибо бот не контролирует завершение рассылки - в случае сбоя рассылка не продолжится
(в теории могу сделать, но не думаю что это необходимо)

<b>Обязательно удалять сообщение перед созданием нового</b>
        '''
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=text, reply_markup=key_mailing)


@dp.callback_query_handler(text='add_mail', user_id=config.admins)
async def active_get_state(call: types.CallbackQuery):
    await call.answer()
    await CreateMail.Mail.set()
    text = 'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    key_under_mail = InlineKeyboardMarkup(row_width=3)
    if config.parse_mail == 'Markdown':
        o = InlineKeyboardButton(text='Markdown', callback_data='HTML')
    else:
        o = InlineKeyboardButton(text='HTML', callback_data='Markdown')
    if config.notification_mail == 0:
        n = InlineKeyboardButton(text='Звук вкл', callback_data='dis_not')
    else:
        n = InlineKeyboardButton(text='Звук выкл', callback_data='act_not')
    if config.preview_mail == 0:
        p = InlineKeyboardButton(text='С превью', callback_data='pre_off')
    else:
        p = InlineKeyboardButton(text='Без превью', callback_data='pre_on')
    b = InlineKeyboardButton(text='Назад', callback_data='mailing')
    key_under_mail.insert(o)
    key_under_mail.insert(n)
    key_under_mail.insert(p)
    key_under_mail.insert(b)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=text, reply_markup=key_under_mail)


@dp.callback_query_handler(text='add_mail', user_id=config.admins, state=CreateMail.text)
async def active_get_state(call: types.CallbackQuery):
    await call.answer()
    await CreateMail.Mail.set()
    text = 'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    key_under_mail = InlineKeyboardMarkup(row_width=3)
    if config.parse_mail == 'Markdown':
        o = InlineKeyboardButton(text='Markdown', callback_data='HTML')
    else:
        o = InlineKeyboardButton(text='HTML', callback_data='Markdown')
    if config.notification_mail == 0:
        n = InlineKeyboardButton(text='Звук вкл', callback_data='dis_not')
    else:
        n = InlineKeyboardButton(text='Звук выкл', callback_data='act_not')
    if config.preview_mail == 0:
        p = InlineKeyboardButton(text='С превью', callback_data='pre_off')
    else:
        p = InlineKeyboardButton(text='Без превью', callback_data='pre_on')
    b = InlineKeyboardButton(text='Назад', callback_data='mailing')
    key_under_mail.insert(o)
    key_under_mail.insert(n)
    key_under_mail.insert(p)
    key_under_mail.insert(b)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=text, reply_markup=key_under_mail)


@dp.callback_query_handler(text='add_mail', user_id=config.admins, state=CreateMail.photo)
async def call_add_link(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await CreateMail.Mail.set()
    await call.answer()
    text = 'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    key_under_mail = InlineKeyboardMarkup(row_width=3)
    if config.parse_mail == 'Markdown':
        o = InlineKeyboardButton(text='Markdown', callback_data='HTML')
    else:
        o = InlineKeyboardButton(text='HTML', callback_data='Markdown')
    if config.notification_mail == 0:
        n = InlineKeyboardButton(text='Звук вкл', callback_data='dis_not')
    else:
        n = InlineKeyboardButton(text='Звук выкл', callback_data='act_not')
    if config.preview_mail == 0:
        p = InlineKeyboardButton(text='С превью', callback_data='pre_off')
    else:
        p = InlineKeyboardButton(text='Без превью', callback_data='pre_on')
    b = InlineKeyboardButton(text='Назад', callback_data='mailing')
    key_under_mail.insert(o)
    key_under_mail.insert(n)
    key_under_mail.insert(p)
    key_under_mail.insert(b)
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_under_mail)


@dp.callback_query_handler(text='add_mail', user_id=config.admins, state=CreateMail.video)
async def call_add_link(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await CreateMail.Mail.set()
    await call.answer()
    text = 'Вы можете прислать текстовое сообщение, фото с подписью или видео с подписью\n' \
           'Если нужно использовать много текстовой разметки, то рекомендуется использовать разметку HTML.\n\n\n' \
           'Разметка Markdown будет корректно работать только при использовании жирного шрифта и вставки ' \
           'ссылки в текст\nНельзя использовать нижнеее подчеркивание(_) нигде кроме ссылок, следовательно ' \
           'нельзя сделать шрифт курсивом'
    key_under_mail = InlineKeyboardMarkup(row_width=3)
    if config.parse_mail == 'Markdown':
        o = InlineKeyboardButton(text='Markdown', callback_data='HTML')
    else:
        o = InlineKeyboardButton(text='HTML', callback_data='Markdown')
    if config.notification_mail == 0:
        n = InlineKeyboardButton(text='Звук вкл', callback_data='dis_not')
    else:
        n = InlineKeyboardButton(text='Звук выкл', callback_data='act_not')
    if config.preview_mail == 0:
        p = InlineKeyboardButton(text='С превью', callback_data='pre_off')
    else:
        p = InlineKeyboardButton(text='Без превью', callback_data='pre_on')
    b = InlineKeyboardButton(text='Назад', callback_data='mailing')
    key_under_mail.insert(o)
    key_under_mail.insert(n)
    key_under_mail.insert(p)
    key_under_mail.insert(b)
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_under_mail)


@dp.callback_query_handler(text='del_mail', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    config.photo_mail = ''
    config.caption_mail = ''
    config.text_mail = ''
    config.parse_mail = 'Markdown'
    config.url_text_mail = ''
    config.url_link_mail = ''
    config.notification_mail = 0
    config.preview_mail = 0
    config.save_mail = 0
    await db.mail_del()
    await call.answer(text='Сообщение для рассылки удалено', show_alert=True)


@dp.callback_query_handler(text='HTML', user_id=config.admins, state=CreateMail.Mail)
async def change_parse(call: types.CallbackQuery):
    await call.answer()
    print(1)
    config.parse_mail = 'HTML'
    await update_key(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(text='Markdown', user_id=config.admins, state=CreateMail.Mail)
async def change_parse(call: types.CallbackQuery):
    await call.answer()
    config.parse_mail = 'Markdown'
    await update_key(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(text='dis_not', user_id=config.admins, state=CreateMail.Mail)
async def change_parse(call: types.CallbackQuery):
    await call.answer()
    config.notification_mail = 1
    await update_key(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(text='act_not', user_id=config.admins, state=CreateMail.Mail)
async def change_parse(call: types.CallbackQuery):
    await call.answer()
    config.notification_mail = 0
    await update_key(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(text='pre_off', user_id=config.admins, state=CreateMail.Mail)
async def change_parse(call: types.CallbackQuery):
    await call.answer()
    config.preview_mail = 1
    await update_key(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(text='pre_on', user_id=config.admins, state=CreateMail.Mail)
async def change_parse(call: types.CallbackQuery):
    await call.answer()
    config.preview_mail = 0
    await update_key(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(text='begin_mail', user_id=config.admins)
async def begin_mailing(call: types.CallbackQuery):
    if config.save_mail == 0:
        await call.answer('Функция не доступна\nСообщение для рассылки не подготовлено', show_alert=True)
    else:
        await call.answer()
        text = 'Выберите пользователей, которые получат рассылку:\n\n*Все* - все пользователи\n' \
               '*День* - пользователи за сегодня\n*Неделя* - пользователи за неделю\n' \
               '*Месяц* - пользователи за месяц\n\nРассылка также обновляет кол-во пользователей остановивших бот'
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    parse_mode='Markdown', reply_markup=key_conf_mailing)


@dp.callback_query_handler(text='begin_mail', user_id=config.admins, state=ConfMail.All)
async def begin_mailing(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    if config.save_mail == 0:
        await call.answer('Функция не доступна\nСообщение для рассылки не подготовлено', show_alert=True)
    else:
        await call.answer()
        text = 'Выберите пользователей, которые получат рассылку:\n\n*Все* - все пользователи\n' \
               '*День* - пользователи за сегодня\n*Неделя* - пользователи за неделю\n' \
               '*Месяц* - пользователи за месяц\n\nРассылка также обновляет кол-во пользователей остановивших бот'
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    parse_mode='Markdown', reply_markup=key_conf_mailing)


@dp.callback_query_handler(text='begin_mail', user_id=config.admins, state=ConfMail.Day)
async def begin_mailing(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    if config.save_mail == 0:
        await call.answer('Функция не доступна\nСообщение для рассылки не подготовлено', show_alert=True)
    else:
        await call.answer()
        text = 'Выберите пользователей, которые получат рассылку:\n\n*Все* - все пользователи\n' \
               '*День* - пользователи за сегодня\n*Неделя* - пользователи за неделю\n' \
               '*Месяц* - пользователи за месяц\n\nРассылка также обновляет кол-во пользователей остановивших бот'
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    parse_mode='Markdown', reply_markup=key_conf_mailing)


@dp.callback_query_handler(text='begin_mail', user_id=config.admins, state=ConfMail.Week)
async def begin_mailing(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    if config.save_mail == 0:
        await call.answer('Функция не доступна\nСообщение для рассылки не подготовлено', show_alert=True)
    else:
        await call.answer()
        text = 'Выберите пользователей, которые получат рассылку:\n\n*Все* - все пользователи\n' \
               '*День* - пользователи за сегодня\n*Неделя* - пользователи за неделю\n' \
               '*Месяц* - пользователи за месяц\n\nРассылка также обновляет кол-во пользователей остановивших бот'
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    parse_mode='Markdown', reply_markup=key_conf_mailing)


@dp.callback_query_handler(text='begin_mail', user_id=config.admins, state=ConfMail.Month)
async def begin_mailing(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    if config.save_mail == 0:
        await call.answer('Функция не доступна\nСообщение для рассылки не подготовлено', show_alert=True)
    else:
        await call.answer()
        text = 'Выберите пользователей, которые получат рассылку:\n\n*Все* - все пользователи\n' \
               '*День* - пользователи за сегодня\n*Неделя* - пользователи за неделю\n' \
               '*Месяц* - пользователи за месяц\n\nРассылка также обновляет кол-во пользователей остановивших бот'
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    parse_mode='Markdown', reply_markup=key_conf_mailing)


@dp.callback_query_handler(text='all_mail', user_id=config.admins)
async def all_mail(call: CallbackQuery):
    await ConfMail.All.set()
    text = 'Подтвердите рассылку\n\nГруппа: *Все*'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                parse_mode='Markdown', reply_markup=key_confirm)


@dp.callback_query_handler(text='today_mail', user_id=config.admins)
async def day_mail(call: CallbackQuery):
    await ConfMail.Day.set()
    text = 'Подтвердите рассылку\n\nГруппа: *Сегодня*'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                parse_mode='Markdown', reply_markup=key_confirm)


@dp.callback_query_handler(text='week_mail', user_id=config.admins)
async def day_mail(call: CallbackQuery):
    await ConfMail.Week.set()
    text = 'Подтвердите рассылку\n\nГруппа: *Неделя*'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                parse_mode='Markdown', reply_markup=key_confirm)


@dp.callback_query_handler(text='month_mail', user_id=config.admins)
async def day_mail(call: CallbackQuery):
    await ConfMail.Month.set()
    text = 'Подтвердите рассылку\n\nГруппа: *Месяц*'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                parse_mode='Markdown', reply_markup=key_confirm)


@dp.callback_query_handler(text='confirm_mail', user_id=config.admins, state=ConfMail.All)
async def all_mail_conf(call: CallbackQuery, state: FSMContext):
    await call.answer('Когда рассылка завершится это сообщение обновится', show_alert=True)
    await state.finish()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    text = '''<b>Реклама и статистика</b>

🕸<b>Второй канал</b> - добавить второй обязательный для подписки канал, чтобы у пользователей сильнее подгорало очко
📊<b>Статистика</b> - статистика по пользователям и постам
📩<b>Рассылка</b> - опять же чтобы у людей пылало очко
📝<b>Подпись</b> - подпись на сообщении, причина в рассылке
🖇<b>Доп сообщение</b> - оформление дополнительного сообщения с рекламой, причина см п.3
        '''
    await bot.send_message(text=text, chat_id=call.message.chat.id, reply_markup=key_promotion)
    data = await db.mail_all()
    for p in data:
        print(p[0])
        try:
            await send_mail(p[0])
            await r.mail_increment()
        except Exception as e:
            await db.ban_user(p[0])
    config.save_mail = 0
    quantity = await r.mail_get()
    text = 'Рассылка успешно завершена\n\nКоличество человек получивших пост: {}'.format(quantity)
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(text='confirm_mail', user_id=config.admins, state=ConfMail.Day)
async def all_mail_conf(call: CallbackQuery, state: FSMContext):
    await call.answer('Когда рассылка завершится это сообщение обновится', show_alert=True)
    await state.finish()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    text = '''<b>Реклама и статистика</b>

🕸<b>Второй канал</b> - добавить второй обязательный для подписки канал, чтобы у пользователей сильнее подгорало очко
📊<b>Статистика</b> - статистика по пользователям и постам
📩<b>Рассылка</b> - опять же чтобы у людей пылало очко
📝<b>Подпись</b> - подпись на сообщении, причина в рассылке
🖇<b>Доп сообщение</b> - оформление дополнительного сообщения с рекламой, причина см п.3
        '''
    await bot.send_message(text=text, chat_id=call.message.chat.id, reply_markup=key_promotion)
    data = await db.mail_day()
    for p in data:
        print(p[0])
        try:
            await send_mail(p[0])
            await r.mail_increment()
        except Exception as e:
            await db.ban_user(p[0])
    config.save_mail = 0
    quantity = await r.mail_get()
    text = 'Рассылка успешно завершена\n\nКоличество человек получивших пост: {}'.format(quantity)
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(text='confirm_mail', user_id=config.admins, state=ConfMail.Week)
async def all_mail_conf(call: CallbackQuery, state: FSMContext):
    await call.answer('Когда рассылка завершится это сообщение обновится', show_alert=True)
    await state.finish()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    text = '''<b>Реклама и статистика</b>

🕸<b>Второй канал</b> - добавить второй обязательный для подписки канал, чтобы у пользователей сильнее подгорало очко
📊<b>Статистика</b> - статистика по пользователям и постам
📩<b>Рассылка</b> - опять же чтобы у людей пылало очко
📝<b>Подпись</b> - подпись на сообщении, причина в рассылке
🖇<b>Доп сообщение</b> - оформление дополнительного сообщения с рекламой, причина см п.3
        '''
    await bot.send_message(text=text, chat_id=call.message.chat.id, reply_markup=key_promotion)
    data = await db.mail_week()
    for p in data:
        print(p[0])
        try:
            await send_mail(p[0])
            await r.mail_increment()
        except Exception as e:
            await db.ban_user(p[0])
    config.save_mail = 0
    quantity = await r.mail_get()
    text = 'Рассылка успешно завершена\n\nКоличество человек получивших пост: {}'.format(quantity)
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(text='confirm_mail', user_id=config.admins, state=ConfMail.Month)
async def all_mail_conf(call: CallbackQuery, state: FSMContext):
    await call.answer('Когда рассылка завершится это сообщение обновится', show_alert=True)
    await state.finish()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    text = '''<b>Реклама и статистика</b>

🕸<b>Второй канал</b> - добавить второй обязательный для подписки канал, чтобы у пользователей сильнее подгорало очко
📊<b>Статистика</b> - статистика по пользователям и постам
📩<b>Рассылка</b> - опять же чтобы у людей пылало очко
📝<b>Подпись</b> - подпись на сообщении, причина в рассылке
🖇<b>Доп сообщение</b> - оформление дополнительного сообщения с рекламой, причина см п.3
        '''
    await bot.send_message(text=text, chat_id=call.message.chat.id, reply_markup=key_promotion)
    data = await db.mail_month()
    for p in data:
        print(p[0])
        try:
            await send_mail(p[0])
            await r.mail_increment()
        except Exception as e:
            await db.ban_user(p[0])
    config.save_mail = 0
    quantity = await r.mail_get()
    text = 'Рассылка успешно завершена\n\nКоличество человек получивших пост: {}'.format(quantity)
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id)
