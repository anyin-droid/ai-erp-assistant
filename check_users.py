import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM Users
""")

for row in cursor.fetchall():
    print(row)

conn.close()