# 💰 FinanceAPI

API REST para gestão financeira pessoal, construída com FastAPI + MySQL.

## 🚀 Tecnologias

- **FastAPI** — framework web moderno e de alta performance
- **SQLAlchemy** — ORM para interação com o banco de dados
- **MySQL** — banco de dados relacional
- **Alembic** — migrations de banco de dados
- **JWT** — autenticação segura com access e refresh tokens
- **Docker** — containerização da aplicação
- **Pytest** — testes automatizados

## 📦 Funcionalidades

- ✅ Autenticação completa (register, login, refresh token)
- ✅ CRUD de transações (receitas e despesas)
- ✅ CRUD de categorias personalizadas
- ✅ Relatório de saldo (total de receitas, despesas e saldo)
- ✅ Relatório de gastos por categoria
- ✅ Filtros por tipo, categoria e período
- ✅ Documentação automática via Swagger

## ⚙️ Como rodar localmente

### Pré-requisitos
- Python 3.11+
- MySQL rodando localmente
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/felipe2008pg1/financeAPI.git
cd financeAPI

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais do MySQL
```

### Rodando a API

```bash
uvicorn app.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🐳 Rodando com Docker

```bash
docker-compose up --build
```

## 📖 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/api/v1/auth/register` | Cadastro de usuário |
| POST | `/api/v1/auth/login` | Login |
| POST | `/api/v1/auth/refresh` | Refresh token |
| GET | `/api/v1/auth/me` | Usuário autenticado |
| GET | `/api/v1/categories` | Listar categorias |
| POST | `/api/v1/categories` | Criar categoria |
| PUT | `/api/v1/categories/{id}` | Atualizar categoria |
| DELETE | `/api/v1/categories/{id}` | Deletar categoria |
| GET | `/api/v1/transactions` | Listar transações |
| POST | `/api/v1/transactions` | Criar transação |
| PUT | `/api/v1/transactions/{id}` | Atualizar transação |
| DELETE | `/api/v1/transactions/{id}` | Deletar transação |
| GET | `/api/v1/reports/summary` | Resumo financeiro |
| GET | `/api/v1/reports/by-category` | Gastos por categoria |

## 🔐 Autenticação

A API utiliza JWT. Após o login, utilize o `access_token` no header: