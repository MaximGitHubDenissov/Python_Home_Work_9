from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import csv

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот онлайн')
    

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/Меню_поиска')

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

kb_main_menu.add(b1).add(b2)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer('Телефонный справочник', reply_markup=kb_main_menu)

@dp.message_handler(commands=['Меню_поиска'])
async def search_start(message: types.Message):
    await message.answer('Введите имя или фамилию')
    

@dp.message_handler()
async def echo_send(message: types.Message):
    check = message.text
    data = []
    with open('data_base.csv', 'r') as f: 
        for line in f:
            if check in line: 
                data.append(line)
               
    await message.answer(''.join(data))  

    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)