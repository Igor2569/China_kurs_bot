from aiogram import executor
from loader import dp,db,bot
from datetime import datetime
import pytz
import asyncio
import keyboards
async def Start_time():
    print('start')
    while True:
        time = datetime.now(pytz.timezone('Europe/Moscow'))
        print(time)
        if time.hour ==10 and time.minute==0:
            ids = db.fetchall('SELECT user_id FROM users WHERE user_id is not null')
            print(ids)
            for id in ids:
                id = id[0]
                is_second = db.fetchone(f'Select is_second FROM users WHERE user_id = {id}')[0]
                print(is_second)
                if is_second=='true':
                    days =  int(db.fetchone(f'Select days FROM users WHERE user_id = {id}')[0])
                    db.query(f"UPDATE users SET days = {days-1} WHERE user_id = {id}")
                    if days-1==0:
                        print("tyt")
                        db.query(f"UPDATE users SET is_second = 'false' WHERE user_id = {id}")
                        await bot.send_message(chat_id=id,
                                               text = '''Привет! Курс ждет тебя! 🌟 Пора продолжить обучение и двигаться к цели! 💪''',
                                               reply_markup=keyboards.next())
        await asyncio.sleep(60)