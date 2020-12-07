from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from loader import bot


async def send_mail(chat_id):
    if len(config.text_mail) > 1:
        if len(config.url_text_mail) > 1:
            key_under_mail = InlineKeyboardMarkup()
            k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
            key_under_mail.insert(k)
            if config.preview_mail == 1:
                if config.notification_mail == 1:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=True,
                                           disable_notification=True, reply_markup=key_under_mail)
                else:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=True,
                                           disable_notification=False, reply_markup=key_under_mail)
            else:
                if config.notification_mail == 1:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=False,
                                           disable_notification=True, reply_markup=key_under_mail)
                else:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=False,
                                           disable_notification=False, reply_markup=key_under_mail)
        else:
            if config.preview_mail == 1:
                if config.notification_mail == 1:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=True,
                                           disable_notification=True)
                else:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=True,
                                           disable_notification=False)
            else:
                if config.notification_mail == 1:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=False,
                                           disable_notification=True)
                else:
                    await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                           disable_web_page_preview=False,
                                           disable_notification=False)
    elif len(config.photo_mail) > 1:
        if len(config.url_text_mail) > 1:
            key_under_mail = InlineKeyboardMarkup()
            k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
            key_under_mail.insert(k)
            if config.notification_mail == 1:
                await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=True, reply_markup=key_under_mail)
            else:
                await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=False, reply_markup=key_under_mail)
        else:
            if config.notification_mail == 1:
                await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=True)
            else:
                await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=False)
    elif len(config.video_mail) > 1:
        if len(config.url_text_mail) > 1:
            key_under_mail = InlineKeyboardMarkup()
            k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
            key_under_mail.insert(k)
            if config.notification_mail == 1:
                await bot.send_video(chat_id=chat_id, photo=config.video_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=True, reply_markup=key_under_mail)
            else:
                await bot.send_video(chat_id=chat_id, photo=config.video_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=False, reply_markup=key_under_mail)
        else:
            if config.notification_mail == 1:
                await bot.send_video(chat_id=chat_id, photo=config.video_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=True)
            else:
                await bot.send_video(chat_id=chat_id, photo=config.video_mail,
                                     caption=config.caption_mail,
                                     parse_mode=config.parse_mail,
                                     disable_notification=False)