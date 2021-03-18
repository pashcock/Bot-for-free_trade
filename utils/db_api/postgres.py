import asyncio
import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                database='testdb',
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host=config.ip
            )
        )

    async def create_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS posts (
        link_post VARCHAR(12),
        text_post VARCHAR(1023),
        photo_post VARCHAR(1023),
        col_vo INTEGER,
        PRIMARY KEY(link_post)
        )'''
        await self.pool.execute(sql)

    async def write_post(self, text: str, random_text: str, photo: str):
        sql = 'INSERT INTO posts (link_post, text_post, photo_post, col_vo) ' \
              'VALUES (\'{}\', \'{}\', \'{}\', 0)'.format(random_text, text, photo)
        await self.pool.execute(sql)

    async def select_text(self, random_text: str):
        sql = 'SELECT text_post, photo_post FROM posts WHERE link_post=\'{}\''.format(random_text)
        return await self.pool.fetchrow(sql)

    async def update_post(self, text: str, random_text: str, photo: str):
        sql = 'UPDATE posts SET text_post=\'{}\', photo_post=\'{}\' WHERE link_post=\'{}\''.format(text,
                                                                                                   photo, random_text)
        await self.pool.execute(sql)

    async def ban_post(self, random_text: str):
        text = 'Данный курс заблокирован по обращению правообладателя'
        sql = 'UPDATE posts SET text_post=\'{}\', photo_post=\'\' WHERE link_post=\'{}\''.format(text, random_text)
        await self.pool.execute(sql)

    async def check_link(self, arg: str):
        sql = 'SELECT link_post FROM posts WHERE link_post =\'{}\''.format(arg)
        return True if await self.pool.fetchval(sql) is not None else False

    async def increment_link(self, arg: str):
        await self.pool.execute('UPDATE posts SET col_vo=col_vo+1 WHERE link_post=\'{}\''.format(arg))

    async def select_col_vo(self, arg: str):
        return await self.pool.fetchval('SELECT col_vo FROM posts WHERE link_post=\'{}\''.format(arg))

    async def create_const_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS const (
        id SMALLINT NOT NULL,
        video VARCHAR(255),
        photo VARCHAR(255),
        caption VARCHAR(1023),
        text VARCHAR(1023),
        parse VARCHAR(20),
        url_text VARCHAR(20),
        url_link VARCHAR(1024),
        notification SMALLINT,
        preview SMALLINT,
        PRIMARY KEY(id)
        )'''
        await self.pool.execute(sql)

    async def const_write(self):
        sql = '''INSERT INTO const (id, video, photo, caption, text, parse, url_text, url_link, notification, preview) 
        VALUES (1, \'\', \'\', \'\', \'\', \'\', \'\', \'\', 0, 0),
        (2, \'\', \'\', \'\', \'\', \'\', \'\', \'\', 0, 0),
        (3, \'\', \'\', \'\', \'\', \'\', \'\', \'\', 0, 0),
        (4, \'\', \'\', \'\', \'\', \'\', \'\', \'\', 0, 0)
        '''
        await self.pool.execute(sql)

    async def select_add_channel(self):
        sql = 'SELECT url_text, url_link FROM const WHERE id=4'
        data = await self.pool.fetchrow(sql)
        config.additional_channel = data[0]
        config.channel_link = data[1]

    async def update_add_channel(self):
        sql = f'UPDATE const SET url_text=\'{config.additional_channel}\', url_link=\'{config.channel_link}\''
        await self.pool.execute(sql)

    async def del_add_channel(self):
        sql = f'UPDATE const SET url_text=\'\', url_link=\'\''
        await self.pool.execute(sql)

    async def blurb_del(self):
        sql = 'UPDATE const SET video=\'\', photo=\'\', caption=\'\', text=\'\', parse=\'\', ' \
              'url_text=\'\', url_link=\'\', preview=0 WHERE id=1'
        await self.pool.execute(sql)

    async def update_blurb(self):
        sql = f'UPDATE const SET video=\'{config.video_blurb}\', photo=\'{config.photo_blurb}\', ' \
              f'caption=\'{config.caption_blurb}\', text=\'{config.text_blurb}\', parse=\'{config.parse_blurb}\', ' \
              f'url_text=\'{config.url_text_blurb}\', url_link=\'{config.url_link_blurb}\', ' \
              f'preview={config.preview_blurb} WHERE id=1'
        await self.pool.execute(sql)

    async def select_blurb(self):
        sql = 'SELECT video, photo, caption, text, parse, url_text, url_link, preview FROM const WHERE id=1'
        d = await self.pool.fetchrow(sql)
        if len(d[0]) > 2 or len(d[1]) > 2 or len(d[2]) > 2 or len(d[3]) > 2:
            config.video_blurb = d[0]
            config.photo_blurb = d[1]
            config.caption_blurb = d[2]
            config.text_blurb = d[3]
            config.parse_blurb = d[4]
            config.url_text_blurb = d[5]
            config.url_link_blurb = d[6]
            config.preview_blurb = d[7]
            config.save_blurb = 1

    async def mail_del(self):
        sql = 'UPDATE const SET video=\'\', photo=\'\', caption=\'\', text=\'\', parse=\'\', ' \
              'url_text=\'\', url_link=\'\', notification=0, preview=0 WHERE id=2'
        await self.pool.execute(sql)

    async def update_mail(self):
        sql = f'UPDATE const SET video=\'{config.video_mail}\', photo=\'{config.photo_mail}\', ' \
              f'caption=\'{config.caption_mail}\', text=\'{config.text_mail}\', parse=\'{config.parse_mail}\', ' \
              f'url_text=\'{config.url_text_mail}\', url_link=\'{config.url_link_mail}\', ' \
              f'notification={config.notification_mail}, preview={config.preview_mail} WHERE id=2'
        await self.pool.execute(sql)

    async def select_mail(self):
        sql = 'SELECT video, photo, caption, text, parse, url_text, url_link,notification,' \
              ' preview FROM const WHERE id=2'
        d = await self.pool.fetchrow(sql)
        if len(d[0]) > 2 or len(d[1]) > 2 or len(d[2]) > 2 or len(d[3]) > 2:
            config.video_mail = d[0]
            config.photo_mail = d[1]
            config.caption_mail = d[2]
            config.text_mail = d[3]
            config.parse_mail = d[4]
            config.url_text_mail = d[5]
            config.url_link_mail = d[6]
            config.notification_mail = d[7]
            config.preview_mail = d[8]
            config.save_mail = 1

    async def select_caption(self):
        sql = 'SELECT caption FROM const WHERE id=3'
        config.caption = await self.pool.fetchval(sql)

    async def update_caption(self):
        sql = f'UPDATE const SET caption =\'{config.caption}\' WHERE id=3'
        await self.pool.execute(sql)

    async def caption_del(self):
        sql = 'UPDATE const SET caption=\'\' WHERE id=3'
        await self.pool.execute(sql)

    async def create_table_user(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT,
        ban_bot SMALLINT,
        date_active DATE,
        date_create DATE,
        mes_mail INTEGER,
        PRIMARY KEY(user_id)
        )'''
        await self.pool.execute(sql)

    async def write_user(self, user_id: int):
        sql = 'INSERT INTO users (user_id, ban_bot, date_active, date_create, mes_mail)' \
              ' VALUES ({}, 0, CURRENT_DATE, CURRENT_DATE, 0)'.format(user_id)
        await self.pool.execute(sql)

    async def update_user(self, user_id: int):
        sql = 'UPDATE users SET ban_bot=0, date_active=CURRENT_DATE ' \
              'WHERE user_id={}'.format(user_id)
        await self.pool.execute(sql)

    async def stat_all(self):
        sql = 'SELECT COUNT(*) FROM users'
        return await self.pool.fetchval(sql)

    async def stat_ban(self):
        sql = 'SELECT COUNT(*) FROM users WHERE ban_bot=1'
        return await self.pool.fetchval(sql)

    async def stat_day(self):
        sql = 'SELECT COUNT(*) FROM users WHERE date_active=CURRENT_DATE'
        return await self.pool.fetchval(sql)

    async def stat_week(self):
        sql = 'SELECT COUNT(*) FROM users WHERE date_active>CURRENT_DATE - interval \'7 day\''
        return await self.pool.fetchval(sql)

    async def stat_month(self):
        sql = 'SELECT COUNT(*) FROM users WHERE date_active>CURRENT_DATE - interval \'1 month\''
        return await self.pool.fetchval(sql)

    async def stat_link(self):
        sql = 'SELECT SUM(col_vo) FROM posts'
        return await self.pool.fetchval(sql)

    async def mail_all(self):
        sql = 'SELECT user_id FROM users WHERE ban_bot=0'
        return await self.pool.fetch(sql)

    async def mail_day(self):
        sql = 'SELECT user_id FROM users WHERE (date_active=CURRENT_DATE and ban_bot=0)'
        return await self.pool.fetch(sql)

    async def mail_week(self):
        sql = 'SELECT user_id FROM users WHERE (date_active>CURRENT_DATE - interval \'7 day\' and ban_bot=0)'
        return await self.pool.fetch(sql)

    async def mail_month(self):
        sql = 'SELECT user_id FROM users WHERE (date_active>CURRENT_DATE - interval \'1 month\' and ban_bot=0)'
        return await self.pool.fetch(sql)

    async def ban_user(self, arg: int):
        sql = 'UPDATE users SET ban_bot=1 WHERE user_id={}'.format(arg)
        await self.pool.execute(sql)

    async def mail_write_mes(self, user_id: int, mes_id: int):
        sql = f'UPDATE users SET mes_mail={mes_id} WHERE user_id={user_id}'
        await self.pool.execute(sql)

    async def select_mes_mail(self):
        sql = 'SELECT user_id, mes_mail FROM users WHERE mes_mail>0'
        return await self.pool.fetch(sql)