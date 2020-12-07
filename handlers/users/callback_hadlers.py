from aiogram.types import CallbackQuery

from data import config
from keyboards.Inline.admin_key import key_promotion
from loader import dp, bot


@dp.callback_query_handler(text='promotion', user_id=config.admins)
async def call_add_link(call: CallbackQuery):
    await call.answer()
    text = '''<b>Реклама и статистика</b>
    
🕸<b>Второй канал</b> - добавить второй обязательный для подписки канал, чтобы у пользователей сильнее подгорало очко
📊<b>Статистика</b> - статистика по пользователям и постам
📩<b>Рассылка</b> - опять же чтобы у людей пылало очко
📝<b>Подпись</b> - подпись на сообщении, причина в рассылке
🖇<b>Доп сообщение</b> - оформление дополнительного сообщения с рекламой, причина см п.3
    '''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=key_promotion)
