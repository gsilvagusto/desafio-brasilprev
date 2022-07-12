from app.jogo import Jogo


def test_lista_jogadores_ordem_aleatoria():
    jogo = Jogo()
    lista_jogadores_ordem_aleatoria = jogo.ordenar_jogadores()
    
    assert lista_jogadores_ordem_aleatoria != jogo.ordenar_jogadores
    