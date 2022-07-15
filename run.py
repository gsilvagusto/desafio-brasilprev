from uuid import uuid4

from app.bo.bo_jogador import JogadorBo
from app.bo.bo_jogo import Jogo
from app.comportamento import Comportameto
from app.domains.domains_jogador import Jogador
from app.utils import probabilidade_50
from estatisticas.analise_dados import gerar_analise
from estatisticas.dominio_dados import DominioDados
from estatisticas.repositorio_dados import RepositorioDados


def main():
    numero_simulacoes: int = 0
    lista_dados = list()

    while numero_simulacoes <= 100:
        numero_simulacoes += 1
        # Inicializa o jogo

        JogadorBo.jogador_azul = Jogador(
            cor="jogador_azul", conta=300, comportamento=Comportameto.impulsivo
        )
        JogadorBo.jogador_preto = Jogador(
            cor="jogador_preto", conta=300, comportamento=Comportameto.exigente
        )
        JogadorBo.jogador_vermelho = Jogador(
            cor="jogador_vermelho", conta=300, comportamento=Comportameto.cauteloso
        )
        JogadorBo.jogador_branco = Jogador(
            cor="jogador_branco", conta=300, comportamento=Comportameto.aleatorio
        )
        Jogo.lista_jogadores_restantes = Jogo.lista_jogadores.copy()
        Jogo.rodada = 0
        Jogo.embaralhar_jogadores(Jogo)

        while len(Jogo.lista_jogadores_restantes) > 1 and Jogo.rodada <= 999:

            for jogador in Jogo.lista_jogadores_restantes:
                Jogo.rolar_dado(Jogo)
                JogadorBo.mover(jogador, Jogo.dado_resultado)

                if jogador.posicao <= 20:
                    jogador.comportamento(
                        Comportameto(jogador, jogador.posicao, probabilidade_50)
                    )

                else:
                    jogador.posicao -= 20
                    jogador.conta += 100
                    jogador.comportamento(
                        Comportameto(jogador, jogador.posicao, probabilidade_50)
                    )

            Jogo.nova_rodada(Jogo)

        if Jogo.rodada >= 1000:
            id = str(uuid4())
            vencedor = Jogo.ordenar()
            class_dados = DominioDados(
                id=id, time_out=True, turnos=Jogo.rodada, vencedor=vencedor
            )
            dict_dados: DominioDados = class_dados.dict()
            lista_dados.append(dict_dados)
            print("Jogo finalizado por time out")
            print(
                f"{Jogo.lista_jogadores_restantes[0].cor} é vencedor: Comportamento: {Jogo.lista_jogadores_restantes[0].comportamento.__name__}"
            )

            continue

        elif len(Jogo.lista_jogadores_restantes) < 2:
            id = str(uuid4())
            vencedor = Jogo.lista_jogadores_restantes[0].comportamento.__name__
            class_dados = DominioDados(
                id=id, time_out=False, turnos=Jogo.rodada, vencedor=vencedor
            )
            dict_dados: DominioDados = class_dados.dict()
            lista_dados.append(dict_dados)
            print("Jogador restante")
            print(
                f"{Jogo.lista_jogadores_restantes[0].cor} é vencedor: Comportamento: {Jogo.lista_jogadores_restantes[0].comportamento.__name__}"
            )

        continue

    RepositorioDados.salvar_base_dados(lista_dados)


if __name__ == "__main__":
    main()
    gerar_analise()
