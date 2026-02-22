# MovieCodeBot - Asosiy bot fayli
import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, ContentType, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.methods import DeleteMessage

# Lokal fayllar
from config import BOT_TOKEN, ADMIN_IDS, CHANNEL_LINK, REQUIRE_SUBSCRIPTION
from database import (
    init_db, add_user, get_user, update_language, 
    add_movie, get_movie, get_all_movies, delete_movie
)
from keyboards import (
    get_language_keyboard, get_main_menu_keyboard, 
    get_admin_keyboard, get_cancel_keyboard
)
from locales import get_text

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot va Dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

# Admin uchun holatlar (FSM)
class AdminStates(StatesGroup):
    waiting_for_movie = State()
    waiting_for_code = State()
    waiting_for_caption = State()

# Foydalanuvchi ma'lumotlari
user_states = {}  # user_id -> holat

# ============ YORDAMCHI FUNKSIYALAR ============

async def check_subscription(user_id: int) -> bool:
    """Foydalanuvchi kanalga obuna bo'lganini tekshirish"""
    if not REQUIRE_SUBSCRIPTION:
        return True
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_LINK, user_id=user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return True  # Xatolik bo'lsa, ruxsat berish

def get_user_lang(user_id: int) -> str:
    """Foydalanuvchi tilini olish"""
    user = get_user(user_id)
    return user['language'] if user else 'uz'

# ============ HANDLERS ============

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """Botga /start buyrug'i kelganda"""
    user_id = message.from_user.id
    username = message.from_user.username
    
    # Foydalanuvchini bazaga qo'shish
    add_user(user_id, username)
    
    # Tilni tekshirish
    user = get_user(user_id)
    if user and user['language']:
        lang = user['language']
        await message.answer(
            get_text('start', lang),
            reply_markup=get_main_menu_keyboard(lang)
        )
    else:
        # Yangi foydalanuvchi - tilni tanlash
        await message.answer(
            get_text('start_new', 'uz'),
            reply_markup=get_language_keyboard()
        )

@router.message(Command("lang"))
async def cmd_language(message: Message):
    """Tilni o'zgartirish"""
    await message.answer(
        get_text('select_language', get_user_lang(message.from_user.id)),
        reply_markup=get_language_keyboard()
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    """Yordam buyrug'i"""
    lang = get_user_lang(message.from_user.id)
    await message.answer(get_text('help', lang))

@router.message(Command("admin"))
async def cmd_admin(message: Message, state: FSMContext):
    """Admin panel"""
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        lang = get_user_lang(user_id)
        await message.answer(get_text('admin_only', lang))
        return
    
    lang = get_user_lang(user_id)
    await state.clear()
    await message.answer(
        get_text('admin_welcome', lang),
        reply_markup=get_admin_keyboard(lang)
    )

@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    """Bekor qilish"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    await state.clear()
    await message.answer(
        get_text('cancelled', lang),
        reply_markup=get_main_menu_keyboard(lang)
    )

@router.callback_query()
async def callback_language(callback: CallbackQuery, state: FSMContext):
    """Tilni tanlash callback"""
    user_id = callback.from_user.id
    data = callback.data
    
    if data.startswith('lang_'):
        lang = data.replace('lang_', '')
        update_language(user_id, lang)
        
        await callback.message.edit_text(
            get_text('language_changed', lang)
        )
        
        # Asosiy menyuni yuborish
        await bot.send_message(
            user_id,
            get_text('start', lang),
            reply_markup=get_main_menu_keyboard(lang)
        )
    
    elif data.startswith('delete_'):
        if user_id not in ADMIN_IDS:
            await callback.answer(get_text('admin_only', 'uz'), show_alert=True)
            return
        
        movie_id = int(data.replace('delete_', ''))
        delete_movie(movie_id)
        
        lang = get_user_lang(user_id)
        await callback.message.edit_text(get_text('deleted', lang))
    
    await callback.answer()

@router.message()
async def handle_messages(message: Message, state: FSMContext):
    """Barcha xabarlarni qayta ishlash"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    text = message.text
    
    # Obunani tekshirish
    if not await check_subscription(user_id):
        await message.answer(
            get_text('not_subscribed', lang) + f"\n\n{CHANNEL_LINK}"
        )
        return
    
    # Admin tekshiruvi
    if user_id in ADMIN_IDS:
        # Admin paneli
        if text == "👨‍💻 Admin panel" or text == "🎬 Yangi kino qo'shish" or "Добавить фильм" in text or "Add new movie" in text:
            lang = get_user_lang(user_id)
            await state.set_state(AdminStates.waiting_for_movie)
            await message.answer(
                get_text('send_movie', lang),
                reply_markup=get_cancel_keyboard(lang)
            )
            return
        
        elif text == "📋 Kinolar ro'yxati" or "Список фильмов" in text or "Movie list" in text:
            movies = get_all_movies()
            if not movies:
                await message.answer(get_text('no_movies', lang))
            else:
                msg = get_text('movies_list', lang)
                for m in movies[:10]:  # Oxirgi 10 ta
                    caption = m['caption'] if m['caption'] else "N/A"
                    msg += get_text('movie_item', lang, caption=caption, code=m['code'], downloads=m['downloads'])
                    msg += f"\n<button callback_data='delete_{m['id']}'>🗑️ O'chirish</button>\n\n"
                await message.answer(msg, parse_mode='HTML')
            return
        
        elif text == "📊 Statistika" or "Статистика" in text or "Statistics" in text:
            movies = get_all_movies()
            total_movies = len(movies)
            total_downloads = sum(m['downloads'] for m in movies)
            await message.answer(
                get_text('stats', lang, total_movies=total_movies, total_downloads=total_downloads)
            )
            return
        
        elif text == "◀️ Orqaga" or "◀️ Назад" in text or "◀️ Back" in text:
            await state.clear()
            await message.answer(
                get_text('start', lang),
                reply_markup=get_main_menu_keyboard(lang)
            )
            return
    
    # Admin kino qo'shish holatlari
    current_state = await state.get_state()
    
    if current_state == AdminStates.waiting_for_movie.state:
        # Kino video kelishi kerak
        if message.video:
            file_id = message.video.file_id
            file_size = message.video.file_size
            
            await state.update_data(file_id=file_id, file_size=file_size)
            await state.set_state(AdminStates.waiting_for_code)
            
            lang = get_user_lang(user_id)
            await message.answer(
                get_text('enter_code_for_movie', lang),
                reply_markup=get_cancel_keyboard(lang)
            )
        else:
            lang = get_user_lang(user_id)
            await message.answer(get_text('send_movie', lang))
        return
    
    elif current_state == AdminStates.waiting_for_code.state:
        # Kod kelishi kerak
        code = text.strip()
        
        if len(code) < 2:
            lang = get_user_lang(user_id)
            await message.answer("❌ Kod juda qisqa! Kamida 2 ta belgi.")
            return
        
        # Kod mavjudligini tekshirish
        existing = get_movie(code)
        if existing:
            lang = get_user_lang(user_id)
            await message.answer(get_text('movie_add_error', lang))
            return
        
        await state.update_data(code=code)
        await state.set_state(AdminStates.waiting_for_caption)
        
        lang = get_user_lang(user_id)
        await message.answer(
            get_text('enter_caption', lang),
            reply_markup=get_cancel_keyboard(lang)
        )
        return
    
    elif current_state == AdminStates.waiting_for_caption.state:
        # Tavsif kelishi kerak
        data = await state.get_data()
        file_id = data['file_id']
        code = data['code']
        caption = text if text != '-' else ""
        
        # Bazaga saqlash
        success = add_movie(code, file_id, caption)
        
        await state.clear()
        
        if success:
            lang = get_user_lang(user_id)
            await message.answer(
                get_text('movie_added', lang, code=code, caption=caption or "Yo'q"),
                reply_markup=get_admin_keyboard(lang)
            )
        else:
            lang = get_user_lang(user_id)
            await message.answer(
                get_text('movie_add_error', lang),
                reply_markup=get_admin_keyboard(lang)
            )
        return
    
    # Oddiy foydalanuvchi - kod qidirish
    # Tugmalarni tekshirish
    if text in ["📥 Kino yuklab olish", "📥 Скачать фильм", "📥 Download movie"]:
        await message.answer(get_text('enter_code', lang))
        return
    
    elif text in ["🌐 Tilni o'zgartirish", "🌐 Изменить язык", "🌐 Change language"]:
        await message.answer(
            get_text('select_language', lang),
            reply_markup=get_language_keyboard()
        )
        return
    
    elif text in ["❓ Yordam", "❓ Помощь", "❓ Help"]:
        await message.answer(get_text('help', lang))
        return
    
    # Kod qidirish
    # Faqat raqamlar yoki harflar bo'lsa
    if text and len(text.strip()) >= 2:
        movie = get_movie(text.strip())
        
        if movie:
            lang = get_user_lang(user_id)
            await message.answer(get_text('movie_found', lang))
            
            # Kinoni yuborish
            try:
                await bot.send_video(
                    chat_id=user_id,
                    video=movie['file_id'],
                    caption=movie['caption'] + f"\n\n{get_text('downloads_count', lang, count=movie['downloads'])}" if movie['caption'] else get_text('downloads_count', lang, count=movie['downloads'])
                )
            except Exception as e:
                logger.error(f"Video yuborishda xatolik: {e}")
                await message.answer(get_text('error', lang))
        else:
            await message.answer(get_text('movie_not_found', lang))
    else:
        # Noma'lum xabar
        await message.answer(get_text('enter_code', lang))

# ============ BOTNI ISHGA TUSHIRISH ============

async def main():
    """Botni ishga tushirish"""
    # Database ni ishga tushirish
    init_db()
    logger.info("Database ishga tushdi!")
    
    # Router ni qo'shish
    dp.include_router(router)
    
    # Botni ishga tushirish
    logger.info("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
