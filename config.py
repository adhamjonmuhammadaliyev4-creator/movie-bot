# Bot konfiguratsiyasi
import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot API Token (BotFather dan oling)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Admin ID (o'zingizning Telegram ID ngizni yozing)
# @userinfobot dan o'zingizning ID ngizni bilib oling
ADMIN_IDS = [123456789]  # O'zingizning ID ni yozing

# Database
DATABASE_URL = "movies.db"

# Bot sozlamalari
CHANNEL_LINK = "https://t.me/your_channel"  # Majburiy obuna uchun kanal (ixtiyoriy)
REQUIRE_SUBSCRIPTION = False  # True qilsangiz, kanalga majburiy obuna qiladi
