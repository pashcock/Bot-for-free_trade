from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data import config
from loader import bot


class ChatMembers(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return 'member' == (await bot.get_chat_member(chat_id=config.channel, user_id=message.chat.id)).status
