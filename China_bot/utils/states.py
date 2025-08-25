from aiogram.dispatcher.filters.state import StatesGroup, State

class get_kurs(StatesGroup):
    kurs = State()

class Settings(StatesGroup):
    start_text = State()
    guides = State()
    questions = State()
    link = State()
    user_id = State()
    ambassador = State()
    group_id = State()

class OrderForm(StatesGroup):
    waiting_for_product_name = State()
    waiting_for_size = State()
    waiting_for_photo = State()
    waiting_for_link = State()
    waiting_for_price = State()
