from app.bo.bo_jogador import JogadorBo
from app.bo.bo_jogo import Jogo
from app.bo.bo_tabuleiro import Tabuleiro
from app.comportamento import Comportameto
from app.utils import probabilidade_50


def main():
    
    # Inicializa o jogo
    Jogo.ordenar_jogadores(Jogo) 
    
    while len(Jogo.lista_jogadores_restantes) > 1 and Jogo.rodada <= 999:
        
        for jogador in Jogo.lista_jogadores_restantes:              
            Jogo.rolar_dado(Jogo)     
            JogadorBo.mover(jogador, Jogo.dado_resultado)  
            
            if jogador.posicao <= 20:                
                jogador.comportamento(Comportameto(jogador, jogador.posicao, probabilidade_50))
                
            
            else:
                jogador.posicao -= 20
                jogador.conta += 100  
                jogador.comportamento(Comportameto(jogador, jogador.posicao, probabilidade_50))
                
            
        Jogo.nova_rodada(Jogo)
    
    print(
        f'{Jogo.lista_jogadores_restantes[0].cor} é vencedor: Comportamento: {Jogo.lista_jogadores_restantes[0].comportamento.__name__}'
    )       


if __name__ == "__main__":
    main()