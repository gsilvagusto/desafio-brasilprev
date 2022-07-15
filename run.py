from uuid import uuid4

from app.bo.bo_jogador import JogadorBo
from app.bo.bo_jogo import Jogo
from app.comportamento import Comportameto
from app.utils import probabilidade_50
from estatisticas.dominio_dados import DominioDados
from estatisticas.repositorio_dados import RepositorioDados


def main():     
    numero_simulacoes: int = 0
    lista_dados = list()
     
    while numero_simulacoes <= 100: 
        numero_simulacoes += 1     
        # Inicializa o jogo      
        Jogo.lista_jogadores_restantes = Jogo.lista_jogadores.copy()   
        Jogo.rodada = 0   
        Jogo.embaralhar_jogadores(Jogo) 
        
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
        
        if Jogo.rodada == 1000:        
            id = str(uuid4())
            vencedor = Jogo.ordenar()
            class_dados = DominioDados(id=id, time_out=True, turnos=Jogo.rodada, vencedor=vencedor)
            dict_dados: DominioDados = class_dados.dict()
            lista_dados.append(dict_dados)
            print('Jogo finalizado por time out')
            print(
                f'{Jogo.lista_jogadores_restantes[0].cor} é vencedor: Comportamento: {Jogo.lista_jogadores_restantes[0].comportamento.__name__}'
            )
               
            break
            
            
        
        else:
            id = str(uuid4())
            vencedor = Jogo.lista_jogadores_restantes[0].cor
            class_dados = DominioDados(id=id, time_out=False, turnos=Jogo.rodada, vencedor=vencedor)
            dict_dados: DominioDados = class_dados.dict()
            lista_dados.append(dict_dados)
            print('Jogador restante')
            print(
                f'{Jogo.lista_jogadores_restantes[0].cor} é vencedor: Comportamento: {Jogo.lista_jogadores_restantes[0].comportamento.__name__}'
            )    
            
        
        
            continue       
    
    RepositorioDados.salvar_base_dados(lista_dados)

if __name__ == "__main__":   
    main()
