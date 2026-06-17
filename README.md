# 💰 FinanceAPI

API REST for management finance pessoal, building with FastAPI + MySQL.

## 🚀 Technologies

- **FastAPI** — framework web modern and for performance up.
- **SQLAlchemy** — ORM for interaction with database.
- **MySQL** — Relacional Database;
- **Alembic** — Database migrations.
- **JWT** — Security autentication with access e refresh tokens.
- **Docker** — Application containerization.
- **Pytest** — Automated tests.

## 📦 Features

- ✅ Autentication full (register, login, refresh token).
- ✅ CRUD transactions (income and expenses).
- ✅ CRUD for personalized categories.
- ✅ Balance report (total income, expenses and balance).
- ✅ Expense report by category.
- ✅ Filters by type, category, and period.
- ✅ Automated documentation via Swagger.

## ⚙️ How to run local

### Pre-requisites
- Python 3.11+
- MySQL running locally
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/felipe2008pg1/financeAPI.git
cd financeAPI

# Create and active the enviroment virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependences
pip install -r requirements.txt

# Configure as environment variables
cp .env.example .env
# Edit the .env file with your MySQL credentials.
```

### Running API

```bash
uvicorn app.main:app --reload
```

Acess: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🐳 Running with Docker

```bash
docker-compose up --build
```

## 📖 Endpoints

| Method | Route | Description |
|--------|------|-----------|
| POST | `/api/v1/auth/register` | Register user |
| POST | `/api/v1/auth/login` | Login |
| POST | `/api/v1/auth/refresh` | Refresh token |
| GET | `/api/v1/auth/me` | User autentic |
| GET | `/api/v1/categories` | List categories |
| POST | `/api/v1/categories` | Create categorie |
| PUT | `/api/v1/categories/{id}` | To update categorie |
| DELETE | `/api/v1/categories/{id}` | Delete categorie |
| GET | `/api/v1/transactions` | List transactions |
| POST | `/api/v1/transactions` | Create transactions |
| PUT | `/api/v1/transactions/{id}` | To update transactions |
| DELETE | `/api/v1/transactions/{id}` | Deletae transaction |
| GET | `/api/v1/reports/summary` | Financial summary |
| GET | `/api/v1/reports/by-category` | Spending by category |

## 🔐 Autentication

The API use JWT. After login, use `access_token` in header:
