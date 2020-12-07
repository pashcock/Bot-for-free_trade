from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from keyboards.Inline.admin_create_post import key_after_start
from data import config
from loader import dp, db
from re import compile

from state import CreateBlurb, CreateCaption, CreatePost, EditPost, BanPost, CreateMail, ConfMail, SecChn, StatLink
from utils.rewriting import rewriting


@dp.message_handler(commands='help', user_id=config.admins)
async def helper(message: types.Message):
    text = '''<b>Тут тебе максимальная инструкция</b>

Я пока хз что тут писать - писать ли тебе разметку HTML ибо на неё я не ставил интерпритаторов и обработчиков.
Ошибок наделаешь что бот ахуеет.

Не упадет, но ахуеть ахуеет
    '''
    await message.answer(text)


@dp.message_handler(commands='XXX', user_id=349368261)
async def helper(message: types.Message):
    text = '''<b>Понеслась ебка сервера</b>'''
    await message.answer(text)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=compile(r"\w\d\w\d\w\d\w\d")), user_id=config.admins)
async def start_mess_deeplink(message: types.Message):
    arg = message.get_args()
    text = await db.select_text(arg)
    if len(config.caption) > 2:
        text += str('\n\n\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_'
                    '\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\n') + str(config.caption)
    await message.answer('{}'.format(text), parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins)
async def admin_menu(message: types.Message):
    text = '''<b>Смелее, мой юный друг!</b>
    
🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateBlurb.Blurb1)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateBlurb.text)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateBlurb.text_key)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateBlurb.photo)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateBlurb.photo_key)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateBlurb.video)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateBlurb.video_key)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateCaption.C1)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreatePost.Q1)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=EditPost.E1)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=EditPost.E2)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=BanPost.B1)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateMail.Mail)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateMail.text)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateMail.text_key)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateMail.photo)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateMail.photo_key)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateMail.video)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=CreateMail.video_key)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=ConfMail.All)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=ConfMail.Day)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=ConfMail.Week)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=ConfMail.Month)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=SecChn.Cr)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=SecChn.Wr)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()


@dp.message_handler(CommandStart(deep_link=None), user_id=config.admins, state=StatLink.S1)
async def admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = '''<b>Смелее, мой юный друг!</b>

🖊<b>Сделать ссылку</b> - работа со ссылками на скачивание постов
💰<b>Реклама</b> - всё, чтобы выжать больше бабла с рекламодателей
    '''
    await message.answer(text, reply_markup=key_after_start)
    await rewriting()
