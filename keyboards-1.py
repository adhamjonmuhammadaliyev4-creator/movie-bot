# Inline keyboard va tugmalar
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_language_keyboard():
    """Tilni tanlash tugmalari"""
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="lang_uz"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")
    )
    return keyboard.as_markup()

def get_main_menu_keyboard(lang: str = 'uz'):
    """Asosiy meny"""
    textsu tugmalari = {
        'uz': {
            'download': "📥 Kino yuklab olish",
            'my_lang': "🌐 Tilni o'zgartirish",
            'help': "❓ Yordam"
        },
        'ru': {
            'download': "📥 Скачать фильм",
            'my_lang': "🌐 Изменить язык",
            'help': "❓ Помощь"
        },
        'en': {
            'download': "📥 Download movie",
            'my_lang': "🌐 Change language",
            'help': "❓ Help"
        }
    }
    
    t = texts.get(lang, texts['uz'])
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t['download'])],
            [KeyboardButton(text=t['my_lang']), KeyboardButton(text=t['help'])]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_admin_keyboard(lang: str = 'uz'):
    """Admin panel tugmalari"""
    texts = {
        'uz': {
            'add_movie': "🎬 Yangi kino qo'shish",
            'list_movies': "📋 Kinolar ro'yxati",
            'stats': "📊 Statistika",
            'back': "◀️ Orqaga"
        },
        'ru': {
            'add_movie': "🎬 Добавить фильм",
            'list_movies': "📋 Список фильмов",
            'stats': "📊 Статистика",
            'back': "◀️ Назад"
        },
        'en': {
            'add_movie': "🎬 Add new movie",
            'list_movies': "📋 Movie list",
            'stats': "📊 Statistics",
            'back': "◀️ Back"
        }
    }
    
    t = texts.get(lang, texts['uz'])
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t['add_movie'])],
            [KeyboardButton(text=t['list_movies']), KeyboardButton(text=t['stats'])],
            [KeyboardButton(text=t['back'])]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_cancel_keyboard(lang: str = 'uz'):
    """Bekor qilish tugmasi"""
    texts = {
        'uz': "❌ Bekor qilish",
        'ru': "❌ Отмена",
        'en': "❌ Cancel"
    }
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=texts.get(lang, texts['uz']))]],
        resize_keyboard=True
    )
    return keyboard
