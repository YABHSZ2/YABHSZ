import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from openai import OpenAI

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
API_KEY = os.environ.get("GEMINI_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
client = OpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("أهلا! أرسل لي أي سؤال")

@dp.message()
async def chat(message: Message):
    try:
        r = client.chat.completions.create(model="gemini-1.5-flash", messages=[{"role":"user","content": message.text}])
        await message.answer(r.choices[0].message.content)
    except Exception as e:
        await message.answer(f"حدث خطأ: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
