from aiogram import types
from aiogram.types import InputFile
from loader import dp,bot,db
import keyboards
from data import config
@dp.callback_query_handler(lambda callback:callback.data=='next_video')
async def Next_video(callback:types.CallbackQuery):
    is_second = db.fetchone(f'SELECT is_second FROM users WHERE user_id = {callback.from_user.id}')[0]
    if is_second=='true':
        await callback.answer('2 часть курса будет доступна через неделю')
        return
    else:
        number = int(db.fetchone(f'SELECT number FROM users WHERE user_id = {callback.from_user.id}')[0])
        if number==34:
            await callback.answer('Ваш курс окончен')
            return
        if number==8:
            await bot.send_message(chat_id=callback.from_user.id,
                                   text = '''Привет! 👋Я рада, что ты снова здесь!
 Надеюсь, неделя самоанализа была 
полезной и помогла тебе лучше 
понять себя и свои цели. 
Теперь самое интересное — 
давай начнем применять полученные
 знания на практике! 🚀

Предлагаю тебе продолжить и узнать, 
как превратить свои осознания в
 конкретные действия. 
Я верю в тебя и знаю, 
что у тебя всё получится!
 Желаю вдохновения, энергии 
и смелости на пути к лучшей 
версии себя! 💖

Давай вместе сделаем эту 
неделю невероятной!
''')
        video_id = db.fetchone(f'SELECT video FROM videos WHERE number = {number+1}')[0]
        db.query(f"UPDATE users SET number = {number+1} WHERE user_id = {callback.from_user.id}")
        await bot.send_video(callback.from_user.id, video=video_id,
                             reply_markup=keyboards.next())
        if number==7:
            db.query(f"UPDATE users SET is_second = 'true' WHERE user_id = {callback.from_user.id}")
            print('tyt')
            await bot.send_document(
            chat_id=callback.from_user.id,
            document=InputFile('data/pdf/слайды курса ИТОГ.pdf'))
            await bot.send_photo(callback.from_user.id, photo=InputFile('./data/photos/9.jpg'),
                                 reply_markup=keyboards.next())
        if number==27:
            await bot.send_photo(callback.from_user.id, photo=InputFile('./data/photos/29.jpg'),
                                 reply_markup=keyboards.next())
            await bot.send_photo(callback.from_user.id, photo=InputFile('./data/photos/30.jpg'),
                                 reply_markup=keyboards.next())
        if number==28:
            await bot.send_photo(callback.from_user.id, photo=InputFile('./data/photos/29_2.png'),
                                 reply_markup=keyboards.next())
        if number==33:
            await bot.send_photo(callback.from_user.id, photo=InputFile('./data/photos/17.jpg'),
                                 reply_markup=keyboards.next())
            await bot.send_message(callback.from_user.id,
                                   text = '''Нужна поддержка ? 🌹
Напиши мне:
@Marina_lifeKouch''')
        

@dp.callback_query_handler(lambda callback:callback.data=='payment')
async def Payment(callback:types.CallbackQuery):
    await bot.send_invoice(chat_id=callback.from_user.id,
                               title = 'Курс',
                               description = 'Оплата курса',
                               payload='kurs',
                               provider_token=config.YOOTOKEN,
                               currency='RUB',
                               start_parameter='true',
                               prices=[{'label':'rub',
                                        'amount':2800000}],
                                need_email=True,
                                send_email_to_provider=True,
                                provider_data={
                                        "receipt": {
                                            "items": [
                                                {
                                                    "description": "Оплата курса",
                                                    "quantity": "1",
                                                    "amount": {
                                                        "value": "28000.00",  
                                                        "currency": "RUB"
                                                    },
                                                    "vat_code": "1",  
                                                }
                                                ]
                                        }
    })