from fastapi import APIRouter, HTTPException, Depends
from database import database, sa
from models.conta import contas
from models.transacoes import transacoes
from schemas.transacoes import TransacaoIn
from views.transacoes import TransacaoOut
from services.auth import get_conta_atual
from datetime import datetime, timezone


router = APIRouter(prefix='/transacao')

@router.post('/', response_model=TransacaoOut,
             summary='Realiza uma transação',
             description='Faz uma nova transação, ' \
             'pode ser tanto um saque quanto um deposito, ' \
             'chegando os valores e modificando o saldo de uma conta')
async def fazer_transacao(transacao: TransacaoIn, conta_id: int = Depends(get_conta_atual)):
    conta_atual = await database.fetch_one(contas.select().where(contas.c.id == conta_id))
    if transacao.valor <= 0:
        raise HTTPException(status_code=422, detail='Os valores das transações não podem ser negativos')
    elif transacao.tipo == 'saque':
        if transacao.valor > conta_atual['saldo']:
            raise HTTPException(status_code=422, detail='Valor de saldo na conta insuficiente')
    comando = transacoes.insert().values(conta_id = conta_id,
                                         tipo = transacao.tipo,
                                     valor = transacao.valor,
                                     data = datetime.now(timezone.utc))
    transacao_id = await database.execute(comando)
    if transacao.tipo == 'deposito':
        novo_saldo = conta_atual['saldo'] + transacao.valor
    elif transacao.tipo == 'saque':
        novo_saldo = conta_atual['saldo'] - transacao.valor
    
    await database.execute(contas.update().where(contas.c.id == conta_id).values(saldo=novo_saldo))
    return await database.fetch_one(transacoes.select().where(transacoes.c.id == transacao_id))

@router.get('/extrato', response_model=list[TransacaoOut],
            summary='Obtem o extrato de uma conta',
            description='Fornece o extrato de transações completo de uma conta através de seu id')
async def mostrar_extrato(conta_id: int = Depends(get_conta_atual)):
    query = sa.select(transacoes).where(transacoes.c.conta_id == conta_id)
    resultado = await database.fetch_all(query)
    return resultado