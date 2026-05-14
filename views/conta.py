from pydantic import BaseModel, Field

class ContaOut(BaseModel):
    id: int = Field(description='id gerado após a criação da conta')
    usuario: str = Field(description='username dado pelo criador da conta')
    saldo: float = Field(description='Saldo total da conta, por padrão ele começa em 0')
