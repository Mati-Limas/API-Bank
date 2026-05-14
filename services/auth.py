from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

secret_key = 'chave-hyper-secreta'
algorithm = 'HS256'
expiracao = 30
pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def criptografar_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)

def criar_token(dados: dict) -> str:
    dados['exp'] = datetime.now(timezone.utc) + timedelta(minutes=expiracao)
    token = jwt.encode(dados, secret_key, algorithm="HS256")
    print(f"TOKEN GERADO: {token}")
    return token

def verificar_token(token: str) -> dict:
    payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    return payload
async def get_conta_atual(token: str = Depends(oauth2_scheme)):
    print(f"TOKEN RECEBIDO: {token}")
    payload = verificar_token(token)
    conta_id = int(payload['sub'])
    return conta_id