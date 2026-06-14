import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS QueryLogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    sql_text TEXT,
    created_at TEXT
)
""")

conn.commit()
conn.close()

print("QueryLogs 建立成功")