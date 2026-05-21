import sqlite3

conn = sqlite3.connect("banco.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")

conn.commit