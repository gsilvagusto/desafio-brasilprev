import json


class RepositorioDados:
    def salvar_base_dados(lista_dados):
        try:
            with open("base_dados.json", "w") as dados:
                json.dump(lista_dados, dados, indent=2)
                print("Dados salvo com sucesso")
                return "sucesso"
        except:
            print("Erro ao salvar na base de dados")
            return "falha"
