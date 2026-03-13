from datetime import datetime, timedelta
import os
import asyncio
from aiogram import Bot
from config import GROUP_ID


GROUP_ID = int(os.getenv("GROUP_ID"))


async def daily_message(bot: Bot):
    while True:
        now = datetime.now()

        target = now.replace(hour=11, minute=30, second=0, microsecond=0)

        if now >= target:
            target += timedelta(days=1)


        wait_time = (target - now).total_seconds()


        await asyncio.sleep(wait_time)


        await bot.send_message(GROUP_ID, "Salom hammaga")
