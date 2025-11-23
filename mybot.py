# mybot.py
import logging
import asyncio
import os
from telegram import Bot
from telegram.error import TelegramError

# تست نصب بودن requests
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("⚠️ requests not installed")

TOKEN = "8456671330:AAFQ0JD_Cf-UpGCEqVahCPGvq_RNdz1hsx4"
ADMIN_CHAT_ID = 100710165

GROUP_IDS = os.getenv('GROUP_IDS', '100710165')
GROUP_LIST = [int(x.strip()) for x in GROUP_IDS.split(',')]

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

def keep_alive():
    """تابع نگه داشتن ربات فعال"""
    if HAS_REQUESTS:
        try:
            requests.get("https://api.telegram.org", timeout=5)
            print("🫀 keep-alive executed")
        except:
            print("🫀 keep-alive failed")
    else:
        print("🫀 keep-alive skipped (no requests)")

async def send_advertisement():
    bot = Bot(token=TOKEN)
    
    for group_id in GROUP_LIST:
        try:
            await bot.send_message(chat_id=group_id, text=ADVERTISEMENT_TEXT)
            print(f"✅ پیام به {group_id} ارسال شد")
        except TelegramError as e:
            print(f"❌ خطا: {e}")

async def main():
    while True:
        # اجرای keep-alive
        keep_alive()
        
        print("🕒 شروع ارسال پیام...")
        await send_advertisement()
        print("⏳ منتظر ۲ ساعت...")
        await asyncio.sleep(2 * 60 * 60)  # ۲ ساعت

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("🤖 ربات مارکتینگ فعال شد...")
    asyncio.run(main())
