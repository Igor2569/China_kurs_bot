from aiogram import Bot, Dispatcher, executor,types
from aiogram.dispatcher import FSMContext
from loader import dp,bot
import utils

def save_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


@dp.message_handler(state = utils.get_kurs.kurs)
async def Kurs(message:types.Message,state:FSMContext):
    f = open('data/textes/kurs.txt','w')
    f.write(message.text)
    f.close()
    await bot.send_message(chat_id=message.from_user.id,
                           text = 'Новый курс установлен')
    return

@dp.message_handler(state=utils.Settings.start_text)
async def process_start_text(message: types.Message, state: FSMContext):
    save_to_file('start_text.txt', message.text)
    await message.answer("Стартовый текст успешно изменен!")
    await state.finish()

@dp.message_handler(state=utils.Settings.guides)
async def process_guides(message: types.Message, state: FSMContext):
    save_to_file('guides.txt', message.text)
    await message.answer("Текст гайдов успешно изменен!")
    await state.finish()

@dp.message_handler(state=utils.Settings.questions)
async def process_questions(message: types.Message, state: FSMContext):
    save_to_file('data/textes/questions.txt', message.text)
    await message.answer("Текст частых вопросов успешно изменен!")
    await state.finish()

@dp.message_handler(state=utils.Settings.link)
async def process_link(message: types.Message, state: FSMContext):
    save_to_file('data/textes/reviews.txt', message.text)
    await message.answer("Ссылка с отзывами успешно изменена!")
    await state.finish()

@dp.message_handler(state=utils.Settings.user_id)
async def process_user_id(message: types.Message, state: FSMContext):
    save_to_file('data/textes/admins.txt', message.text)
    await message.answer("User_id заказчика успешно изменен!")
    await state.finish()

@dp.message_handler(state=utils.Settings.ambassador)
async def process_ambassador(message: types.Message, state: FSMContext):
    save_to_file('data/textes/ambassador.txt', message.text)
    await message.answer("Текст амбассадорства успешно изменен!")
    await state.finish()
@dp.message_handler(state = utils.Settings.group_id)
async def process_groupId(message:types.Message,state:FSMContext):
    save_to_file('data/textes/ambassador.txt', message.text)
    await message.answer("Айди канала с заявками установлен")
    await state.finish()

@dp.message_handler(state=utils.OrderForm.waiting_for_product_name)
async def process_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text
        data['user_id'] = message.from_user.id
        data['username'] = message.from_user.username
    
    await utils.OrderForm.next()
    await message.answer("📏 Введите размер товара:")

@dp.message_handler(state=utils.OrderForm.waiting_for_size)
async def process_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    
    await utils.OrderForm.next()
    await message.answer("📸 Отправьте фото товара:")


@dp.message_handler(content_types=['photo'], state=utils.OrderForm.waiting_for_photo)
async def process_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo_id'] = message.photo[-1].file_id
    
    await utils.OrderForm.next()
    await message.answer("🔗 Введите ссылку на товар:")


@dp.message_handler(state=utils.OrderForm.waiting_for_link)
async def process_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_link'] = message.text
    
    await utils.OrderForm.next()
    await message.answer("💰 Введите цену товара в юанях:")


@dp.message_handler(state=utils.OrderForm.waiting_for_price)
async def process_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        order_message = (
            "🚀 *НОВАЯ ЗАЯВКА!*\n\n"
            f"👤 *Клиент:* @{data['username']} (ID: {data['user_id']})\n"
            f"📦 *Товар:* {data['product_name']}\n"
            f"📏 *Размер:* {data['size']}\n"
            f"💰 *Цена:* {data['price']} ¥\n"
            f"🔗 *Ссылка:* {data['product_link']}\n\n"
            f"🆔 *ID заявки:* {message.message_id + 1}"
        )
        
        f = open('data/textes/group_id.txt','r')
        GROUP_ID = int(f.read())
        try:
            if 'photo_id' in data:
                await bot.send_photo(
                    chat_id=GROUP_ID,
                    photo=data['photo_id'],
                    caption=order_message,
                    parse_mode='Markdown'
                )
            else:
                await bot.send_message(
                    chat_id=GROUP_ID,
                    text=order_message,
                    parse_mode='Markdown'
                )
            
            await message.answer("✅ Ваша заявка успешно отправлена! С вами свяжутся в ближайшее время.")
            
        except Exception as e:
            await message.answer("❌ Произошла ошибка при отправке заявки. Попробуйте позже.")
            print(f"Error sending to group: {e}")
    
    await state.finish()