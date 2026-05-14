from pydantic import BaseModel, Field

class TransacaoIn(BaseModel):
    tipo: str = Field(description='Deposito ou saque')
    valor: float = Field(description='Valor da transação, não pode ser negativo')