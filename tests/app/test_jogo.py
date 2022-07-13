import pytest


@pytest.fixture
def criar_jogo():
    from app.jogo import Jogo
    return(Jogo())



def test_lista_jogadores_ordem_aleatoria(criar_jogo):
    
    criar_jogo.ordenar_jogadores()    
    assert criar_jogo.lista_jogadores_restantes != criar_jogo.lista_jogadores
    
    

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
 