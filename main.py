from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import TOKEN_API
from keyboards import kb, ikb, rkb, kpb
from random import randint, choice
from others import HELP_TXT, arr_photoas

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('РАБОТАЕМ!')

random_photo = choice(list(arr_photoas.keys()))

async def random_photos(message: types.Message):
    global random_photo
    random_photo = choice(list(arr_photoas.keys()))
    await bot.send_photo(chat_id=message.chat.id, photo = random_photo, caption= arr_photoas[random_photo], reply_markup=ikb)

@dp.message_handler(Text(equals='Random photo'))
async def open_new_kb(message: types.Message):
    await message.answer(text = 'РАНДОМНАЯ ФОТКА', reply_markup=rkb)
    await random_photos(message)
    await message.delete()

@dp.message_handler(Text(equals='Назад'))
async def back_main_kb(message: types.Message):
    await message.answer(text = 'Ты вернуЛся в гЛАВНОЕ МЕНЮ'.lower(), reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer('Welcome to our Bot!!!', reply_markup=kb)
    await bot.send_sticker(chat_id=message.from_user.id, sticker= 'CAACAgEAAxkBAAIHlWSnzBMGyplf5xnluM4eaplpf7SCAAK0AgACtAoZRAIkX7S-piKVLwQ')
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.answer(text = HELP_TXT, parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_cmd(message: types.Message):
    await message.reply('ОПИСАНИЕ ЭТОГО АХУИТЕЛЬНОГО БОТА! 💋')

# @dp.message_handler(commands=['vote'])
# async def photos_cmd(message: types.Message):
#     await bot.send_photo(chat_id=message.from_user.id,
#                    photo= photos[0],
#                    caption= captions[0],
#                    )

@dp.message_handler(commands=['location'])
async def location_cmd(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude= randint(30, 50), longitude= randint(30, 50))
    await message.delete()

flag = 'null'


@dp.callback_query_handler()
async def vote_cmd(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == 'like':
        if flag == 'dislike' or flag == 'null':
            await callback.answer('Тебе пОнравиЛОСЬ'.lower())
            flag = 'like'
        else:
            await callback.answer('ВТОРОЙ РАЗ ГОЛОСОВАТЬ НЕЛЬЗЯ!'.lower())
    elif callback.data == 'dislike':
        if flag == 'like' or flag == 'null':
            await callback.answer('CОГЛАСЕН, ГАВНО!!!')
            flag = 'dislike'
        else:
            await callback.answer('ВТОРОЙ РАЗ ГОЛОСОВАТЬ НЕЛЬЗЯ!'.lower())
    elif callback.data == 'back':
        await callback.message.answer(text = 'Ты вернУЛСЯ В ГЛАВНОЕ МЕНЮ'.lower(), reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        random_photo = choice(list(filter(lambda x: x != random_photo, list(arr_photoas.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption= arr_photoas[random_photo]),
                                          reply_markup=ikb)
        flag = 'null'
        await callback.answer()



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)