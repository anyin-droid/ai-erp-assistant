# AI ERP Assistant

<img width="1342" height="878" alt="螢幕擷取畫面 2026-07-06 203547" src="https://github.com/user-attachments/assets/7da3899b-023f-4da8-949d-c430045a763a" />
<img width="1351" height="874" alt="螢幕擷取畫面 2026-07-06 203555" src="https://github.com/user-attachments/assets/cc5cff93-7311-4fd7-b06c-e6248bf79365" />


An AI-powered ERP query assistant that converts natural language into SQL using **OpenAI GPT-4.1-mini**.

This project simulates a real-world ERP query workflow. Users enter questions in natural language, and the system automatically generates SQL, executes the query, and returns formatted results.

---

## 🚀 Live Demo

👉 https://ai-erp-assistant-kfp9.onrender.com

---

## 📷 Project Preview

> *(Add screenshots here later)*

![Home Page](images/home.png)

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

```
ai-erp-assistant/

│
├── main.py
├── ai_service.py
├── db_service.py
├── index.html
├── orders.db
├── requirements.txt
└── .env
```

---

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
