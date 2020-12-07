from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from loader import bot


async def update_key(chat_id, message_id):
    key_under_blurb = InlineKeyboardMarkup(row_width=3)
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
    key_under_blurb.insert(o)
    key_under_blurb.insert(n)
    key_under_blurb.insert(p)
    key_under_blurb.insert(b)
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=key_under_blurb)


async def s_mes(chat_id, e):
    text = f'Ошибка в разметке, попробуйте снова {e}'
    key_under_blurb = InlineKeyboardMarkup(row_width=3)
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
    key_under_blurb.insert(o)
    key_under_blurb.insert(n)
    key_under_blurb.insert(p)
    key_under_blurb.insert(b)
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=key_under_blurb)