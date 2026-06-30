# AI ERP Assistant

AI-powered ERP query assistant built with FastAPI, OpenAI API and SQLite.

Users can query ERP-style data using natural language, and the system automatically generates SQL queries through GPT-4.1-mini and returns database results.

---

## 🚀 Live Demo

👉 [AI ERP Assistant Demo](https://ai-erp-assistant-kfp9.onrender.com)

---

## Tech Stack

* Python
* FastAPI
* OpenAI API (GPT-4.1-mini)
* SQLite
* HTML / CSS / JavaScript
* REST API
* SQL JOIN / GROUP BY

---

## Features

* Natural language to SQL
* AI-generated SQL queries
* ERP-style relational database
* JOIN query support
* Frontend + Backend integration
* RESTful API
* Prompt Engineering for SQL generation

---

## Database Schema

Tables:

* Customers
* Orders
* Products
* OrderItems

Relationships:

* OrderItems.product_id -> Products.product_id
* OrderItems.order_id -> Orders.order_id

---

## Project Structure

ai-erp-assistant/

├── main.py
├── ai_service.py
├── db_service.py
├── index.html
├── orders.db
└── .env

---

## Installation

```bash
pip install -r requirements.txt
```

## Run Project

```bash
python -m uvicorn main:app --reload
```

## Example Query

User Input:

查詢訂單中的商品

Generated SQL:

```sql
SELECT
    oi.order_id,
    p.product_name,
    oi.quantity
FROM OrderItems oi
JOIN Products p
ON oi.product_id = p.product_id
```

## Future Improvements

* React frontend
* PostgreSQL / MSSQL support
* User authentication
* Docker deployment
* RAG-based schema retrieval
* Advanced SQL generation
