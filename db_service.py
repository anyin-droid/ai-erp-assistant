# db_service.py

import sqlite3
from datetime import datetime
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

        error_message = str(e)

        # 欄位不存在
        if "no such column" in error_message:
            return {
                "error": "查無對應欄位，請確認資料表欄位名稱"
            }

        # 資料表不存在
        elif "no such table" in error_message:
            return {
                "error": "查無對應資料表"
            }

        # 其他錯誤
        return {
            "error": error_message
        }

    finally:

        conn.close()
        
def save_query_log(question, sql):

    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO QueryLogs
        (question, sql_text, created_at)
        VALUES (?, ?, ?)
    """, (
        question,
        sql,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()
