from app.bo.bo_jogador import JogadorBo
from app.bo.bo_tabuleiro import Tabuleiro


def test_mover():
    jogador = JogadorBo.jogador_azul
    dado_resultado = 4
    posicao_atual = JogadorBo.mover(jogador, dado_resultado)
    assert jogador.posicao == posicao_atual


def test_comprar_sucesso():
    jogador = JogadorBo.jogador_azul
    posicao = 1
    prop = Tabuleiro.tabuleiro[posicao]
    msg = JogadorBo.comprar(jogador, posicao)
    assert "Sucesso" == msg
    assert prop in jogador.lista_propriedades


def test_comprar_falha():
    jogador = JogadorBo.jogador_azul
    jogador.lista_propriedades = [Tabuleiro.tabuleiro[8]]
    posicao = 2
    prop = Tabuleiro.tabuleiro[posicao]
    lista = jogador.lista_propriedades
    msg = JogadorBo.comprar(jogador, posicao)
    assert "Falha" == msg
    assert prop not in lista
