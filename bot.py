# Імпортуємо бібліотеки
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# Сюди вставляємо свій токен з BotFather
API_TOKEN = "8746185237:AAHu0oguurkr_oK6_dM_Ge7KLJL3wKcvnf8"

# Створюємо бота і диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Я бот який повторюю")

# Обробник усіх повідомлень
@dp.message()
async def repeat_handler(message: Message):
    await message.answer(message.text)

# Головна функція для запуску бота
async def main():
    await dp.start_polling(bot)

# Запускаємо
if __name__ == "__main__":
    asyncio.run(main())
