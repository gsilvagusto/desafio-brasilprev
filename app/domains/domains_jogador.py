from typing import Any, List

from pydantic import BaseModel, Field


class Jogador(BaseModel):
    cor: str = Field(...)
    conta: int = Field(...)
    lista_propriedades: List = []
    posicao: int = 0
    comportamento: Any = None
