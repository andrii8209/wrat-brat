import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Токен бота
API_TOKEN = "8746185237:AAHu0oguurkr_oK6_dM_Ge7KLJL3wKcvnf8"

# Створюємо бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Клавіатура з кнопками
def main_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="🕒 Година")
    builder.button(text="🤓 Цікавий факт")
    builder.button(text="/start")
    builder.button(text="/help")

    builder.adjust(2)

    return builder.as_markup(
        resize_keyboard=True
    )


# Команда /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Я бот який повторює",
        reply_markup=main_keyboard()
    )


# Команда /help
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Я бот який повторює твої повідомлення.\n\n"
        "Кнопки:\n"
        "🕒 Година — показує час\n"
        "🤓 Цікавий факт — випадковий факт",
        reply_markup=main_keyboard()
    )


# Кнопка "Година"
@dp.message(lambda message: message.text == "🕒 Година")
async def time_handler(message: Message):
    current_time = datetime.now().strftime("%H:%M:%S")

    await message.answer(
        f"Зараз година: {current_time}"
    )


# Кнопка "Цікавий факт"
@dp.message(lambda message: message.text == "🤓 Цікавий факт")
async def fact_handler(message: Message):
    fact = (
        "Восьминіг має 3 серця 🐙"
    )

    await message.answer(fact)


# Повторює всі повідомлення
@dp.message()
async def repeat_handler(message: Message):
    await message.answer(message.text)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())