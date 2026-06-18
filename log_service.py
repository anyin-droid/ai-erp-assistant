import sqlite3
from datetime import datetime

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

def get_query_logs():

    conn = sqlite3.connect("orders.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM QueryLogs
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    result = [dict(row) for row in rows]

    conn.close()

    return result

def get_dashboard_stats():

    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    # 總查詢次數
    cursor.execute("""
        SELECT COUNT(*)
        FROM QueryLogs
    """)
    total_queries = cursor.fetchone()[0]

    # 最近查詢
    cursor.execute("""
        SELECT question
        FROM QueryLogs
        ORDER BY id DESC
        LIMIT 1
    """)
    latest = cursor.fetchone()

    latest_question = latest[0] if latest else "無資料"

    conn.close()

    return {
        "total_queries": total_queries,
        "latest_question": latest_question
    }