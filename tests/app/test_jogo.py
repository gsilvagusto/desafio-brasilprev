from app.jogo import Jogo


def test_lista_jogadores_ordem_aleatoria():
    jogo = Jogo()
    lista_jogadores_ordem_aleatoria = jogo.ordenar_jogadores()
    
    assert lista_jogadores_ordem_aleatoria != jogo.ordenar_jogadores
    

def test_dado_resultado():
    jogo = Jogo()
    jogo.rolar_dado()
    lista = [i for i in range(1, 7)]
    
    assert jogo.dado_resultado in lista