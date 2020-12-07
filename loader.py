from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data.config import BOT_TOKEN, ip

from utils.db_api.postgres import Database
from utils.redis.consts import RedisBase

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(host=ip)
dp = Dispatcher(bot=bot, storage=storage)
db = Database(loop=dp.loop)
r = RedisBase(loop=dp.loop)
