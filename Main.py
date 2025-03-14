import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("سلام! برای دریافت لینک V2Ray رایگان، دستور /get_v2ray رو بفرست.")

@dp.message_handler(commands=['get_v2ray'])
async def send_v2ray_link(message: types.Message):
    try:
        response = requests.get("https://raw.githubusercontent.com/mahdibland/V2RayAggregator/main/sub/splitted/iran.txt")
        if response.status_code == 200:
            links = response.text.split("\n")[:5]
            await message.reply("\n".join(links))
        else:
            await message.reply("متاسفم، نتونستم لینک‌ها رو بگیرم. لطفاً بعداً امتحان کن!")
    except Exception as e:
        await message.reply("مشکلی پیش اومد، لطفاً بعداً امتحان کن!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
