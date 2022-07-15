import operator
from uuid import uuid4

import pandas as pd

data = pd.read_json('base_dados.json') 

partidas_time_out = data.time_out.value_counts() #pertence a partidas terminada por time out

time_out_true = (data.loc[data['time_out'] == True]) #pertence a partidas terminada por time out



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



partidas_terminadas_time_out = int(time_out_true['time_out'].count()) #informacao partidas terminadas por time out

media_turnos = data.turnos.median() # Informacao de quantos turnos em media demmora uma partida


porcetagem_impulsivo = (total_vitorias_impulsivo / 100)*100 #informacao de porcentagem de vitorias por comportamento
porcetagem_exigente = ( total_vitorias_exigente/ 100)*100 #informacao de porcentagem de vitorias por comportamento
porcetagem_cauteloso = (total_vitorias_cauteloso / 100)*100 #informacao de porcentagem de vitorias por comportamento
porcetagem_aleatorio = (total_vitorias_aleatorio / 100)*100 #informacao de porcentagem de vitorias por comportamento

comportamento_mais_vence = l[0]['comportamento'] #informacao do comportamento que mais vence


lista_analise = [
        {'Quantas partidas terminam por timeout (1000 rodadas) = ': str(partidas_terminadas_time_out)}, 
        {'Quantos turnos em media demora uma partida = ': str(media_turnos)},
        {'Qual o comportamento que mais vence = ': str(comportamento_mais_vence)},
        {'Porcentagem de vitorias por comportamento impulsivo = ': str(porcetagem_impulsivo)},
        {'Porcentagem de vitorias por comportamento exigente = ': str(porcetagem_exigente)},
        {'Porcentagem de vitorias por comportamento cauteloso = ': str(porcetagem_cauteloso)},
        {'Porcentagem de vitorias por comportamento aleatorio = ': str(porcetagem_aleatorio)},
    ]

def gerar_analise():
    arq = f"{uuid4()}.txt"
    for analise in lista_analise:
        for k, v in analise.items():
            with open(arq, 'a+') as arquivo:
                arquivo.write(f"\n {k}"+v)

