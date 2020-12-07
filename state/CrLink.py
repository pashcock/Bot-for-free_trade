from aiogram.dispatcher.filters.state import StatesGroup, State


class CreatePost(StatesGroup):
    Q1 = State()


class EditPost(StatesGroup):
    E1 = State()
    E2 = State()


class BanPost(StatesGroup):
    B1 = State()



