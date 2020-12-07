from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_stat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Общая статистика', callback_data='all_stat')
        ],
        [
            InlineKeyboardButton(text='Статистика ссылки', callback_data='stat_link')
        ],
        [
            InlineKeyboardButton(text='Реклама', callback_data='promotion')
        ]
    ]
)

key_stat_link_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='statistics')
        ]
    ]
)