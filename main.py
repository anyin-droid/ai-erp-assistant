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

    db_result = execute_sql(sql)

    if "error" in db_result:
        return db_result

    return {
        "question": question,
        "sql": sql,
        "result": db_result["result"]
    }