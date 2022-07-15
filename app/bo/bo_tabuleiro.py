from dataclasses import dataclass

from app.domains.domains_propriedade import Propriedade


@dataclass
class Tabuleiro:
    inicio = Propriedade(nome="posição de início", local=0)
    barra = Propriedade(nome="barra", venda=30, aluguel=10, local=1)
    botafogo = Propriedade(nome="botafogo", venda=30, aluguel=15, local=2)
    copacabana = Propriedade(nome="copacabana", venda=40, aluguel=20, local=3)
    leblon = Propriedade(nome="leblon", venda=50, aluguel=25, local=4)
    ipanema = Propriedade(nome="ipanema", venda=50, aluguel=30, local=5)
    recreio = Propriedade(nome="recreio", venda=60, aluguel=30, local=6)
    lapa = Propriedade(nome="lapa", venda=60, aluguel=25, local=7)
    flamengo = Propriedade(nome="flamengo", venda=70, aluguel=30, local=8)
    laranjeiras = Propriedade(nome="laranjeiras", venda=80, aluguel=35, local=9)
    leme = Propriedade(nome="leme", venda=100, aluguel=200, local=10)
    lagoa = Propriedade(nome="lagoa", venda=150, aluguel=90, local=11)
    centro = Propriedade(nome="centro", venda=160, aluguel=95, local=12)
    mangueira = Propriedade(nome="mangueira", venda=180, aluguel=100, local=13)
    tijuca = Propriedade(nome="tijuca", venda=200, aluguel=120, local=14)
    vila_isabel = Propriedade(nome="vila_isabel", venda=250, aluguel=140, local=15)
    bomsucesso = Propriedade(nome="bomsucesso", venda=300, aluguel=200, local=16)
    meier = Propriedade(nome="meier", venda=400, aluguel=230, local=17)
    taquara = Propriedade(nome="taquara", venda=450, aluguel=250, local=18)
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
