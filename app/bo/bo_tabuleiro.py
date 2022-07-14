from dataclasses import dataclass

from app.domains.domains_propriedade import Propriedade


@dataclass
class Tabuleiro:
    inicio = Propriedade(nome="posição de início", local=0)
    barra = Propriedade(nome="barra", venda=50, aluguel=10, local=1)
    botafogo = Propriedade(nome="botafogo", venda=60, aluguel=20, local=2)
    copacabana = Propriedade(nome="copacabana", venda=70, aluguel=30, local=3)
    leblon = Propriedade(nome="leblon", venda=80, aluguel=40, local=4)
    ipanema = Propriedade(nome="ipanema", venda=90, aluguel=50, local=5)
    recreio = Propriedade(nome="recreio", venda=100, aluguel=60, local=6)
    lapa = Propriedade(nome="lapa", venda=110, aluguel=50, local=7)
    flamengo = Propriedade(nome="flamengo", venda=120, aluguel=70, local=8)
    laranjeiras = Propriedade(nome="laranjeiras", venda=130, aluguel=80, local=9)
    leme = Propriedade(nome="leme", venda=140, aluguel=90, local=10)
    lagoa = Propriedade(nome="lagoa", venda=150, aluguel=100, local=11)
    centro = Propriedade(nome="centro", venda=160, aluguel=110, local=12)
    mangueira = Propriedade(nome="mangueira", venda=170, aluguel=120, local=13)
    tijuca = Propriedade(nome="tijuca", venda=180, aluguel=130, local=14)
    vila_isabel = Propriedade(nome="vila_isabel", venda=190, aluguel=140, local=15)
    bomsucesso = Propriedade(nome="bomsucesso", venda=200, aluguel=150, local=16)
    meier = Propriedade(nome="meier", venda=300, aluguel=200, local=17)
    taquara = Propriedade(nome="taquara", venda=400, aluguel=250, local=18)
    jacarepagua = Propriedade(nome="jacarepagua", venda=500, aluguel=300, local=19)
    santa_teresa = Propriedade(nome="santa_teresa", venda=600, aluguel=400, local=20)
    tabuleiro = (
        inicio,
        barra,
        botafogo,
        copacabana,
        leblon,
        ipanema,
        recreio,
        lapa,
        flamengo,
        laranjeiras,
        leme,
        lagoa,
        centro,
        mangueira,
        tijuca,
        vila_isabel,
        bomsucesso,
        meier,
        taquara,
        jacarepagua,
        santa_teresa,
    )
