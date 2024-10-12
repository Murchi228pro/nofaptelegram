from aiogram import Dispatcher, Bot
from aiogram.types import Message
import asyncio
from aiogram.filters import CommandStart

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart)
async def start(message: Message):
    await message.reply(f"Hello))))")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
