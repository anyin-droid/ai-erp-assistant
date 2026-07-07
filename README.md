# AI ERP Assistant

An AI-powered ERP query assistant that converts natural language into SQL using **OpenAI GPT-4.1-mini**.

This project simulates a real-world ERP query workflow. Users enter questions in natural language, and the system automatically generates SQL, executes the query, and returns formatted results.

---

## 🚀 Live Demo

👉 https://ai-erp-assistant-kfp9.onrender.com

---

## 📷 Project Preview

<img width="1190" height="876" alt="螢幕擷取畫面 2026-07-07 210731" src="https://github.com/user-attachments/assets/eff3e4ba-5f88-4a98-a506-1c8e84f81a62" />
<img width="1345" height="874" alt="螢幕擷取畫面 2026-07-07 210740" src="https://github.com/user-attachments/assets/c7ea8c2c-6ad4-4cd7-98e4-9f817cd57e61" />

---

## ✨ Features

- 🤖 Natural Language → SQL
- 🧠 Prompt Engineering with Database Schema
- 🔍 AI-generated SQL Queries
- 📊 ERP-style Relational Database
- 🔗 Multi-table JOIN Queries
- 📈 GROUP BY / SUM Aggregate Queries
- 📝 Query History
- 🌐 RESTful API
- 💻 Frontend + Backend Integration

---

# 🏗 Tech Stack

### Backend

- Python
- FastAPI
- OpenAI API (GPT-4.1-mini)

### Database

- SQLite
- SQL
- JOIN
- GROUP BY
- Aggregate Functions

### Frontend

- HTML
- CSS
- JavaScript

### Deployment

- Render
- Git
- GitHub

---

# 🏛 System Architecture

```
                 User
                   │
                   ▼
        HTML / CSS / JavaScript
                   │
                   ▼
              FastAPI API
                   │
                   ▼
        Prompt Engineering
      (Inject Database Schema)
                   │
                   ▼
        OpenAI GPT-4.1-mini
                   │
                   ▼
          AI Generated SQL
                   │
                   ▼
            SQLite Database
                   │
                   ▼
          Query Result (JSON)
                   │
                   ▼
              Frontend UI
```

---

# 🗄 Database Schema

This project uses four ERP-style relational tables.

| Table | Description |
|------|-------------|
| Customers | Customer Information |
| Orders | Order Records |
| Products | Product Information |
| OrderItems | Order Details |

Relationship

```
Customers
     │
     │
 Orders
     │
     │
OrderItems
     │
     │
 Products
```

---

# 📂 Project Structure

```text
ai-erp-assistant/
│
├── main.py                  # FastAPI main application
├── ai_service.py             # OpenAI API and SQL generation logic
├── db_service.py             # Database connection and query execution
├── user_service.py           # User-related service logic
├── log_service.py            # Query log service
├── current_user.py           # Current user / role handling
│
├── static/
│   ├── index.html            # Main AI ERP query page
│   └── login.html            # Login page
│
├── orders.db                 # SQLite database
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .env                      # Environment variables
├── .gitignore
│
├── create_users.py           # Script to create users
├── insert_users.py           # Script to insert user data
├── create_querylogs.py       # Script to create query log table
├── check_users.py            # Script to check user data
├── check_querylogs.py        # Script to check query logs
├── check_logs.py             # Script to check logs
└── delete_user.py            # Script to delete user data

## Demo Accounts

| Username |   Role    |
|----------|-----------|
| Andy     | Admin     |
| Amy      | Sales     |
| John     | Purchase  |

# ⚙️ How It Works

### Step 1

User enters a question.

```
查詢訂單中的商品
```

↓

### Step 2

Prompt Engineering injects the database schema into GPT.

↓

### Step 3

GPT generates SQL.

```sql
SELECT
    oi.order_id,
    p.product_name,
    oi.quantity
FROM OrderItems oi
JOIN Products p
ON oi.product_id = p.product_id;
```

↓

### Step 4

FastAPI executes SQL.

↓

### Step 5

SQLite returns the query results.

↓

### Step 6

Results are displayed on the frontend.

---

# 💡 Prompt Engineering

Instead of allowing the LLM to generate arbitrary SQL, this project injects the database schema into the prompt.

Benefits:

- Improve SQL generation accuracy
- Prevent hallucinated tables
- Prevent hallucinated columns
- Restrict SQL to existing schema
- Support complex JOIN queries
- Improve response consistency

---

# 🎯 Project Highlights

- Developed independently from scratch
- Designed ERP-style relational database
- Built RESTful APIs using FastAPI
- Integrated OpenAI GPT-4.1-mini
- Implemented Prompt Engineering for SQL generation
- Supported multi-table JOIN queries
- Deployed online using Render
- Version controlled with Git & GitHub

---

# 🖥 Example Query

### User Input

```
查詢訂單中的商品
```

### Generated SQL

```sql
SELECT
    oi.order_id,
    p.product_name,
    oi.quantity
FROM OrderItems oi
JOIN Products p
ON oi.product_id = p.product_id;
```

### Result

| Order ID | Product | Quantity |
|----------|----------|---------|
| 1001 | Laptop | 2 |
| 1001 | Mouse | 1 |
| 1002 | Keyboard | 3 |

---

# 🚀 Installation

Clone this repository.

```bash
git clone https://github.com/your-account/ai-erp-assistant.git
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
python -m uvicorn main:app --reload
```

Open your browser.

```
http://127.0.0.1:8000
```

---

# 🔮 Future Improvements

- React Frontend
- PostgreSQL Support
- MSSQL Support
- Docker Deployment
- User Authentication
- Role-Based Access Control
- RAG-based Schema Retrieval
- Streaming Response
- More Advanced SQL Generation

---

# 👨‍💻 Author

**Yu-Tang Liu**

Backend Developer

ERP Assistant Engineer

Python • FastAPI • SQL • AI Application • Prompt Engineering

---

## ⭐ If you like this project, feel free to give it a Star!
