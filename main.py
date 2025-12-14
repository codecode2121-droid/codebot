import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("8566049755:AAHqZI3li5gVX_6JVyXO76bHOndgSWroDlY")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я твой бот.")

@dp.message_handler(commands=["hello"])
async def hello(message: types.Message):
    await message.answer("Hello, friend!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

