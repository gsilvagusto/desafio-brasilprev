from dataclasses import dataclass
from random import randint, sample


@dataclass
class Jogo:
    lista_jogadores = ["azul", "branco", "vermelho", "preto"]
    lista_jogadores_restantes = lista_jogadores
    rodada: int = 0
    dado_resultado: int = None

    def ordenar_jogadores(self):
        self.lista_jogadores_restantes = sample(
            self.lista_jogadores, k=len(self.lista_jogadores)
        )

    def rolar_dado(self):
        self.dado_resultado = randint(1, 6)

    def nova_rodada(self):
        self.rodada += 1