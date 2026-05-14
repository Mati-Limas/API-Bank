from pydantic import BaseModel, Field
from datetime import datetime

class TransacaoOut(BaseModel):
    id: int = Field(description='Id da transação')
    conta_id: int = Field(description='Id da conta ligada a transação')
    tipo: str = Field(description='O tipo da transação, saque ou deposito')
    valor: float = Field(description='O valor da transação, não pode ser negativo')
    data: datetime = Field(description='A data de quando a transação foi realizada')