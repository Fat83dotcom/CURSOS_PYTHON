from time import time
from datetime import datetime
from random import randint


def salvaArquivo(valor, funcNome, resultado):
    with open('logExecutor.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{datetime.today()}: A função {funcNome.__name__} levou '
                      f'{round(valor, 4)} segundos na execução\n')
        arquivo.write(f'{datetime.today()}: Foram contados / ordenados / processados: {resultado} números / registros.\n\n')


def logTempoExecucao(funcao):
    def motor(*args, **kwargs):
        tempoIni = time()
        resultado = funcao(*args, **kwargs)
        tempoTerm = time()
        tempoExec = tempoTerm - tempoIni
        salvaArquivo(tempoExec, funcao, resultado)
        return resultado
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
    for numeroAnalizado in range(len(listaDeTrabalho)):
        for numeroComparado in range(numeroAnalizado)[::-1]:
            if listaDeTrabalho[numeroComparado + 1] < listaDeTrabalho[numeroComparado]:
                listaDeTrabalho[numeroComparado], listaDeTrabalho[numeroComparado + 1] = \
                    listaDeTrabalho[numeroComparado + 1], listaDeTrabalho[numeroComparado]
            else:
                break

    return f'Quantidade de números ordenado: {len(listaDeTrabalho)}' \
           f'\nNúmeros desordenados:{listaOriginal}\nOrdenados: {listaDeTrabalho},\n'


@logTempoExecucao
def insertionSort2(lista):
    listaDeTrabalho = lista.copy()
    listaOriginal = lista.copy()
    for i in range(1, len(listaDeTrabalho)):
        numeroAnalizado = listaDeTrabalho[i]
        j = i - 1
        while j >= 0 and numeroAnalizado < listaDeTrabalho[j]:
            listaDeTrabalho[j + 1] = listaDeTrabalho[j]
            j = j - 1
        listaDeTrabalho[j + 1] = numeroAnalizado
    return f'Quantidade de números ordenado: {len(listaDeTrabalho)}' \
           f'\nNúmeros desordenados:{listaOriginal}\nOrdenados: {listaDeTrabalho},\n'


# if __name__ == '__main__':
#     contadorNumerico(1000000)

#     embaralhados = embaralhadorNumerico(1)
#     insertionSort(embaralhados)
#     insertionSort2(embaralhados)

#     print(embaralhados)
