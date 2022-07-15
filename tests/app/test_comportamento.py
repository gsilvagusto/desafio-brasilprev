from app.bo.bo_jogador import JogadorBo
from app.bo.bo_tabuleiro import Tabuleiro
from app.comportamento import Comportameto


def test_comportamento_impulsivo():
    jogador = JogadorBo.jogador_azul
    dado_resultado = 1
    posicao = JogadorBo.mover(jogador, dado_resultado)
    prop = Tabuleiro.tabuleiro[posicao]
    probabilidade_50 = 2
    msg = jogador.comportamento(Comportameto(jogador, posicao, probabilidade_50))
    assert msg == "Sucesso"
    assert prop in jogador.lista_propriedades


def test_comportamento_exigente():
    jogador = JogadorBo.jogador_preto
    dado_resultado = 3
    posicao = JogadorBo.mover(jogador, dado_resultado)
    prop = Tabuleiro.tabuleiro[posicao]
    probabilidade_50 = 2
    msg = jogador.comportamento(Comportameto(jogador, posicao, probabilidade_50))
    assert msg == "Sucesso"
    assert prop in jogador.lista_propriedades


def test_comportamento_cauteloso():
    jogador = JogadorBo.jogador_vermelho
    dado_resultado = 1
    posicao = JogadorBo.mover(jogador, dado_resultado)
    prop = Tabuleiro.tabuleiro[posicao]
    probabilidade_50 = 2
    msg = jogador.comportamento(Comportameto(jogador, posicao, probabilidade_50))
    assert msg == "Sucesso"
    assert prop in jogador.lista_propriedades


def test_comportamento_aleatorio():
    jogador = JogadorBo.jogador_branco
    dado_resultado = 1
    posicao = JogadorBo.mover(jogador, dado_resultado)
    prop = Tabuleiro.tabuleiro[posicao]
    probabilidade_50 = 2
    msg = jogador.comportamento(Comportameto(jogador, posicao, probabilidade_50))
    assert msg == "Sucesso"
    assert prop in jogador.lista_propriedades
