from typing import List
from faker import Faker
from random import randint
from dadosConfidenciais import senha, host, porta
from Escola_DB import Escola
from funcoes_decoradoras import logTempoExecucao


@logTempoExecucao
def geradorCpf(qtdCpfs: int) -> list:
    cpfs: set = set()
    while len(cpfs) <= qtdCpfs:
        numero = randint(10000000000, 99999999999)
        cpfs.add(numero)
    listagemCpf = list(cpfs)
    return listagemCpf


@logTempoExecucao
def geradorDadosAlunos(qtdAlunos: int) -> list:
    geradorFalso = Faker(locale='pt-br')
    cpfsListados = geradorCpf(qtdAlunos)
    dadosColetados: list = []
    for i in range(qtdAlunos):
        dadoBruto: str = geradorFalso.name()
        recebeNome = ''
        recebeSobrenome = ''
        dadoCompleto = {
            'cpf': '',
            'nome': '',
            'sobrenome': '',
            'endereco': '',
        }
        if '.' in dadoBruto:
            continue
        else:
            separador: list = dadoBruto.split(' ')
            recebeNome = separador[0]
            separador.pop(0)
            recebeSobrenome = ' '.join(separador)
        dadoCompleto['cpf'] = cpfsListados[i]
        dadoCompleto['nome'] = recebeNome
        dadoCompleto['sobrenome'] = recebeSobrenome
        dadosColetados.append(dadoCompleto)
    return dadosColetados


@logTempoExecucao
def geradorEndereco(qtdEnderecos: int) -> list:
    geradorFalso = Faker(locale='pt-br')
    dadoCompleto: list = []
    while len(dadoCompleto) < qtdEnderecos:
        enderecoBruto: str = geradorFalso.address()
        dadoColetado = {
            'logradouro': '',
            'numero': '',
            'bairro': '',
            'complemento': 'Casa, Apto...'
        }
        dadoBruto = enderecoBruto.split('\n')
        if dadoBruto[0][-1].isdigit():
            dadoColetado['bairro'] = dadoBruto[1]
            if "'" not in dadoColetado['bairro']:
                lograNum = dadoBruto[0].split(',')
                dadoColetado['logradouro'] = lograNum[0]
                dadoColetado['numero'] = lograNum[1].strip()
                dadoColetado['bairro'] = dadoBruto[1]
                dadoCompleto.append(dadoColetado)
    return dadoCompleto


@logTempoExecucao
def registradorEnderecos(qtdEnderecos: int, bancoDados: Escola) -> int:
    enderecos = geradorEndereco(qtdEnderecos)

    for contador, endereco in enumerate(enderecos):
        bancoDados.cadastroEndereco(
            endereco['logradouro'],
            endereco['numero'],
            endereco['bairro'],
            endereco['complemento'],
            nome_tabela='cadastros_endereco',
            nome_colunas='(logradouro, numero, bairro, complemento)')
    bancoDados.fecharConexao()
    return contador + 1


def registradorAluno(qtdAluno: int, bancoDados: Escola) -> int:
    registros: list = geradorDadosAlunos()
    for contador, dados in registros:
        pass


postgresSQL = Escola(host, porta, 'db_escola', 'fernandomendes', senha)

QTD_REGISTROS = 5000

registradorEnderecos(QTD_REGISTROS, postgresSQL)
