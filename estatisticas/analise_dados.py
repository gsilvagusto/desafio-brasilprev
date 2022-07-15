import pandas as pd 
import operator

# Qual a porcentagem de vitórias por comportamento dos jogadores;
  
data = pd.read_json('base_dados.json') 

partidadas_time_out = data.time_out.value_counts()

time_out_true = (data.loc[data['time_out'] == True])

partidas_terminadas_time_out = time_out_true['time_out'].count() #informacao partidas terminadas por time out

media_turnos = data.turnos.median()

vitorias_impulsivo = (data.loc[data['vencedor'] == "impulsivo"])
total_vitorias_impulsivo = vitorias_impulsivo['vencedor'].count() #informacao total de vitorias por comportamento

vitorias_exigente = (data.loc[data['vencedor'] == 'exigente'])
total_vitorias_exigente = vitorias_exigente['vencedor'].count() #informacao total de vitorias por comportamento

vitorias_cauteloso = (data.loc[data['vencedor'] == 'cauteloso'])
total_vitorias_cauteloso = vitorias_cauteloso['vencedor'].count() #informacao total de vitorias por comportamento


vitorias_aleatorio = (data.loc[data['vencedor'] == "aleatorio"])
total_vitorias_aleatorio = vitorias_aleatorio['vencedor'].count() #informacao total de vitorias por comportamento

lista_ordenada_ganhadores = [
    {'comportamento':'impulsivo', 'total': total_vitorias_impulsivo},
    {'comportamento':'exigente', 'total':total_vitorias_exigente},
    {'comportamento':'cauteloso', 'total':total_vitorias_cauteloso},
    {'comportamento':'aleatorio', 'total':total_vitorias_aleatorio},
]

l = sorted(lista_ordenada_ganhadores, key=operator.itemgetter("total"), reverse=True)

comportamento_mais_vence = l[0] #informacao do comportamento que mais vence

porcetagem_impulsivo = (total_vitorias_impulsivo / 10)*100 #informacao de porcentagem de vitorias por comportamento
porcetagem_exigente = ( total_vitorias_exigente/ 10)*100 #informacao de porcentagem de vitorias por comportamento
porcetagem_cauteloso = (total_vitorias_cauteloso / 10)*100 #informacao de porcentagem de vitorias por comportamento
porcetagem_aleatorio = (total_vitorias_aleatorio / 10)*100 #informacao de porcentagem de vitorias por comportamento


print(data)

