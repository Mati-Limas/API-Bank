from fastapi import APIRouter, status, HTTPException, Depends
from database import database, sa
from models.conta import contas
from schemas.conta import ContaIn
from views.conta import ContaOut
from services.auth import criptografar_senha, verificar_senha, criar_token, get_conta_atual
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(prefix='/auth')


@router.post('/cadastro', 
             status_code=status.HTTP_201_CREATED, 
             response_model=ContaOut,
             summary='Cadastro de novas contas',
             description='Cria uma nova conta com usuário e senha criptografada')
async def criar_conta(conta: ContaIn):
    query = sa.select(contas).where(contas.c.usuario == conta.usuario)
    resultado = await database.fetch_one(query)
    if resultado:
        raise HTTPException(status_code=400, detail='Usuário já existente')
    senha_hash = criptografar_senha(conta.senha)
    criacao = contas.insert().values(usuario = conta.usuario,
                                    senha = senha_hash,
                                    saldo = 0.0)
    conta_id = await database.execute(criacao)
    return {**conta.model_dump(), 'id': conta_id, 'saldo': 0.0}

@router.post('/login',
             summary='Faz login em uma conta especifica',
             description='O usuário entra com usuário e senha de uma conta para conectar nela')
async def login_conta(form: OAuth2PasswordRequestForm = Depends()):
    query = sa.select(contas).where(contas.c.usuario == form.username)
    resultado = await database.fetch_one(query)
    if not resultado:
        raise HTTPException(status_code=401, detail='Credenciais inválidas')
    verificacao = verificar_senha(form.password, resultado['senha'])
    if not verificacao:
        raise HTTPException(status_code=401, detail='Credenciais inválidas')
    token = criar_token({"sub": str(resultado['id'])})
    return {"access_token": token, "token_type": "bearer"}