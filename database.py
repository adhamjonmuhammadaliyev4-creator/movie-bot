# Ma'lumotlar bazasi bilan ishlash
import sqlite3
from datetime import datetime
from config import DATABASE_URL

def init_db():
    """Database ni yaratish va jadvallarni sozlash"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Foydalanuvchilar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            language TEXT DEFAULT 'uz',
            joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Kinolar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            file_id TEXT NOT NULL,
            caption TEXT,
            file_size INTEGER DEFAULT 0,
            downloads INTEGER DEFAULT 0,
            added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

def add_user(user_id: int, username: str = None, language: str = 'uz'):
    """Yangi foydalanuvchi qo'shish"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, username, language)
        VALUES (?, ?, ?)
    """, (user_id, username, language))
    conn.commit()
    conn.close()

def get_user(user_id: int) -> dict:
    """Foydalanuvchi ma'lumotlarini olish"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, language, joined_date FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'user_id': row[0],
            'username': row[1],
            'language': row[2],
            'joined_date': row[3]
        }
    return None

def update_language(user_id: int, language: str):
    """Foydalanuvchi tilini o'zgartirish"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET language = ? WHERE user_id = ?", (language, user_id))
    conn.commit()
    conn.close()

def add_movie(code: str, file_id: str, caption: str = "", file_size: int = 0):
    """Yangi kino qo'shish"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO movies (code, file_id, caption, file_size)
            VALUES (?, ?, ?, ?)
        """, (code, file_id, caption, file_size))
        conn.commit()
        result = True
    except sqlite3.IntegrityError:
        result = False  # Kod allaqachon mavjud
    conn.close()
    return result

def get_movie(code: str) -> dict:
    """Kino ma'lumotlarini kod bo'yicha olish"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, code, file_id, caption, downloads 
        FROM movies WHERE code = ?
    """, (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        # Download sonini oshirish
        increment_downloads(row[0])
        return {
            'id': row[0],
            'code': row[1],
            'file_id': row[2],
            'caption': row[3],
            'downloads': row[4]
        }
    return None

def increment_downloads(movie_id: int):
    """Yuklab olishlar sonini oshirish"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET downloads = downloads + 1 WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()

def get_all_movies() -> list:
    """Barcha kinolar ro'yxatini olish (admin uchun)"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, code, caption, downloads, added_date 
        FROM movies ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            'id': row[0],
            'code': row[1],
            'caption': row[2],
            'downloads': row[3],
            'added_date': row[4]
        }
        for row in rows
    ]

def delete_movie(movie_id: int):
    """Kino o'chirish"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()

def search_movie_by_code(code: str) -> dict:
    """Kino qidirish (kodi bo'yicha)"""
    return get_movie(code)
