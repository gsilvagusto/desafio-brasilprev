from app.jogo import Jogo

from app.tabuleiro import Tabuleiro

def main():
 
    
    # Inicializa o jogo
    jogo = Jogo()    
    
    while len(jogo.lista_jogadores_restantes) > 1:
        jogo.ordenar_jogadores()
        
        for jogador in jogo.lista_jogadores_restantes:
            jogo.rolar_dado()
            a = Tabuleiro.tabuleiro[2]
            
            print(a)
            # print(jogador.cor, jogo.dado_resultado)
        
        break
        


if __name__ == "__main__":
    main()