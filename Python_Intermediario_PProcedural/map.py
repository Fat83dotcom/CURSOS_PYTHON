'''
Aplica uma função em um conteudo de uma lista ou dicionario, modificando seu conteudo ou não,
podendo acrescentar qualquer coisa a lista ou dicionario.
'''


from dados_map import pessoas, produtos, lista


def dobro(x):
    return x * 2


novaLista = map(dobro, lista)

for i in novaLista:
    print(i)

novaLista = [x * 2 for x in lista]
print(novaLista)


def pegaPreco(p):
    p['preco'] = round(p['preco'] + p['preco'] * (5 / 100), 2)
    return p['preco']


precos = map(pegaPreco, produtos)

print(produtos)

for preco in precos:
    print(preco)

print(produtos)


def pegaNome(n):
    return n['nome']


nomes = map(pegaNome, pessoas)
for nome in nomes:
    print(nome)
