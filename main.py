from fastapi import FastAPI
from controllers.auth import router as auth_router
from controllers.transacao import router as transacao_router
from controllers.conta import router as conta_router
from database import engine, database, metadata
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.conta import contas
    from models.transacoes import transacoes
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan,
              title='Bank API',
              description='API bancária para gerenciamento de contas e transações com autentificação JWToken',
              version='1.0.0')


app.include_router(auth_router)
app.include_router(transacao_router)
app.include_router(conta_router)