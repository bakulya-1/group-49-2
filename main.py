from turtledemo.penrose import start

from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import logging
import os


token = config('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

Admins = [992671114, ]

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включён!')



@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello {message.from_user.first_name}!\n"
                                f"Твой telegram ID - {message.from_user.id}\n")

    await message.answer('Привет!')


@dp.message_handler(commands=['cat'])
async def cat_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')

#    photo = open(photo_path, 'rb')

    with open(photo_path, 'rb') as photo:

        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption='Это котик')

        await message.answer_photo(photo=photo, caption='Котик')


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

