import operator
from dataclasses import dataclass
from random import randint, shuffle

from app.bo.bo_jogador import JogadorBo


@dataclass
class Jogo:

    lista_jogadores = [
        JogadorBo.jogador_azul,
        JogadorBo.jogador_preto,
        JogadorBo.jogador_vermelho,
        JogadorBo.jogador_branco,
    ]
    lista_rest = lista_jogadores
    lista_jogadores_restantes = lista_jogadores.copy()
    rodada: int = 1
    dado_resultado: int = None

    def embaralhar_jogadores(self):
        shuffle(self.lista_jogadores_restantes)
        print("")

    def rolar_dado(self):
        self.dado_resultado = randint(1, 6)

    def nova_rodada(self):
        self.rodada += 1
        print(f"Rodada numero {self.rodada}")

    def remove_jogador(self, indice):
        return self.lista_jogadores_restantes.pop(indice)

    def ordenar():
        lista = list()
        for jogador in Jogo.lista_jogadores_restantes:
            lista.append(
                {
                    "comportamento": jogador.comportamento.__name__,
                    "conta": jogador.conta,
                }
            )
        ordenar = sorted(lista, key=operator.itemgetter("conta"), reverse=True)
        return ordenar[0]["comportamento"]
