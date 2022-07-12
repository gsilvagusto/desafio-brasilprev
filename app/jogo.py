from dataclasses import dataclass
from random import sample
from typing import List


@dataclass
class Jogo:
    lista_jogagores = ["azul", "branco", "vermelho", "preto"]
    lista_jogagores_restantes = lista_jogagores
    rodada: int = 0

    def ordenar_jogadores(self):
        self.lista_jogagores_restantes = sample(
            self.lista_jogagores, k=len(self.lista_jogagores)
        )
