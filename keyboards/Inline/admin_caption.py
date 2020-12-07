from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_caption = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Изменить подпись', callback_data='change_caption')
        ],
        [
            InlineKeyboardButton(text='Удалить подпись', callback_data='del_caption')
        ],
        [
            InlineKeyboardButton(text='Реклама', callback_data='promotion')
        ]
    ]
)

key_caption_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='word_caption')
        ]
    ]
)
