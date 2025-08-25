from aiogram import executor
from loader import dp
import handlers
import asyncio
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s')

def mains():
    executor.start_polling(dp)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(mains())
    loop.run_forever()