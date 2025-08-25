from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
def startKb():
    f = open('data/textes/reviews_url.txt','r')
    url = f.read()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    make = KeyboardButton(text = 'Создать заказ')
    kurs = KeyboardButton(text = 'Текущий курс юаня')
    guides = KeyboardButton(text = 'Гайды')
    questions = KeyboardButton(text = 'Частые вопросы')
    reviews = KeyboardButton(text = 'Отзывы',url = url)
    keyboard.add(make)
    keyboard.add(kurs)
    keyboard.add(guides)
    keyboard.add(questions)
    keyboard.add(reviews)
    return keyboard