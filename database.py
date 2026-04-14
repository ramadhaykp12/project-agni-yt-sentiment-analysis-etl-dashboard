import sqlite3
import pandas as pd

DB_NAME = "project_agni.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT,
            clean_text TEXT,
            sentiment TEXT,
            extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def load_to_db(df):
    conn = sqlite3.connect(DB_NAME)
    # Append data baru tanpa menghapus data lama
    df.to_sql('comments', conn, if_exists='append', index=False)
    conn.close()

def fetch_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM comments ORDER BY extracted_at DESC", conn)
    conn.close()
    return df