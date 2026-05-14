from fastapi import APIRouter, Depends, status
from services.auth import get_conta_atual
from views.conta import ContaOut
from schemas.conta import ContaUpdate
from models.conta import contas
from services.auth import criptografar_senha
from database import database

router = APIRouter(prefix='/conta')


@router.patch('/', response_model=ContaOut,
              summary='Atualiza dados da conta',
              description='Atualiza usuário e senha, ou apenas um desses campos de uma conta')
async def atualizar_conta(conta: ContaUpdate, conta_id: int = Depends(get_conta_atual)):
    dados = conta.model_dump(exclude_none=True)

    if 'senha' in dados:
        dados['senha'] = criptografar_senha(dados['senha'])
    
    comando = contas.update().where(contas.c.id == conta_id).values(**dados)
    await database.execute(comando)
    return await database.fetch_one(contas.select().where(contas.c.id == conta_id))

@router.delete('/', status_code=status.HTTP_204_NO_CONTENT,
               summary='deleta uma conta',
               description='Apartir de um id especifico, ele deleta uma única conta do banco')
async def deletar_conta(conta_id: int = Depends(get_conta_atual)):
    comando = contas.delete().where(contas.c.id == conta_id)
    return await database.execute(comando)