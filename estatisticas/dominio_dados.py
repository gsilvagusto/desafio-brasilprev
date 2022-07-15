from pydantic import BaseModel, Field


class DominioDados(BaseModel):
    id: str = Field(...)
    time_out: bool = Field(...)
    turnos: int = Field(...)
    vencedor: str = Field(...)
