
import os
import logging
from aiogram import Bot, Dispatcher, types 
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup   
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


API_TOKEN = os.environ.get("TG_BOT_TOKEN")
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.WARNING)


# States

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Let's start the party!)
    """
    chatid = []
    print(message.from_user.id)
    with open("chat_id.txt") as file:
        for item in file:
            print("f",item)
            chatid.append(item.replace("\n",""))
    file.close()
    print(chatid)
    if str(message.from_user.id) in chatid:
        await message.answer("Отлично! Теперь заказы будут приходить Вам в ЛС")
    else:
        await message.answer("Вы не добавлены в админ панель! Обратитесь к администратору")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)