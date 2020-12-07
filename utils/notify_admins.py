import logging

from aiogram import Dispatcher

from data import config


async def on_startup_notify(dp: Dispatcher):
    for admin in config.admins:
        try:
            if admin == 349368261:
                await dp.bot.send_message(admin, "Бот Запущен\nНе забудь про /XXX")
            else:
                await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
