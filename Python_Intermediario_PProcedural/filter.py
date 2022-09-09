'''
usa uma funcao relacional (maio, menor, igual) e filtra os valores de uma lista ou dicionario
'''

from dados_map import lista, produtos


def menor_5(n):
    return n < 5


menor5 = filter(menor_5, lista)

print(list(menor5))


def menorPreco(p):
    return p['preco'] < 70


preco_menor = list(filter(menorPreco, produtos))

print(preco_menor)
