import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import g4f

# Token bot Telegram (ganti dengan token bot Anda)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Inisialisasi bot dan dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Handler untuk pesan teks
@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        response = g4f.chatCompletion(
            messages=[{"role": "user", "content": message.text}],
            provider=g4f.Provider.You
        )
        await message.reply(response)
    except Exception as e:
        logging.error(f"Terjadi kesalahan: {e}")
        await message.reply("Maaf, terjadi kesalahan saat memproses permintaan Anda.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
