from pyparsing import empty

from estatisticas.dominio_dados import DominioDados
from estatisticas.repositorio_dados import RepositorioDados


def test_salvar_no_banco():
    id = "123432"
    time_out = False
    turnos = 178
    vencedor = "aleatorio"
    class_dados = DominioDados(
        id=id, time_out=time_out, turnos=turnos, vencedor=vencedor
    )
    dict_dados: DominioDados = class_dados.dict()
    lista_dados = []
    lista_dados.append(dict_dados)
    res = RepositorioDados.salvar_base_dados(lista_dados)
    assert res == "sucesso"
