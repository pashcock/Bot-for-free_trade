from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


key_blurb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить сообщение', callback_data='add_blurb')
        ],
        [
            InlineKeyboardButton(text='Удалить сообщение', callback_data='del_blurb')
        ],
        [
            InlineKeyboardButton(text='Реклама', callback_data='promotion')
        ]
    ]
)

key_blurb_back_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='С превью', callback_data='preview_off'),
            InlineKeyboardButton(text='Markdown', callback_data='parse_h')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='blurb')
        ]
    ]
)

key_blurb_back_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Без превью', callback_data='preview_on'),
            InlineKeyboardButton(text='Markdown', callback_data='parse_h')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='blurb')
        ]
    ]
)

key_blurb_back_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='С превью', callback_data='preview_off'),
            InlineKeyboardButton(text='HTML', callback_data='parse_m')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='blurb')
        ]
    ]
)

key_blurb_back_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Без превью', callback_data='preview_on'),
            InlineKeyboardButton(text='HTML', callback_data='parse_m')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='blurb')
        ]
    ]
)

key_addKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить кнопку', callback_data='add_key_blurb')
        ],
        [
            InlineKeyboardButton(text='Сохранить', callback_data='save_blurb')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='add_blurb')
        ]
    ]
)

key_addKey_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='add_key_back')
        ]
    ]
)
