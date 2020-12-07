import asyncio

from utils.set_bot_commands import set_default_commands
from loader import db


async def on_startup(dp):
    await asyncio.sleep(10)
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)
    await db.create_table()
    await db.create_const_table()
    await db.create_table_user()
    try:
        await db.write_post('Тестовый текст', '11111111')
    except:
        pass
    try:
        await db.const_write()
    except:
        pass
    await db.select_caption()
    await db.select_blurb()
    await db.select_mail()
    await db.select_add_channel()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

