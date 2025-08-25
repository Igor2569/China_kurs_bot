from aiogram import types
from loader import dp,bot
import keyboards
from data import textes
from utils import get_kurs
@dp.message_handler(commands='start')
async def start(message:types.Message):
    f = open('data/textes/start.txt','r',encoding='utf-8')
    text = f.read()
    await bot.send_message(chat_id=message.from_user.id,
                           text = text,
                           reply_markup=keyboards.startKb())
    return
@dp.message_handler(commands='kurs')
async def Kurs(message:types.Message):
    f = open('data/textes/admins.txt','r',encoding='utf-8')
    admins = f.readlines()
    for admin in admins:
        if int(admin)==message.from_user.id:
            await bot.send_message(chat_id=message.from_user.id,text = 'Введите новый курс юаня в формате 11.67')
            get_kurs.kurs.set()
            return
    return

@dp.message_handler(commands='super_admin')
async def SuperPanel(message:types.Message):
    f = open('data/textes/superAdmins.txt','r',encoding='utf-8')
    sadmins = f.readlines()
    for admin in sadmins:
        print(int(admin))
        if int(admin)==message.from_user.id:
            
            await bot.send_message(chat_id=message.from_user.id,
                                   text = 'Приветствую тебя,суперадмин',
                                   reply_markup=keyboards.superPanel())