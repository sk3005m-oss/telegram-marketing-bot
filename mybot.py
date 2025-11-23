# marketing_bot.py
import logging
import asyncio
from telegram import Bot
from telegram.error import TelegramError

TOKEN = "8456671330:AAFQ0JD_Cf-UpGCEqVahCPGvq_RNdz1hsx4"
ADMIN_CHAT_ID = 100710165

ADVERTISEMENT_TEXT = """ربات فروشگاهی حرفه ای

ما ربات فروشگاهی با قابلیت های زیر می سازیم:

• پنل مدیریت
• ثبت سفارش
• مدیریت محصولات
• گزارش گیری فروش
• سیستم کد تخفیف

دریافت دمو رایگان:
@robaticashop_bot

قیمت: ۱٫۵ میلیون تومان"""

GROUP_LIST = [100710165]

async def send_advertisement():
    bot = Bot(token=TOKEN)
    
    for group_id in GROUP_LIST:
        try:
            await bot.send_message(chat_id=group_id, text=ADVERTISEMENT_TEXT)
            print(f"✅ پیام به {group_id} ارسال شد")
            return
        except TelegramError as e:
            print(f"❌ خطا: {e}")
    
    try:
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text="✅ ربات فعال است")
        print("📨 گزارش به ادمین ارسال شد")
    except Exception as e:
        print(f"❌ خطا در ارسال گزارش: {e}")

async def main():
    while True:
        print("🕒 شروع ارسال پیام...")
        await send_advertisement()
        print("⏳ منتظر ۲ ساعت...")
        await asyncio.sleep(2 * 60 * 60)  # 🎯 حالا ۲ ساعت

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("🤖 ربات مارکتینگ فعال شد...")
    print("⏰ هر ۲ ساعت پیام ارسال میشه")
    asyncio.run(main())