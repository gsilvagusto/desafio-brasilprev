from tests.fixtures import criar_jogo


def test_embaralhar_jogadores(criar_jogo):
    lista_original = criar_jogo.lista_jogadores
    lista_aleatoria = criar_jogo.embaralhar_jogadores()
    assert lista_original != lista_aleatoria


def test_dado_resultado(criar_jogo):
    criar_jogo.rolar_dado()
    lista = [i for i in range(1, 7)]

    assert criar_jogo.dado_resultado in lista


def test_nova_rodada(criar_jogo):
    criar_jogo.nova_rodada()
    assert criar_jogo.rodada == 1


def test_remove_jogador(criar_jogo):
    criar_jogo.remove_jogador(3)
    assert len(criar_jogo.lista_jogadores_restantes) != len(criar_jogo.lista_jogadores)
