from aiogram.dispatcher.filters.state import StatesGroup, State


class ConfMail(StatesGroup):
    All = State()
    Day = State()
    Week = State()
    Month = State()