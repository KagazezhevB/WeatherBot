from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from openweather_api import get_weather

from configure import TOKEN_TELEGRAM

bot = Bot(token=TOKEN_TELEGRAM)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!")


@dp.message_handler()
async def request_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, get_weather(msg.text))


if __name__ == '__main__':
    executor.start_polling(dp)
