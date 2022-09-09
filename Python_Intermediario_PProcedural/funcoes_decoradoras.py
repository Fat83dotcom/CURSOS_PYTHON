from time import time
from datetime import datetime
from random import randint


def salvaArquivo(valor, funcNome, resultado):
    with open('logExecutor.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{datetime.today()} a função {funcNome.__name__} levou '
                      f'{round(valor, 4)} segundos na execução')
        arquivo.write(f'\nForam contados / ordenados: {resultado} números.\n\n')


def logTempoExecucao(funcao):
    def motor(*args, **kwargs):
        tempoIni = time()
        resultado = funcao(*args, **kwargs)
        tempoTerm = time()
        tempoExec = tempoTerm - tempoIni
        salvaArquivo(tempoExec, funcao, resultado)

    return motor


def embaralhadorNumerico(numero) -> list:
    numeros = [randint((0 * x), numero) for x in range(numero)]
    return numeros


@logTempoExecucao
def contadorNumerico(numero) -> int:
    numeros = 0
    for i in range(int(numero)):
        numeros += 1
    return numeros


@logTempoExecucao
def insertionSort(listaNumeros):
    listaOriginal = listaNumeros.copy()
    listaDeTrabalho = listaNumeros.copy()
    for i in range(len(listaDeTrabalho)):
        for j in range(i)[::-1]:
            if listaDeTrabalho[j + 1] < listaDeTrabalho[j]:
                listaDeTrabalho[j], listaDeTrabalho[j + 1] = listaDeTrabalho[j + 1], listaDeTrabalho[j]
            else:
                break

    return f'números desordenados:{listaOriginal}, ordenados: {listaDeTrabalho},' \
        f'{len(listaDeTrabalho)}'


contadorNumerico(100)

embaralhados = embaralhadorNumerico(100)
insertionSort(embaralhados)

print(embaralhados)
