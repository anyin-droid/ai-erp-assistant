# ai_service.py

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_sql(question):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
你是一位 SQLite SQL 專家。

資料表如下：

Table: Orders

Columns:
- order_id
- customer_name
- amount
- status
- order_date


Table: Customers

Columns:
- customer_id
- customer_name


Table: Products

Columns:
- product_id
- product_name
- price


Table: OrderItems

Columns:
- id
- order_id
- product_id
- quantity


Relationships:

OrderItems.product_id
-> Products.product_id

OrderItems.order_id
-> Orders.order_id


請根據使用者需求產生 SQL。

規則：

1. 只能使用 SELECT
2. 不可使用 DELETE、UPDATE、INSERT、DROP
3. 只回傳 SQL
4. 不要 markdown
5. 優先使用 JOIN 語法
6. 查詢商品名稱時請 JOIN Products
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content.strip()