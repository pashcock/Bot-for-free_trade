from aiogram import types
from aiogram.dispatcher import FSMContext

from data import config
from keyboards.Inline.admin_stat_key import key_stat, key_stat_link_back

from loader import bot, dp, r, db
from state import StatLink
from utils.rewriting import rewriting_for_stat


@dp.message_handler(state=StatLink.S1)
async def get_link(message: types.Message, state: FSMContext):
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
        col_vo = await db.select_col_vo(arg)
        text = 'Количество запросов: {}\nАргумент: {}'.format(col_vo, arg)
        await message.answer(text, reply_markup=key_stat_link_back)
        await state.finish()
    else:
        text = 'Аргумент: введен не вверно\n\nПовторите попытку'
        await message.answer(text, reply_markup=key_stat_link_back)


@dp.callback_query_handler(user_id=config.admins, text='statistics')
async def stats(call: types.CallbackQuery):
    await call.answer()
    text = '👥*Общая статистика* - показывает количествово активных пользователей в боте,' \
           ' количество пользователей отключивших бот, которое обновляется после каждой рассылки в боте,' \
           ' и количество полученных *Доп сообщений*, которое меняется, когда обновляется сообщение.\n\n' \
           '📜*Статистика ссылки* - можете посмотреть сколько раз посмотрели ссылку по аргументу\n\n' \
           '*Не рекомендуется часто проверять общую статистику, так как сбор статистики дает лишную нагрузку на сервер*'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                parse_mode='Markdown', reply_markup=key_stat)


@dp.callback_query_handler(user_id=config.admins, text='statistics', state=StatLink.S1)
async def stats(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    text = '👥*Общая статистика* - показывает количествово активных пользователей в боте,' \
           ' количество пользователей отключивших бот, которое обновляется после каждой рассылки в боте,' \
           ' и количество полученных *Доп сообщений*, которое меняется, когда обновляется сообщение.\n\n' \
           '📜*Статистика ссылки* - можете посмотреть сколько раз посмотрели ссылку по аргументу\n\n' \
           '*Не рекомендуется часто проверять общую статистику, так как сбор статистики дает лишную нагрузку на сервер*'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                parse_mode='Markdown', reply_markup=key_stat)


@dp.callback_query_handler(user_id=config.admins, text='all_stat')
async def all_stat(call: types.CallbackQuery):
    await call.answer()
    await rewriting_for_stat(0)
    blurb = await r.par_get()
    sum_link = await db.stat_link()
    day = await db.stat_day()
    week = await db.stat_week()
    month = await db.stat_month()
    stat_all = await db.stat_all()
    ban = await db.stat_ban()

    statistics = f'''📈*Статистика*
    
👤*Пользователи*
    
    Всего: {stat_all}
    Сегодня: {day}
    Неделя: {week}
    Месяц: {month}
    
    👨🏿‍🦼Остановили бота: {ban}
    \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_
    
    Всего запрошенных постов: {sum_link}
    Всего разосланных доп сообщений: {blurb}
    '''
    await bot.send_message(text=statistics, chat_id=call.message.chat.id, parse_mode='Markdown')
    text = '👥*Общая статистика* - показывает количествово активных пользователей в боте,' \
           ' количество пользователей отключивших бот, которое обновляется после каждой рассылки в боте,' \
           ' и количество полученных *Доп сообщений*, которое меняется, когда обновляется сообщение.\n\n' \
           '📜*Статистика ссылки* - можете посмотреть сколько раз посмотрели ссылку по аргументу\n\n' \
           '*Не рекомендуется часто проверять общую статистику, так как сбор статистики дает лишную нагрузку на сервер*'
    await bot.send_message(text=text, chat_id=call.message.chat.id, parse_mode='Markdown', reply_markup=key_stat)


@dp.callback_query_handler(user_id=config.admins, text='stat_link')
async def stat_link(call: types.CallbackQuery):
    await call.answer()
    text = '<b>Статистика ссылки</b>\n\n' \
           'Вы можете прислать аргумент<b>(start=аргумент)</b> или прислать саму ссылку с аргументом'
    await StatLink.S1.set()
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_stat_link_back)
