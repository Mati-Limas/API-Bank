#FEATURES 
- User registration and authentication with JWT
- Deposits and withdrawals linked to the authenticated account
- Full transaction history
- Account update and deletion
- Balance validation for withdrawals
- Automatic documentation via Swagger UI

- # Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

Access the documentation at `http://127.0.0.1:8000/docs`

# Endpoints

| Method | Route | Description | Auth |
|--------|-------|-------------|------|
| POST | `/auth/cadastro` | Create account | no |
| POST | `/auth/login` | Authenticate and get token | no |
| PATCH | `/conta/` | Update account data | yes |
| DELETE | `/conta/` | Delete account | yes |
| POST | `/transacao/` | Make a deposit or withdrawal | yes |
| GET | `/transacao/extrato` | List account transactions | yes |
