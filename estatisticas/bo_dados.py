from dataclasses import dataclass
from uuid import uuid4

from app.bo.bo_jogo import Jogo
from estatisticas.dominio_dados import DominioDados


@dataclass
class BoDados:
    def adicionar(dict_dados):
        return dict_dados
