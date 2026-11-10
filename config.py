"""VELOCITY SWAHILI - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY SWAHILI"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "SWAHILI"
HANDLE = "@velocityswahili"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "sw",
    "name": "Swahili",
    "native_name": "Kiswahili",
    "history_key": "swahili",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "sw-KE-RafikiNeural",
    "native_fallback_voice": "sw-KE-ZuriNeural",
    "native_engine": "edge",
    "native_lang_code": "sw",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "KISWAHILI",
    "translit_label": "SAY IT LIKE",
    "greeting": "Habari!",
    "encouragement": "Vizuri sana!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Salamu", "hand", "#1CB0F6"),
    ("Basic Phrases", "Misamiati ya Msingi", "chat", "#58CC02"),
    ("Common Expressions", "Maneno ya Kawaida", "chat", "#1CB0F6"),
    ("Travel", "Safari", "plane", "#1CB0F6"),
    ("Restaurant", "Mgahawa", "fork", "#FF7A00"),
    ("Shopping", "Ununuzi", "bag", "#E056A0"),
    ("Emergency", "Dharura", "siren", "#FF4B4B"),
    ("Family Terms", "Maneno ya Familia", "heart", "#E056A0"),
    ("Numbers", "Nambari", "hash", "#A560E8"),
    ("Time", "Wakati", "clock", "#00A889"),
    ("Motivation", "Motisha", "rocket", "#A560E8"),
    ("Love", "Upendo", "heart", "#FF4B4B"),
    ("Success", "Mafanikio", "trophy", "#F5A700"),
    ("Wisdom", "Hekima", "book", "#A560E8"),
    ("Happiness", "Furaha", "smile", "#F5A700"),
    ("Self Improvement", "Kujiboresha", "leaf", "#58CC02"),
    ("Gratitude", "Shukrani", "heart", "#FF7A00"),
    ("Friendship", "Urafiki", "users", "#00A889"),
    ("Hope", "Tumaini", "sun", "#FF7A00"),
    ("Creativity", "Ubunifu", "palette", "#E056A0"),
    ("Inner Peace", "Amani ya Ndani", "lotus", "#00A889"),
    ("Confidence", "Kujiamini", "shield", "#1CB0F6"),
    ("Perseverance", "Uvumilivu", "mountain", "#FF7A00"),
    ("Inspiration", "Msukumo", "sparkles", "#A560E8"),
    ("Positive Life", "Maisha Chanya", "sun", "#58CC02"),
    ("Courage", "Ujasiri", "shield", "#FF4B4B"),
    ("Kindness", "Wema", "heart", "#E056A0"),
    ("Patience", "Subira", "hourglass", "#00A889"),
    ("Forgiveness", "Msamaha", "hands", "#FF7A00"),
    ("Strength", "Nguvu", "dumbbell", "#FF4B4B"),
    ("Joy", "Shangwe", "smile", "#F5A700"),
    ("Balance", "Usawa", "scale", "#00A889"),
    ("Growth", "Ukuaji", "sprout", "#58CC02"),
    ("Purpose", "Kusudi", "target", "#A560E8"),
    ("Mindfulness", "Uangalifu", "lotus", "#00A889"),
    ("Daily Routine", "Utaratibu wa Kila Siku", "calendar", "#1CB0F6"),
    ("Weather", "Hali ya Hewa", "cloud", "#1CB0F6"),
    ("Feelings", "Hisia", "smile", "#E056A0"),
    ("Food", "Chakula", "fork", "#FF7A00"),
    ("Health", "Afya", "heart", "#58CC02"),
    ("Work", "Kazi", "briefcase", "#1CB0F6"),
    ("Technology", "Teknolojia", "chip", "#A560E8"),
    ("Nature", "Asili", "leaf", "#58CC02"),
    ("Animals", "Wanyama", "paw", "#FF7A00"),
    ("Colors", "Rangi", "palette", "#E056A0"),
    ("Directions", "Maelekezo", "compass", "#1CB0F6"),
    ("Body Parts", "Sehemu za Mwili", "hand", "#00A889"),
    ("Clothes", "Nguo", "shirt", "#E056A0"),
    ("Music", "Muziki", "music", "#A560E8"),
    ("Sports", "Michezo", "ball", "#FF7A00"),
    ("Holidays", "Likizo", "gift", "#FF4B4B"),
    ("Education", "Elimu", "book", "#1CB0F6"),
    ("Culture", "Utamaduni", "globe", "#00A889"),
    ("Finance", "Fedha", "coin", "#58CC02"),
    ("Relationships", "Mahusiano", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnswahili",
    "#swahililessons",
    "#swahiliforbeginners",
    "#languagelearning",
    "#swahilivocabulary",
    "#velocityswahili",
    "#dailyswahili",
    "#swahili",
    "#learnlanguages",
    "#speakswahili",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
