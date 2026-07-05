from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from user_service import get_current_user
from fastapi.staticfiles import StaticFiles

from ai_service import generate_sql
from db_service import execute_sql
from user_service import check_user
from user_service import get_user_role

from log_service import (
    save_query_log,
    get_query_logs,
    get_dashboard_stats,
    get_recent_queries
)


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str
    username: str

class LoginRequest(BaseModel):
    username: str

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/ask")
def ask_ai(data: AskRequest):

    question = data.question
    username = data.username

    role = get_user_role(username)

    print("使用者：", username)
    print("角色：", role)
    

    sql = generate_sql(question)

    if sql == "ERROR":
        return {
            "error": f"{role} 無權限查詢資料表：{table}"
        }

    sql_upper = sql.upper()
    role_permissions = {
        "Admin": [
            "Orders",
            "Products",
            "Customers",
            "OrderItems"
        ],
        "Sales": [
            "Orders",
            "Customers"
        ],
        "Purchase": [
            "Products",
            "OrderItems"
        ]
    }

    allowed_tables = role_permissions.get(role)

    if not allowed_tables:
        return {
            "error": "未知角色"
        }
    
    all_tables = [
        "Orders",
        "Products",
        "Customers",
        "OrderItems"
    ]
    

    sql_upper = sql.upper()

    for table in all_tables:

        if table.upper() in sql_upper:

            if table not in allowed_tables:

                return {
                    "error": f"無權限查詢資料表：{table}"
                }
    
    if sql == "ERROR":
        return {
            "error": "查無對應欄位或資料"
        }

    db_result = execute_sql(sql)
    save_query_log(question, sql)

    if "error" in db_result:
        return db_result

    return {
        "question": question,
        "sql": sql,
        "result": db_result["result"]
    }

@app.get("/logs")
def logs():

    return {
        "logs": get_query_logs()
    }

@app.get("/stats")
def stats():

    return get_dashboard_stats()

@app.get("/recent")
def recent():

    return {
        "recent": get_recent_queries()
    }


@app.get("/current-user")
def current_user():

    return get_current_user()

@app.get("/login")
def login_page():

    return FileResponse("static/login.html")

@app.post("/login")
def login(data: LoginRequest):

    user = check_user(data.username)

    if not user:
        return {
            "success": False,
            "message": "使用者不存在"
        }

    return {
        "success": True,
        "username": user[0],
        "role": user[1]
    }