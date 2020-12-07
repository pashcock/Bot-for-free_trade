from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from filters.chat_member import ChatMembers
from loader import dp, bot, db, r
from re import compile


from utils.misc import rate_limit


@rate_limit(limit=1)
@dp.message_handler(CommandStart(deep_link=compile(r"\w\d\w\d\w\d\w\d")), ChatMembers())
async def start_mess_deeplink(message: types.Message):
    await r.write_user(message.chat.id)
    arg = message.get_args()
    text = await db.select_text(arg)
    if text is None:
        await message.answer('Аругмент не верный')
    else:
        if config.additional_channel != '':
            try:
                k = await bot.get_chat(config.additional_channel)
                if 'member' == (await bot.get_chat_member(config.additional_channel, message.chat.id)).status:
                    await db.increment_link(arg=arg)
                    if len(config.caption) > 2:
                        text += str('\n\n\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_'
                                    '\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\n') + str(
                            config.caption)
                    await message.answer('{}'.format(text), parse_mode=types.ParseMode.MARKDOWN,
                                         disable_web_page_preview=True)
                    if config.save_blurb == 1:
                        if await r.get_user(message.chat.id) == '0':
                            await r.increment_user(message.chat.id)
                            await r.par_increment()
                            if len(config.text_blurb) > 1:
                                if len(config.url_text_blurb) > 1:
                                    key_under_blurb = InlineKeyboardMarkup()
                                    k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                                    key_under_blurb.insert(k)
                                    if config.preview_blurb == 1:
                                        await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                             disable_web_page_preview=True,
                                                             disable_notification=True,
                                                             reply_markup=key_under_blurb)
                                    else:
                                        await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                             disable_notification=True,
                                                             reply_markup=key_under_blurb)
                                else:
                                    if config.preview_blurb == 1:
                                        await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                             disable_web_page_preview=True,
                                                             disable_notification=True)
                                    else:
                                        await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                             disable_notification=True)
                            elif len(config.photo_blurb) > 1:
                                if len(config.url_text_blurb) > 1:
                                    key_under_blurb = InlineKeyboardMarkup()
                                    k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                                    key_under_blurb.insert(k)
                                    await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb,
                                                         caption=config.caption_blurb,
                                                         parse_mode=config.parse_blurb,
                                                         disable_notification=True, reply_markup=key_under_blurb)
                                else:
                                    await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb,
                                                         caption=config.caption_blurb,
                                                         parse_mode=config.parse_blurb,
                                                         disable_notification=True)
                            elif len(config.video_blurb) > 1:
                                if len(config.url_text_blurb) > 1:
                                    key_under_blurb = InlineKeyboardMarkup()
                                    k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                                    key_under_blurb.insert(k)
                                    await bot.send_video(chat_id=message.chat.id, video=config.video_blurb,
                                                         caption=config.caption_blurb,
                                                         parse_mode=config.parse_blurb,
                                                         disable_notification=True, reply_markup=key_under_blurb)
                                else:
                                    await bot.send_video(chat_id=message.chat.id, video=config.video_blurb,
                                                         caption=config.caption_blurb,
                                                         parse_mode=config.parse_blurb,
                                                         disable_notification=True)
                else:
                    name = k.title
                    ans = f'Для того чтобы получить курс вы должны быть ' \
                          f'подписаны на [{name}]({config.channel_link})\n\n' \
                          f'Подпишитесь на канал и активируйте бот по ссылке:\n' \
                          f'https://t.me/f\\_trade\\_bot?start={arg}'
                    await message.answer(ans, parse_mode='Markdown')
            except Exception as e:
                await db.increment_link(arg=arg)
                if len(config.caption) > 2:
                    text += str('\n\n\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_'
                                '\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\n') + str(config.caption)
                await message.answer('{}'.format(text), parse_mode=types.ParseMode.MARKDOWN,
                                     disable_web_page_preview=True)
                if config.save_blurb == 1:
                    if await r.get_user(message.chat.id) == '0':
                        await r.increment_user(message.chat.id)
                        await r.par_increment()
                        if len(config.text_blurb) > 1:
                            if len(config.url_text_blurb) > 1:
                                key_under_blurb = InlineKeyboardMarkup()
                                k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                                key_under_blurb.insert(k)
                                if config.preview_blurb == 1:
                                    await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                         disable_web_page_preview=True,
                                                         disable_notification=True,
                                                         reply_markup=key_under_blurb)
                                else:
                                    await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                         disable_notification=True,
                                                         reply_markup=key_under_blurb)
                            else:
                                if config.preview_blurb == 1:
                                    await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                         disable_web_page_preview=True,
                                                         disable_notification=True)
                                else:
                                    await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                         disable_notification=True)
                        elif len(config.photo_blurb) > 1:
                            if len(config.url_text_blurb) > 1:
                                key_under_blurb = InlineKeyboardMarkup()
                                k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                                key_under_blurb.insert(k)
                                await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb,
                                                     caption=config.caption_blurb,
                                                     parse_mode=config.parse_blurb,
                                                     disable_notification=True, reply_markup=key_under_blurb)
                            else:
                                await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb,
                                                     caption=config.caption_blurb,
                                                     parse_mode=config.parse_blurb,
                                                     disable_notification=True)
                        elif len(config.video_blurb) > 1:
                            if len(config.url_text_blurb) > 1:
                                key_under_blurb = InlineKeyboardMarkup()
                                k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                                key_under_blurb.insert(k)
                                await bot.send_video(chat_id=message.chat.id, video=config.video_blurb,
                                                     caption=config.caption_blurb,
                                                     parse_mode=config.parse_blurb,
                                                     disable_notification=True, reply_markup=key_under_blurb)
                            else:
                                await bot.send_video(chat_id=message.chat.id, video=config.video_blurb,
                                                     caption=config.caption_blurb,
                                                     parse_mode=config.parse_blurb,
                                                     disable_notification=True)
        else:
            await db.increment_link(arg=arg)
            if len(config.caption) > 2:
                text += str('\n\n\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_'
                            '\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\n') + str(config.caption)
            await message.answer('{}'.format(text), parse_mode=types.ParseMode.MARKDOWN,
                                 disable_web_page_preview=True)
            if config.save_blurb == 1:
                if await r.get_user(message.chat.id) == '0':
                    await r.increment_user(message.chat.id)
                    await r.par_increment()
                    if len(config.text_blurb) > 1:
                        if len(config.url_text_blurb) > 1:
                            key_under_blurb = InlineKeyboardMarkup()
                            k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                            key_under_blurb.insert(k)
                            if config.preview_blurb == 1:
                                await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                     disable_web_page_preview=True,
                                                     disable_notification=True,
                                                     reply_markup=key_under_blurb)
                            else:
                                await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                     disable_notification=True,
                                                     reply_markup=key_under_blurb)
                        else:
                            if config.preview_blurb == 1:
                                await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                     disable_web_page_preview=True,
                                                     disable_notification=True)
                            else:
                                await message.answer(text=config.text_blurb, parse_mode=config.parse_blurb,
                                                     disable_notification=True)
                    elif len(config.photo_blurb) > 1:
                        if len(config.url_text_blurb) > 1:
                            key_under_blurb = InlineKeyboardMarkup()
                            k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                            key_under_blurb.insert(k)
                            await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb,
                                                 caption=config.caption_blurb,
                                                 parse_mode=config.parse_blurb,
                                                 disable_notification=True, reply_markup=key_under_blurb)
                        else:
                            await bot.send_photo(chat_id=message.chat.id, photo=config.photo_blurb,
                                                 caption=config.caption_blurb,
                                                 parse_mode=config.parse_blurb,
                                                 disable_notification=True)
                    elif len(config.video_blurb) > 1:
                        if len(config.url_text_blurb) > 1:
                            key_under_blurb = InlineKeyboardMarkup()
                            k = InlineKeyboardButton(text=config.url_text_blurb, url=config.url_link_blurb)
                            key_under_blurb.insert(k)
                            await bot.send_video(chat_id=message.chat.id, video=config.video_blurb,
                                                 caption=config.caption_blurb,
                                                 parse_mode=config.parse_blurb,
                                                 disable_notification=True, reply_markup=key_under_blurb)
                        else:
                            await bot.send_video(chat_id=message.chat.id, video=config.video_blurb,
                                                 caption=config.caption_blurb,
                                                 parse_mode=config.parse_blurb,
                                                 disable_notification=True)


@rate_limit(limit=1)
@dp.message_handler(CommandStart(deep_link=compile(r"\w\d\w\d\w\d\w\d")))
async def start_mess_deeplink_m(message: types.Message):
    await r.write_user(message.chat.id)
    arg = message.get_args()
    await message.answer('Для того чтобы скачать курс, вы должны быть подписаны на канал @free_trade\n\n'
                         'Подпишитесь на канал и запустите бота по ссылке:\n'
                         'https://t.me/f_trade_bot?start={}'.format(arg))


@rate_limit(limit=1)
@dp.message_handler(CommandStart(deep_link=compile(r"\S+")), ChatMembers())
async def start_mess_deeplink_m(message: types.Message):
    await r.write_user(message.chat.id)
    arg = message.get_args()
    await message.answer('Ошибка в ссылке:\n'
                         'https://t.me/f_trade_bot?start={}\n\nОбратитесь к администратору @pashcock'.format(arg))


@rate_limit(limit=1)
@dp.message_handler(CommandStart(deep_link=compile(r"\S+")))
async def start_mess_deeplink_m(message: types.Message):
    await r.write_user(message.chat.id)
    arg = message.get_args()
    await message.answer('<b>Для того чтобы скачать курс, вы должны быть подписаны на канал</b> @free_trade\n\n'
                         'Подпишитесь на канал и запустите бота по ссылке:\n'
                         'https://t.me/f_trade_bot?start={}'.format(arg))


@rate_limit(limit=1)
@dp.message_handler(CommandStart(deep_link=None))
async def all_start_mess(message: types.Message):
    await r.write_user(message.chat.id)
    await message.answer('<b>Здравствуйте!</b>\n\nВ этом боте вы можете получить ссылку для'
                         ' скачивания курса с канала @free_trade\nВопросы /help'.format(message.from_user.full_name))


@rate_limit(limit=1)
@dp.message_handler(commands='help')
async def helper(message: types.Message):
    text = '''<b>Помощь</b>
Бот создан, чтобы получать ссылку на скачивание курса от канала @free_trade.
Для использования вы должны быть подписчиком канала.

Когда вы переходите на канал и нажимаете скачать курс, то вас перенаправляет в бота по специальной ссылке.
После перехода вы должны сразу нажать старт - не зависимо от того запускали ли вы ранее бот.
Бот в ответ выдаст вам курс, который вы хотели скачать

Если вам нужна помощь по работе с ботом: 
    Пишите @pashcock и сразу присылайте скриншот, чем смогу помогу.
    
    '''
    await message.answer(text)


@rate_limit(limit=1)
@dp.message_handler()
async def helper(message: types.Message):
    text = '''<b>Такой команды нет</b>'''
    await message.answer(text)
    await message.delete()
