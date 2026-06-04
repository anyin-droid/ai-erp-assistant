# db_service.py

import sqlite3

def execute_sql(sql):

    blocked_words = [
        "DELETE",
        "UPDATE",
        "INSERT",
        "DROP"
    ]

    for word in blocked_words:
        if word in sql.upper():
            return {
                "error": "危險 SQL 被阻擋"
            }

    conn = sqlite3.connect("orders.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    try:

        cursor.execute(sql)

        rows = cursor.fetchall()

        result = [dict(row) for row in rows]

        return {
            "result": result
        }

    except Exception as e:

        return {
            "error": str(e)
        }

    finally:

        conn.close()