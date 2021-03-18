from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from loader import bot, db
from asyncio import sleep


async def send_mail(chat_id):
    if len(config.text_mail) > 1:
        if len(config.url_text_mail) > 1:
            key_under_mail = InlineKeyboardMarkup()
            k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
            key_under_mail.insert(k)
            if config.preview_mail == 1:
                if config.notification_mail == 1:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=True,
                                                  disable_notification=True, reply_markup=key_under_mail)
                    return data.message_id
                else:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=True,
                                                  disable_notification=False, reply_markup=key_under_mail)
                    return data.message_id
            else:
                if config.notification_mail == 1:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=False,
                                                  disable_notification=True, reply_markup=key_under_mail)
                    return data.message_id
                else:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=False,
                                                  disable_notification=False, reply_markup=key_under_mail)
                    return data.message_id
        else:
            if config.preview_mail == 1:
                if config.notification_mail == 1:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=True,
                                                  disable_notification=True)
                    return data.message_id
                else:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=True,
                                                  disable_notification=False)
                    return data.message_id
            else:
                if config.notification_mail == 1:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=False,
                                                  disable_notification=True)
                    return data.message_id
                else:
                    data = await bot.send_message(chat_id=chat_id, text=config.text_mail, parse_mode=config.parse_mail,
                                                  disable_web_page_preview=False,
                                                  disable_notification=False)
                    return data.message_id
    elif len(config.photo_mail) > 1:
        if len(config.url_text_mail) > 1:
            key_under_mail = InlineKeyboardMarkup()
            k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
            key_under_mail.insert(k)
            if config.notification_mail == 1:
                data = await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=True, reply_markup=key_under_mail)
                return data.message_id
            else:
                data = await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=False, reply_markup=key_under_mail)
                return data.message_id
        else:
            if config.notification_mail == 1:
                data = await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=True)
                return data.message_id
            else:
                data = await bot.send_photo(chat_id=chat_id, photo=config.photo_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=False)
                return data.message_id
    elif len(config.video_mail) > 1:
        if len(config.url_text_mail) > 1:
            key_under_mail = InlineKeyboardMarkup()
            k = InlineKeyboardButton(text=config.url_text_mail, url=config.url_link_mail)
            key_under_mail.insert(k)
            if config.notification_mail == 1:
                data = await bot.send_video(chat_id=chat_id, video=config.video_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=True, reply_markup=key_under_mail)
                return data.message_id
            else:
                data = await bot.send_video(chat_id=chat_id, video=config.video_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=False, reply_markup=key_under_mail)
                return data.message_id
        else:
            if config.notification_mail == 1:
                data = await bot.send_video(chat_id=chat_id, video=config.video_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=True)
                return data.message_id
            else:
                data = await bot.send_video(chat_id=chat_id, video=config.video_mail,
                                            caption=config.caption_mail,
                                            parse_mode=config.parse_mail,
                                            disable_notification=False)
                return data.message_id


async def delete_mes_mail():
    data = await db.select_mes_mail()
    for p in data:
        try:
            await db.mail_write_mes(user_id=int(p[0]), mes_id=0)
            await bot.delete_message(chat_id=p[0], message_id=p[1])
            await sleep(0.2)
        except:
            pass
