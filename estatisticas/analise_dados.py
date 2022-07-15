import pandas as pd 
# Qual a porcentagem de vitórias por comportamento dos jogadores;
# Qual o comportamento que mais vence
  
data = pd.read_json('base_dados.json') 

partidadas_time_out = data.time_out.value_counts()

time_out_true = (data.loc[data['time_out'] == True])

partidas_terminadas_time_out = time_out_true['time_out'].sum()

turnos_media = data.turnos.median()

total_vitorias_jogador_vermelho = (data.loc[data['vencedor'] == 'jogador_vermelho'])
total_vitorias_jogador_azul = (data.loc[data['vencedor'] == 'jogador_azul'])
total_vitorias_jogador_branco = (data.loc[data['vencedor'] == 'jogador_branco'])
total_vitorias_aleatório = (data.loc[data['vencedor'] == 'aleatório'])

print(data)

