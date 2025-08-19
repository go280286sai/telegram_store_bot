import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()
import os

bot = Bot(token=os.getenv('BOT_TELEGRAM'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    return await bot.send_message("Hello World!")


@dp.message()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


async def main():
    await dp.start_polling(bot)
    print("Bot is running...")


if __name__ == '__main__':
    asyncio.run(main())
