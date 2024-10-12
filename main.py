from aiogram import Dispatcher, Bot
import asyncio
from app.handlers import router

from config import TOKEN

dp = Dispatcher()
bot = Bot(token=TOKEN)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
