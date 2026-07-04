import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM Users
WHERE id = 2
""")

conn.commit()
conn.close()

print("Delete success!")