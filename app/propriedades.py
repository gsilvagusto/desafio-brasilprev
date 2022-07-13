from collections import namedtuple

p = namedtuple("Propriedade", "proprietario venda aluguel local vendida")

barra = p(None, 100, 10, 0, False)
botafogo = p(None, 100, 10, 1, False)
copacabana = p(None, 100, 10, 2, False)
leblon = p(None, 100, 10, 3, False)
ipanema = p(None, 100, 10, 4, False)
recreio = p(None, 100, 10, 5, False)
lapa = p(None, 100, 10, 6, False)
flamengo = p(None, 100, 10, 7, False)
laranjeiras= p(None, 100, 10, 8, False)
leme = p(None, 100, 10, 9, False)
lagoa = p(None, 100, 10, 10, False)
centro = p(None, 100, 10, 11, False)
mangueira = p(None, 100, 10, 12, False)
tijuca = p(None, 100, 10, 13, False)
vila_isabel= p(None, 100, 10, 14, False)
bomsucesso = p(None, 100, 10, 15, False)
meier = p(None, 100, 10, 16, False)
taquara= p(None, 100, 10, 17, False)
jacarepagua = p(None, 100, 10, 18, False)
santa_teresa = p(None, 100, 10, 19, False)


tupla_propriedades = (
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
    santa_teresa
)
