from pydantic import BaseModel, Field


class Propriedade(BaseModel):
    nome: str = Field(...)
    venda: int = 0
    aluguel: int = 0
    local: int = Field(...)
    proprietario: bool = False
