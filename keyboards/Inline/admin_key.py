from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


key_promotion = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Второй канал', callback_data='second_channel')
        ],
        [
            InlineKeyboardButton(text='Статистика', callback_data='statistics'),
            InlineKeyboardButton(text='Рассылка', callback_data='mailing')
        ],
        [
            InlineKeyboardButton(text='Подпись', callback_data='word_caption')
        ],
        [
            InlineKeyboardButton(text='Доп сообщение', callback_data='blurb')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='start_return')
        ]
    ]
)

key_mailing = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Подготовить сообщение', callback_data='add_mail')
        ],
        [
            InlineKeyboardButton(text='Удалить сообщение', callback_data='del_mail')
        ],
        [
            InlineKeyboardButton(text='Выбрать категорию для рассылки', callback_data='begin_mail')
        ],
        [
            InlineKeyboardButton(text='Реклама', callback_data='promotion')
        ]
    ]
)


key_addKey_mail = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить кнопку', callback_data='add_key_mail')
        ],
        [
            InlineKeyboardButton(text='Сохранить', callback_data='save_mail')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='add_mail')
        ]
    ]
)


key_addKey_mail_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='add_key_back_mail')
        ]
    ]
)


key_conf_mailing = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Все', callback_data='all_mail'),
            InlineKeyboardButton(text='День', callback_data='today_mail')
        ],
        [
            InlineKeyboardButton(text='Неделя', callback_data='week_mail'),
            InlineKeyboardButton(text='Месяц', callback_data='month_mail')
        ],
        [
            InlineKeyboardButton(text='Рассылка', callback_data='mailing')
        ]
    ]
)

key_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Подтвердить', callback_data='confirm_mail')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='begin_mail')
        ]
    ]
)


key_sec_chn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить канал', callback_data='add_second_channel')
        ],
        [
            InlineKeyboardButton(text='Удалить канал', callback_data='del_second_channel')
        ],
        [
            InlineKeyboardButton(text='Реклама', callback_data='promotion')
        ]
    ]
)

key_add_second_channel_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='second_channel')
        ]
    ]
)