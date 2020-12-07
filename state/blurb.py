from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateBlurb(StatesGroup):
    Blurb1 = State()
    text = State()
    text_key = State()
    photo = State()
    photo_key = State()
    video = State()
    video_key = State()