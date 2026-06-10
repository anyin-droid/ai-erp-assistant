from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from ai_service import generate_sql
from db_service import execute_sql

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": "AI ERP Assistant API"
    }

@app.post("/ask")
def ask_ai(data: AskRequest):

    question = data.question

    sql = generate_sql(question)
    # 可查詢資料表白名單
    allowed_tables = [
        "Orders",
        "Products"
    ]

    # SQL 轉大寫方便比對
    sql_upper = sql.upper()

    # 檢查 SQL 是否包含禁止資料表
    blocked = False

    for table in ["Customers", "OrderItems"]:

        if table.upper() in sql_upper:
            blocked = True

    if blocked:
        return {
            "error": "無權限查詢此資料表"
        }
    if sql == "ERROR":
        return {
            "error": "查無對應欄位或資料"
        }

    db_result = execute_sql(sql)

    if "error" in db_result:
        return db_result

    return {
        "question": question,
        "sql": sql,
        "result": db_result["result"]
    }