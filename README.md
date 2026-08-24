# 💰 Expense Tracker API

A secure **Personal Expense Tracker REST API** built with FastAPI, PostgreSQL (Supabase), SQLAlchemy, and JWT Authentication.

🚀 **Live API:** https://expense-tracker-api-ovpp.onrender.com

📚 **Swagger Docs:** https://expense-tracker-api-ovpp.onrender.com/docs

---

## 📌 Overview

Users can securely register, login, and manage their personal income and expense transactions.
Each transaction belongs to a specific user, so users can only access and manage their own transactions.

---

## ✨ Features

- 🔐 JWT Authentication & Authorization
- 👤 User Registration & Login
- 🔑 Password Hashing with Bcrypt
- 💰 Income & Expense CRUD Operations
- 🔎 Transaction Filtering by Type
- ✅ Pydantic Data Validation
- 🗄️ PostgreSQL Database with Supabase
- 📖 Swagger/OpenAPI Documentation
- 🌐 Deployed on Render

---

## 🛠️ Tech Stack

**Python · FastAPI · PostgreSQL · Supabase · SQLAlchemy · Pydantic · JWT · Passlib · Bcrypt · Pytest · Uvicorn · Render**

---

## 🏗️ Architecture

```text
Client
  ↓
FastAPI
  ↓
JWT Authentication
  ↓
API Routers
  ↓
SQLAlchemy
  ↓
PostgreSQL (Supabase)
```

---

## 📂 Project Structure

```text
expense-tracker/
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth_utils.py
│   └── router/
│       ├── auth.py
│       └── transactions.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_transactions.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register user |
| POST | `/auth/login` | Login & get JWT |
| GET | `/transactions/` | Get transactions |
| POST | `/transactions/` | Create transaction |
| GET | `/transactions/filter` | Filter transactions |
| GET | `/transactions/{transaction_id}` | Get transaction |
| PUT | `/transactions/{transaction_id}` | Update transaction |
| DELETE | `/transactions/{transaction_id}` | Delete transaction |

### Example Transaction

```json
{
  "title": "Monthly Salary",
  "amount": 50000,
  "type": "income",
  "category": "Salary",
  "date": "2026-08-24"
}
```

Filter example:
```text
GET /transactions/filter?type=income
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root with the following keys:

```env
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<db_name>
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ Never commit your `.env` file. It's already listed in `.gitignore`.

---

## ⚙️ Local Setup

```bash
git clone <your-repository-url>
cd expense-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger: `http://127.0.0.1:8000/docs`

---

## 🌐 Deployment

Deployed on Render.

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## 🔒 Security

- JWT-based authentication
- Password hashing
- User-based authorization
- Protected endpoints
- Environment variables
- Pydantic validation

---

## 🎯 Skills Demonstrated

FastAPI · REST API · CRUD · PostgreSQL · Supabase · SQLAlchemy · JWT Authentication · Authorization · Pydantic · Git · Render Deployment
