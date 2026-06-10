<div align="center">

#  API-Bank

**Asynchronous RESTful API for managing bank accounts and transactions**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

---

##  Overview

API-Bank is a fully asynchronous banking REST API built with **FastAPI** and **SQLAlchemy**. It handles user registration, JWT-based authentication, and financial transactions — all with auto-generated interactive documentation via Swagger UI. A static frontend is also served directly from the application.

---

## ✨ Features

- 🔐 **User registration and authentication** with JWT tokens
- 💸 **Deposits and withdrawals** linked to the authenticated account
- 📊 **Full transaction history** (bank statement)
- ✏️ **Account update and deletion**
- 🛡️ **Balance validation** before withdrawals
- ⚡ **Async database access** via `databases` + `aiosqlite`
- 🌐 **Static frontend** served at the root route
- 📚 **Auto-generated docs** via Swagger UI and ReDoc

---

##  Project Structure

```
API-Bank/
├── controllers/        # Route handlers (auth, conta, transacao)
├── models/             # SQLAlchemy table definitions
├── schemas/            # Pydantic request/response models
├── services/           # Business logic layer
├── static/             # Frontend files (HTML/CSS/JS)
├── views/              # HTML templates (if any)
├── database.py         # Database connection and metadata setup
├── main.py             # Application entry point
└── requirements.txt    # Project dependencies
```

---

##  Getting Started

### Prerequisites

- **Python 3.10 or higher**
- **pip** (comes bundled with Python)
- **Git**

---

### 🐧 Linux

> The core steps are the same across all distros. The difference is **how you install Python and pip** before starting.

---

#### Ubuntu / Debian

```bash
# Install Python and required tools
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y

# Clone the repository
git clone https://github.com/Mati-Limas/API-Bank.git
cd API-Bank

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

<details>
<summary><strong>⚠️ Common issues on Ubuntu/Debian</strong></summary>

**`python3-venv` not found or venv creation fails**
```bash
sudo apt install python3-venv python3-full -y
```

**`pip install` fails with `externally-managed-environment`** (Ubuntu 23.04+/Debian 12+)
> This is a system protection. Always use a venv (as shown above) — never use `--break-system-packages`.
```

</details>

---

#### Arch Linux / Manjaro

```bash
# Install Python and Git (Python 3 is already the default on Arch)
sudo pacman -Syu python python-pip git --noconfirm

# Clone the repository
git clone https://github.com/Mati-Limas/API-Bank.git
cd API-Bank

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

<details>
<summary><strong>⚠️ Common issues on Arch/Manjaro</strong></summary>

**`pip install` fails with `externally-managed-environment`**
> Arch enforces PEP 668. Always install inside a venv. If you really need to install globally (not recommended):
```bash
pip install -r requirements.txt --break-system-packages
```

**`uvicorn` not found after installing**
> The venv may not be active. Check for `(venv)` at the start of your prompt. If missing:
```bash
source venv/bin/activate
```

</details>

---

#### Fedora / RHEL / CentOS Stream

```bash
# Install Python and Git
sudo dnf install python3 python3-pip git -y

# Clone the repository
git clone https://github.com/Mati-Limas/API-Bank.git
cd API-Bank

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

<details>
<summary><strong>⚠️ Common issues on Fedora/RHEL</strong></summary>

**`python3-venv` not available**
```bash
sudo dnf install python3-virtualenv -y
```

**`pip` not found after activating venv**
```bash
python3 -m ensurepip --upgrade
```

</details>

---

#### openSUSE

```bash
# Install Python and Git
sudo zypper install python3 python3-pip git

# Clone the repository
git clone https://github.com/Mati-Limas/API-Bank.git
cd API-Bank

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

<details>
<summary><strong>⚠️ Common issues on openSUSE</strong></summary>

**`python3-venv` not found**
```bash
sudo zypper install python3-virtualenv
```

</details>

---

### 🍎 macOS

```bash
# 1. Clone the repository
git clone https://github.com/Mati-Limas/API-Bank.git
cd API-Bank

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the server
uvicorn main:app --reload
```

> **Note:** If `python3` is not found, install it via [Homebrew](https://brew.sh/): `brew install python`

---

### 🪟 Windows

```powershell
# 1. Clone the repository
git clone https://github.com/Mati-Limas/API-Bank.git
cd API-Bank

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the server
uvicorn main:app --reload
```

> **Note:** If `python` is not recognized, download the installer from [python.org](https://www.python.org/downloads/) and make sure to check **"Add Python to PATH"** during installation.

---

### ✅ Verifying the server is running

After starting, the terminal should display:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

Open your browser and navigate to:

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000` | Frontend interface |
| `http://127.0.0.1:8000/docs` | Swagger UI (interactive docs) |
| `http://127.0.0.1:8000/redoc` | ReDoc documentation |

---

## 📡 API Endpoints

### Authentication

| Method | Route | Description | Auth Required |
|--------|-------|-------------|:---:|
| `POST` | `/auth/cadastro` | Create a new account | ❌ |
| `POST` | `/auth/login` | Authenticate and receive JWT token | ❌ |

### Account

| Method | Route | Description | Auth Required |
|--------|-------|-------------|:---:|
| `PATCH` | `/conta/` | Update account data | ✅ |
| `DELETE` | `/conta/` | Delete account | ✅ |

### Transactions

| Method | Route | Description | Auth Required |
|--------|-------|-------------|:---:|
| `POST` | `/transacao/` | Make a deposit or withdrawal | ✅ |
| `GET` | `/transacao/extrato` | List all account transactions | ✅ |

---

### 🔑 Authentication Flow

Authenticated endpoints require a **Bearer token** in the `Authorization` header.

**1. Register**
```http
POST /auth/cadastro
Content-Type: application/json

{
  "nome": "John Doe",
  "email": "john@example.com",
  "senha": "strongpassword123"
}
```

**2. Login and get token**
```http
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "senha": "strongpassword123"
}
```

**3. Use token on protected routes**
```http
GET /transacao/extrato
Authorization: Bearer <your_token_here>
```

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM / database toolkit |
| [databases](https://www.encode.io/databases/) | Async database access |
| [aiosqlite](https://github.com/omnilib/aiosqlite) | Async SQLite driver |
| [python-jose](https://github.com/mpdavis/python-jose) | JWT generation and validation |
| [passlib + bcrypt](https://passlib.readthedocs.io/) | Password hashing |
| [Pydantic v2](https://docs.pydantic.dev/) | Data validation and schemas |
| [uvicorn](https://www.uvicorn.org/) | ASGI server |

---

## 📄 License

This project is for educational purposes.
