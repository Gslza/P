import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from aiogram.utils.executor import start_polling
import g4f

# Token bot Telegram (ganti dengan token bot Anda)
TOKEN = "7608587541:AAHSBQt8GBw207r2AMPGlwiLooStHq6IoR8"

# Inisialisasi bot
bot = Bot(token=TOKEN)
router = Router()
dp = Dispatcher(storage=MemoryStorage())

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Handler untuk pesan teks
@router.message()
async def handle_message(message: Message):
    try:
        response = g4f.chatCompletion(
            messages=[{"role": "user", "content": message.text}],
            provider=g4f.Provider.You
        )
        await message.reply(response)
    except Exception as e:
        logging.error(f"Terjadi kesalahan: {e}")
        await message.reply("Maaf, terjadi kesalahan saat memproses permintaan Anda.")

# Menjalankan bot
if __name__ == "__main__":
    dp.include_router(router)
    start_polling(dp, skip_updates=True)
