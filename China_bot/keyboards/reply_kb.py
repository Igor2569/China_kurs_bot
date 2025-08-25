from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
def startKb():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    make = KeyboardButton(text = 'Создать заказ')
    kurs = KeyboardButton(text = 'Текущий курс юаня')
    guides = KeyboardButton(text = 'Гайды')
    questions = KeyboardButton(text = 'Частые вопросы')
    reviews = KeyboardButton(text = 'Отзывы')
    ambassador = KeyboardButton(text = 'Амбассадорство')
    keyboard.add(make)
    keyboard.add(kurs)
    keyboard.add(guides)
    keyboard.add(questions)
    keyboard.add(reviews)
    keyboard.add(ambassador)
    return keyboard

def superPanel():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    start_text = KeyboardButton(text = 'Изменить стартовый текст')
    guides = KeyboardButton(text = 'Изменить текст гайдов')
    questions = KeyboardButton(text = 'Изменить текст частых вопросов')
    link = KeyboardButton(text = 'Изменить ссылку с отзывами')
    user_id = KeyboardButton(text = 'Изменить user_id заказчика')
    ambassador = KeyboardButton(text = 'Изменить текст амбассадорства')
    group_id = KeyboardButton(text = 'Изменить айди канала с заявками')
    keyboard.add(start_text)
    keyboard.add(guides)
    keyboard.add(questions)
    keyboard.add(link)
    keyboard.add(user_id)
    keyboard.add(ambassador)
    keyboard.add(group_id)
    return keyboard