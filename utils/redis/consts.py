import asyncio

import aioredis

from data import config


class RedisBase:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            aioredis.create_pool(**config.redis, db=1)
        )

    async def write_user(self, chat_id):
        await self.pool.execute(b'SET', f'user:{chat_id}', 0, b'EX', 86400, b'NX')

    async def get_user(self, chat_id):
        return await self.pool.execute(b'GET', f'user:{chat_id}')

    async def increment_user(self, chat_id):
        await self.pool.execute(b'SET', f'user:{chat_id}', 1, b'EX', 86400, b'XX')

    async def del_users(self, id):
        await self.pool.execute(b'DEL', f'user:{id}')

    async def param_blurb(self):
        await self.pool.execute(b'SET', f'par:blurb', 0)

    async def par_increment(self):
        await self.pool.execute(b'INCR', f'par:blurb')

    async def par_get(self):
        return await self.pool.execute(b'GET', f'par:blurb')

    async def scan_users(self):
        return await self.pool.execute(b'KEYS', 'user:*')

    async def param_mail(self):
        await self.pool.execute(b'SET', f'par:mail', 0)

    async def mail_increment(self):
        await self.pool.execute(b'INCR', f'par:mail')

    async def mail_get(self):
        return await self.pool.execute(b'GET', f'par:mail')

