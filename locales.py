# Multilingual matnlar (tarjimalar)
translations = {
    'uz': {
        # Asosiy xabarlar
        'start': "🎬 Kino Kod Boti ga xush kelibsiz!\n\nBu bot orqali siz kinolarni kod orqali yuklab olishingiz mumkin.\n\nKino kodini yuboring:",
        'start_new': "🎬 Kino Kod Boti ga xush kelibsiz!\n\nTilni tanlang:",
        'help': "❓ Yordam\n\nBu bot orqali:\n1. Kino kodini yuboring\n2. Kino avtomatik yuklab tushadi\n\nMavjud tillar: O'zbek, Rus, Ingliz",
        'select_language': "🌐 Tilni tanlang:",
        'language_changed': "✅ Til o'zgartirildi!",
        
        # Kino yuklash
        'enter_code': "📥 Kino kodini yuboring:",
        'movie_not_found': "❌ Kino topilmadi!\n\nBoshqa kod urinib ko'ring yoki adminga bog'laning.",
        'movie_found': "🎬 Kino topildi!\n\nYuklanmoqda...",
        'downloads_count': "📊 Yuklab olishlar soni: {count}",
        
        # Admin xabarlari
        'admin_panel': "👨‍💻 Admin panel",
        'admin_welcome': "👨‍💻 Admin panelga xush kelibsiz!",
        'send_movie': "🎬 Kino yuboring:",
        'enter_code_for_movie': "📝 Endi bu kino uchun kod yozing:",
        'enter_caption': "📝 Kino tavsifini yozing (ixtiyoriy, bekor qilish uchun /cancel):",
        'movie_added': "✅ Kino muvaffaqiyatli qo'shildi!\n\nKod: {code}\nTavsif: {caption}",
        'movie_add_error': "❌ Xatolik! Bunday kod allaqachon mavjud.",
        'movie_add_cancelled': "❌ Kino qo'shish bekor qilindi.",
        'cancel': "❌ Bekor qilish",
        'cancelled': "❌ Bekor qilindi.",
        
        # Admin ro'yxat
        'movies_list': "📋 Kinolar ro'yxati:\n\n",
        'no_movies': "Hozircha kinolar yo'q.",
        'movie_item': "🎬 {caption}\nKod: <code>{code}</code>\nYuklab olishlar: {downloads}\n",
        'delete_movie': "🗑️ O'chirish",
        'confirm_delete': "Haqiqatan ham bu kinoni o'chirmoqchimisiz?",
        'deleted': "✅ Kino o'chirildi!",
        
        # Statistika
        'stats': "📊 Statistika:\n\nJami kinolar: {total_movies}\nJami yuklab olishlar: {total_downloads}",
        'total_downloads': "Jami yuklab olishlar: {count}",
        
        # Xatolar
        'error': "❌ Xatolik yuz berdi. Qayta urinib ko'ring.",
        'not_admin': "⚠️ Siz admin emassiz!",
        'admin_only': "⚠️ Bu funksiya faqat adminlar uchun!",
        
        # Majburiy obuna
        'subscribe': "📢 Botdan foydalanish uchun kanalga obuna bo'ling:",
        'not_subscribed': "❌ Siz kanalga obuna emassiz!",
        'subscribed': "✅ Obuna tasdiqlandi!"
    },
    
    'ru': {
        # Asosiy xabarlar
        'start': "🎬 Добро пожаловать в Бот Кодов Фильмов!\n\nС помощью этого бота вы можете скачивать фильмы по коду.\n\nОтправьте код фильма:",
        'start_new': "🎬 Добро пожаловать в Бот Кодов Фильмов!\n\nВыберите язык:",
        'help': "❓ Помощь\n\nС помощью этого бота:\n1. Отправьте код фильма\n2. Фильм автоматически загрузится\n\nДоступные языки: Узбекский, Русский, Английский",
        'select_language': "🌐 Выберите язык:",
        'language_changed': "✅ Язык изменён!",
        
        # Kino yuklash
        'enter_code': "📥 Отправьте код фильма:",
        'movie_not_found': "❌ Фильм не найден!\n\nПопробуйте другой код или свяжитесь с админом.",
        'movie_found': "🎬 Фильм найден!\n\nЗагрузка...",
        'downloads_count': "📊 Количество загрузок: {count}",
        
        # Admin xabarlari
        'admin_panel': "👨‍💻 Панель админа",
        'admin_welcome': "👨‍💻 Добро пожаловать в панель админа!",
        'send_movie': "🎬 Отправьте видео:",
        'enter_code_for_movie': "📝 Теперь введите код для этого фильма:",
        'enter_caption': "📝 Введите описание фильма (необязательно, /cancel для отмены):",
        'movie_added': "✅ Фильм успешно добавлен!\n\nКод: {code}\nОписание: {caption}",
        'movie_add_error': "❌ Ошибка! Такой код уже существует.",
        'movie_add_cancelled': "❌ Добавление фильма отменено.",
        'cancel': "❌ Отмена",
        'cancelled': "❌ Отменено.",
        
        # Admin ro'yxat
        'movies_list': "📋 Список фильмов:\n\n",
        'no_movies': "Пока нет фильмов.",
        'movie_item': "🎬 {caption}\nКод: <code>{code}</code>\nЗагрузок: {downloads}\n",
        'delete_movie': "🗑️ Удалить",
        'confirm_delete': "Вы уверены, что хотите удалить этот фильм?",
        'deleted': "✅ Фильм удалён!",
        
        # Statistika
        'stats': "📊 Статистика:\n\nВсего фильмов: {total_movies}\nВсего загрузок: {total_downloads}",
        'total_downloads': "Всего загрузок: {count}",
        
        # Xatolar
        'error': "❌ Произошла ошибка. Попробуйте снова.",
        'not_admin': "⚠️ Вы не админ!",
        'admin_only': "⚠️ Эта функция только для админов!",
        
        # Majburiy obuna
        'subscribe': "📢 Для использования бота подпишитесь на канал:",
        'not_subscribed': "❌ Вы не подписаны на канал!",
        'subscribed': "✅ Подтверждено!"
    },
    
    'en': {
        # Asosiy xabarlar
        'start': "🎬 Welcome to Movie Code Bot!\n\nWith this bot you can download movies by code.\n\nSend the movie code:",
        'start_new': "🎬 Welcome to Movie Code Bot!\n\nSelect language:",
        'help': "❓ Help\n\nWith this bot:\n1. Send the movie code\n2. Movie will download automatically\n\nAvailable languages: Uzbek, Russian, English",
        'select_language': "🌐 Select language:",
        'language_changed': "✅ Language changed!",
        
        # Kino yuklash
        'enter_code': "📥 Send the movie code:",
        'movie_not_found': "❌ Movie not found!\n\nTry another code or contact admin.",
        'movie_found': "🎬 Movie found!\n\nDownloading...",
        'downloads_count': "📊 Downloads: {count}",
        
        # Admin xabarlari
        'admin_panel': "👨‍💻 Admin panel",
        'admin_welcome': "👨‍💻 Welcome to admin panel!",
        'send_movie': "🎬 Send the video:",
        'enter_code_for_movie': "📝 Now enter the code for this movie:",
        'enter_caption': "📝 Enter movie description (optional, /cancel to cancel):",
        'movie_added': "✅ Movie added successfully!\n\nCode: {code}\nDescription: {caption}",
        'movie_add_error': "❌ Error! This code already exists.",
        'movie_add_cancelled': "❌ Movie addition cancelled.",
        'cancel': "❌ Cancel",
        'cancelled': "❌ Cancelled.",
        
        # Admin ro'yxat
        'movies_list': "📋 Movie list:\n\n",
        'no_movies': "No movies yet.",
        'movie_item': "🎬 {caption}\nCode: <code>{code}</code>\nDownloads: {downloads}\n",
        'delete_movie': "🗑️ Delete",
        'confirm_delete': "Are you sure you want to delete this movie?",
        'deleted': "✅ Movie deleted!",
        
        # Statistika
        'stats': "📊 Statistics:\n\nTotal movies: {total_movies}\nTotal downloads: {total_downloads}",
        'total_downloads': "Total downloads: {count}",
        
        # Xatolar
        'error': "❌ An error occurred. Try again.",
        'not_admin': "⚠️ You are not admin!",
        'admin_only': "⚠️ This function is only for admins!",
        
        # Majburiy obuna
        'subscribe': "📢 Subscribe to the channel to use the bot:",
        'not_subscribed': "❌ You are not subscribed to the channel!",
        'subscribed': "✅ Subscription confirmed!"
    }
}

def get_text(key: str, lang: str = 'uz', **kwargs) -> str:
    """Tarjima matnini olish"""
    text = translations.get(lang, translations['uz']).get(key, translations['uz'][key])
    if kwargs:
        text = text.format(**kwargs)
    return text
