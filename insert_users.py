import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO Users(username, role)
VALUES
('Amy','Sales'),
('John','Purchase')
""")

conn.commit()
conn.close()

print("Users inserted!")