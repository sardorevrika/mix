import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

# Logni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher obyektlarini yaratish
# 'YOUR_BOT_TOKEN' o'rniga @BotFather bergan tokenni qo'ying
bot = Bot(token='7685723172:AAEjVM4nP6zCVRh7H9dqy32Ts82Cu8q97_8')
dp = Dispatcher()

# Klaviaturani yaratish
def get_keyboard():
    buttons = [
        [KeyboardButton(text="👋 Salom")],
        [KeyboardButton(text="ℹ️ Ma'lumot")],
        [KeyboardButton(text="📞 Aloqa")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard

# /start buyrug'ini qayta ishlash
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply(
        "Assalomu alaykum! Men oddiy telegram botman.\nKlaviaturadan harakatni tanlang:",
        reply_markup=get_keyboard()
    )

# Matn xabarlarini qayta ishlash
@dp.message()
async def handle_text(message: types.Message):
    if message.text == "👋 Salom":
        await message.answer("Salom! Sizni ko'rishdan xursandman!")
    
    elif message.text == "ℹ️ Ma'lumot":
        await message.answer("Bu aiogram yordamida yaratilgan oddiy bot namunasi")
    
    elif message.text == "📞 Aloqa":
        await message.answer("Biz bilan bog'lanish: bestevrika@gmail.com || +998 99 500 00 95")
    
    else:
        await message.answer("Bu buyruqni tushunmayman. Iltimos, klaviaturadagi tugmalardan foydalaning.")

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())