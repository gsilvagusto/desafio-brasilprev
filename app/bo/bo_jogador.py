from dataclasses import dataclass

from app.bo.bo_tabuleiro import Tabuleiro
from app.comportamento import Comportameto
from app.domains.domains_jogador import Jogador


@dataclass
class JogadorBo:
    jogador_azul: Jogador = Jogador(
        cor="jogador_azul", conta=300, comportamento=Comportameto.impulsivo
    )
    jogador_preto: Jogador = Jogador(
        cor="jogador_preto", conta=300, comportamento=Comportameto.exigente
    )
    jogador_vermelho: Jogador = Jogador(
        cor="jogador_vermelho", conta=300, comportamento=Comportameto.cauteloso
    )
    jogador_branco: Jogador = Jogador(
        cor="jogador_branco", conta=300, comportamento=Comportameto.aleatorio
    )

    def mover(jogador, dado_resultado):
        jogador.posicao += dado_resultado
        return jogador.posicao

    def pagar(jogador, propriedade):
        from app.bo.bo_jogo import Jogo

        if jogador.conta > -1 and jogador.cor != propriedade.proprietario:
            jogador.conta -= propriedade.aluguel
            JogadorBo.__dict__[propriedade.proprietario].conta += propriedade.aluguel
            print(
                f"{jogador.cor}: pagou aluguel de {propriedade.aluguel}: {propriedade.proprietario} : propriedade: {propriedade.nome} "
            )
        else:
            for propriedade in jogador.lista_propriedades:
                propriedade.proprietario = False
            indice = Jogo.lista_jogadores_restantes.index(jogador)
            Jogo.remove_jogador(Jogo, indice)
            print(
                f"{jogador.cor}: perdeu :: Comportamento: {jogador.comportamento.__name__}"
            )

    def comprar(jogador: Jogador, posicao: int):
        propriedade = Tabuleiro.tabuleiro[posicao]

        if (
            propriedade.local != 0
            and propriedade.proprietario == False
            and jogador.conta >= propriedade.venda
        ):
            jogador.conta -= propriedade.venda
            jogador.lista_propriedades.append(propriedade)
            propriedade.proprietario = jogador.cor
            print(f"{jogador.cor}: Compra realizada com sucesso: {propriedade.nome}")
            return "Sucesso"

        elif propriedade.proprietario:
            JogadorBo.pagar(jogador, propriedade)

        else:
            print(f"{jogador.cor}: Dinheiro insuficiente: : {propriedade.nome}")
            return "Falha"
