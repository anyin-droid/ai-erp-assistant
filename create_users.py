import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    role TEXT
)
""")

cursor.execute("""
INSERT INTO Users(username, role)
VALUES
('Andy', 'Admin')
""")

conn.commit()
conn.close()

print("Users table created!")