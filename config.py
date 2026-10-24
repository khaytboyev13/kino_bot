import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# SUPERADMIN_ID bo'sh yoki yo'q bo'lsa xatolik bermasligi uchun tekshiruv qo'shildi
_superadmin = os.getenv("SUPERADMIN_ID")
SUPERADMIN_ID = int(_superadmin) if _superadmin and _superadmin.strip() else 0

DB_PATH = "database.db"
RATE_LIMIT = 2
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")