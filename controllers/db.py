import sqlite3
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_PATH


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM productos")
    if cursor.fetchone()[0] == 0:
        datos = [
            ("Laptop", 999.99, 15),
            ("Mouse inalambrico", 25.50, 120),
            ("Teclado mecanico", 75.00, 60),
            ("Monitor 24 pulgadas", 189.99, 30),
            ("Audifonos bluetooth", 45.00, 85),
        ]
        cursor.executemany(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", datos
        )
    conn.commit()
    conn.close()
