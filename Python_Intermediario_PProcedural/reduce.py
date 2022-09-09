'''
faz um somatorio de uma lista ou dicionario usando uma função
'''
from dados_map import lista
from functools import reduce

print(lista)


def acumulador(ac, n):
    ac += n
    return ac


soma = reduce(acumulador, lista, 0)

print(soma)

somatorio = 0

for numero in lista:
    somatorio += numero

print(somatorio)
