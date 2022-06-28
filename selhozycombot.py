import logging
from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



logging.basicConfig(level=logging.INFO)

API_TOKEN = '5332040921:AAEB2eMvWi3vi2yIxkoJlPI8mqjuKk9G8JY'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

agro = 0
asoc = 0
cagro = 100
csoc = 100
wagro = "False"
wsoc = "False"


@dp.message_handler(commands = ["start"])
async def start(message: types.Message):
    await message.answer("Список команд:        /info - подробная информация для вас,        /contacts - выдает контакты,         /start - начать с начала.      Скоро(когда-нибудь) будет добавлено больше команд.")

@dp.message_handler(commands = ["info"])
async def info(message: types.Message):
    await message.answer("Количество Поливальных машин и коммунального оборудования:" + str(agro)+ ", " +str(asoc)+ ",         Состояние Поливальных машин и коммунального оборудования:"+ str(cagro)+ ", "+ str(csoc)+ ",        Режим .В работе. у Поливальных машин и коммунального оборудования:"+ str(wagro)+ ", "+ str(wsoc))

@dp.message_handler(commands = ["contacts"])
async def contacts(message: types.Message):
    await message.answer("example@gmail.com")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
