import sqlite3

def get_current_user():

    conn = sqlite3.connect("orders.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT username, role
        FROM Users
        LIMIT 1
    """)

    user = cursor.fetchone()

    conn.close()

    return dict(user)

def check_user(username):

    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username, role
        FROM Users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user

def get_user_role(username):

    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role
        FROM Users
        WHERE username = ?
    """, (username,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None