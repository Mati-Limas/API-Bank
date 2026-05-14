from pydantic import BaseModel, Field

class ContaIn(BaseModel):
    usuario: str = Field(description='Username de uma conta')
    senha: str = Field(description='Senha que será criptografada')

class ContaUpdate(BaseModel):
    usuario: str | None = Field(default=None, description='Novo username da conta') 
    senha: str | None = Field(default=None, description='Novo senha da conta')