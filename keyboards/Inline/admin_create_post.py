from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_after_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сделать ссылку", callback_data='create_link')
        ],
        [
            InlineKeyboardButton(text='Реклама', callback_data='promotion')
        ]
    ]
)

key_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить ссылку', callback_data='add_link'),
            InlineKeyboardButton(text='Изменить ссылку', callback_data='edit_link'),
        ],
        [
            InlineKeyboardButton(text='Заблокировать ссылку', callback_data='block_link'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='start_return')
        ]
    ]
)

key_return_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='create_link')
        ]
    ]
)

key_after_create_post = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сделать ссылку", callback_data='create_link')
        ],
        [
            InlineKeyboardButton(text='Меню', callback_data='start_return')
        ]
    ]
)