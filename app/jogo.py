from dataclasses import dataclass
from random import randint, sample


@dataclass
class Jogo:
    lista_jogagores = ["azul", "branco", "vermelho", "preto"]
    lista_jogagores_restantes = lista_jogagores
    rodada: int = 0
    dado_resultado: int = None

    def ordenar_jogadores(self):
        self.lista_jogagores_restantes = sample(
            self.lista_jogagores, k=len(self.lista_jogagores)
        )

    def rolar_dado(self):
        self.dado_resultado = randint(1, 6)
