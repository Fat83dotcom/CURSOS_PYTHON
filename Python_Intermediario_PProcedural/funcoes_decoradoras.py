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


def embaralhadorNumerico(numero):
    numeros = [randint(0, numero) * x for x in range(numero)]
    return numeros


@logTempoExecucao
def contadorNumerico(numero) -> int:
    numeros = 0
    for i in range(int(numero)):
        numeros += 1
    return numeros


@logTempoExecucao
def insertionSort(listaNumeros):
    listaDeTrabalho = listaNumeros
    for i in range(len(listaDeTrabalho)):
        for j in range(i)[::-1]:
            if listaDeTrabalho[j + 1] < listaDeTrabalho[j]:
                listaDeTrabalho[j], listaDeTrabalho[j + 1] = listaDeTrabalho[j + 1], listaDeTrabalho[j]
            else:
                break
    return listaDeTrabalho


contadorNumerico(1000676000)

embaralhados = embaralhadorNumerico(10000)
insertionSort(embaralhados)