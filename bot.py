import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Токен бота
API_TOKEN = "8746185237:AAHu0oguurkr_oK6_dM_Ge7KLJL3wKcvnf8"

# Створюємо бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Клавіатура
def main_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="🕒 Година")
    builder.button(text="🤓 Цікавий факт")
    builder.button(text="/start")
    builder.button(text="/help")

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)


# /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Я бот який повторює",
        reply_markup=main_keyboard()
    )


# /help
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Я бот який повторює твої повідомлення.\n\n"
        "Кнопки:\n"
        "🕒 Година — показує час по Києву\n"
        "🤓 Цікавий факт — випадковий факт",
        reply_markup=main_keyboard()
    )


# Година по Києву
@dp.message(lambda message: message.text == "🕒 Година")
async def time_handler(message: Message):
    kyiv_time = datetime.now(ZoneInfo("Europe/Kyiv"))
    current_time = kyiv_time.strftime("%H:%M:%S")

    await message.answer(
        f"🕒 Зараз у Києві: {current_time}"
    )


# Цікавий факт
@dp.message(lambda message: message.text == "🤓 Цікавий факт")
async def fact_handler(message: Message):
    await message.answer(
        "🐙 Восьминіг має 3 серця!"
    )


# Повторення повідомлень
@dp.message()
async def repeat_handler(message: Message):
    await message.answer(message.text)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())