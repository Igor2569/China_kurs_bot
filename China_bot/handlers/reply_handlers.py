from aiogram import types
from loader import dp,bot
from data import config
import utils
@dp.message_handler(lambda message:message.text=='Курс')
async def GetKurs(message:types.Message):
        f = open('data/textes/kurs.txt','r')
        kurs = f.read()
        f.close()
        await bot.send_message(chat_id=message.from_user.id,
                               text = f'Текущий курс {kurs} рублей = 1 юань.')
        return
@dp.message_handler(lambda message:message.text=='Идеи амбассадорства')
async def Ambassador(message:types.Message):
        f = open('data/textes/ambassador.txt','r')
        text = f.read()
        f.close()
        await bot.send_message(chat_id=message.from_user.id,
                               text = text)
        return


@dp.message_handler(lambda message: message.text == 'Изменить стартовый текст')
async def change_start_text(message: types.Message):
    await utils.Settings.start_text.set()
    await message.answer("Введите новый стартовый текст:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Изменить текст гайдов')
async def change_guides(message: types.Message):
    await utils.Settings.guides.set()
    await message.answer("Введите новый текст гайдов:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Изменить текст частых вопросов')
async def change_questions(message: types.Message):
    await utils.Settings.questions.set()
    await message.answer("Введите новый текст частых вопросов:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Изменить ссылку с отзывами')
async def change_link(message: types.Message):
    await utils.Settings.link.set()
    await message.answer("Введите новую ссылку с отзывами:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Изменить user_id заказчика')
async def change_user_id(message: types.Message):
    await utils.Settings.user_id.set()
    await message.answer("Введите новый user_id заказчика:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Изменить текст амбассадорства')
async def change_ambassador(message: types.Message):
    await utils.Settings.ambassador.set()
    await message.answer("Введите новый текст амбассадорства:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Изменить айди канала с заявками')
async def change_ambassador(message: types.Message):
    await utils.Settings.group_id.set()
    await message.answer("Введите айди канала для заявок", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Создать заказ')
async def start_order(message: types.Message):
    await utils.OrderForm.waiting_for_product_name.set()
    await message.answer("👕 Введите название товара (например: 'Кроссовки Nike Air Force'):", 
                         reply_markup=types.ReplyKeyboardRemove())

