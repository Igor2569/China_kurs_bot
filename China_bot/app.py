from aiogram import executor
from loader import dp,db
import handlers
import asyncio
import logging
from timer import Start_time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s')

def mains():
    executor.start_polling(dp)


if __name__ == '__main__':
    db.create_tables()
    loop = asyncio.get_event_loop()
    loop.create_task(Start_time())
    loop.create_task(mains())
    loop.run_forever()