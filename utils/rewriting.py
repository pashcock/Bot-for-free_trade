import asyncio

from loader import r, db, bot


async def rewriting_for_stat(del_us):
    keys = await r.scan_users()
    try:
        for key in keys:
            id = key.split(':')[1]
            try:
                await db.write_user(id)
            except:
                await db.update_user(id)
            finally:
                if del_us == 1:
                    await r.del_users(id)
    except Exception as e:
        await bot.send_message(349368261, f"Ошибка перезаписи случилась\n\n{e}")


async def rewriting():
    while True:
        await asyncio.sleep(43200)
        keys = await r.scan_users()
        try:
            for key in keys:
                id = key.split(':')[1]
                try:
                    await db.write_user(id)
                except:
                    await db.update_user(id)
        except Exception as e:
            await bot.send_message(349368261, f"Ошибка перезаписи случилась\n\n{e}")
