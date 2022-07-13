from dataclasses import dataclass
from random import randint, sample

from app.jogador import Jogador

@dataclass
class Jogo():
    jogador_azul = Jogador("azul", 300, None, None)
    jogador_preto = Jogador("preto", 300, None, None)
    jogador_vermelho = Jogador("vermelho", 300, None, None)
    jogador_branco = Jogador("branco", 300, None, None)
    lista_jogadores = [jogador_azul, jogador_preto, jogador_vermelho, jogador_branco]
    lista_jogadores_restantes = lista_jogadores.copy()
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
        
        
    def remove_jogador(self, indice):
        return(self.lista_jogadores_restantes.pop(indice))
