import asyncio
from aiogram import Bot, Dispatcher

from functions import daily_message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    """har kungi xabar yuborish vazifasini boshlaydi va botni ishga tushiradi"""
    asyncio.create_task(daily_message(bot))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
