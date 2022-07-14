from dataclasses import dataclass

from app.bo.bo_tabuleiro import Tabuleiro
from app.comportamento import Comportameto
from app.domains.domains_jogador import Jogador


@dataclass
class JogadorBo:
    jogador_azul: Jogador = Jogador(
        cor="azul", conta=300, comportamento=Comportameto.impulsivo
    )
    jogador_preto: Jogador = Jogador(
        cor="preto", conta=300, comportamento=Comportameto.exigente
    )
    jogador_vermelho: Jogador = Jogador(
        cor="vermelho", conta=300, comportamento=Comportameto.cauteloso
    )
    jogador_branco: Jogador = Jogador(
        cor="branco", conta=300, comportamento=Comportameto.aleatorio
    )

    def mover(jogador, dado_resultado):
        jogador.posicao += dado_resultado
        return jogador.posicao

    def pagar(jogador, propriedade):
        from app.bo.bo_jogo import Jogo

        if jogador.conta >= propriedade.aluguel:
            jogador.conta -= propriedade.aluguel
            print(f"Jogador_{jogador.cor} pagou {propriedade.aluguel}")
        else:
            for propriedade in jogador.lista_propriedades:
                propriedade.proprietario = False
            indice = Jogo.lista_jogadores_restantes.index(jogador)
            Jogo.remove_jogador(Jogo, indice)
            print(f"Jogador_{jogador.cor}: perdeu")

    def comprar(jogador: Jogador, posicao: int):
        propriedade = Tabuleiro.tabuleiro[posicao]

        if (
            propriedade.local != 0
            and propriedade.proprietario == False
            and jogador.conta >= propriedade.venda
        ):
            jogador.conta -= propriedade.venda
            jogador.lista_propriedades.append(propriedade)
            propriedade.proprietario = True
            print(
                f"Jogador_{jogador.cor}: Compra realizada com sucesso: {propriedade.nome}"
            )
            return "Sucesso"

        elif propriedade.proprietario:
            JogadorBo.pagar(jogador, propriedade)

        else:
            print(
                f"Jogador_{jogador.cor}: Não foi possível realizar a comprar desta propriedade: : {propriedade.nome}"
            )
            return "Falha"
