from faker import Faker
from random import randint
from dadosConfidenciais import senha, host, porta
from Escola_DB import Escola
from funcoes_decoradoras import logTempoExecucao
# from itertools import count


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
    contador = 0
    while contador < qtdAlunos:
        dadoBruto: str = geradorFalso.name()
        datanasc = geradorFalso.date_between(start_date="-60y", end_date="-16y")
        recebeNome = ''
        recebeSobrenome = ''
        dadoCompleto = {
            'cpf': '',
            'nome': '',
            'sobrenome': '',
            'endereco': '',
            'nasc': '',
        }
        if '.' in dadoBruto:
            continue
        else:
            separador: list = dadoBruto.split(' ')
            recebeNome = separador[0]
            separador.pop(0)
            recebeSobrenome = ' '.join(separador)
        dadoCompleto['cpf'] = cpfsListados[contador]
        dadoCompleto['nome'] = recebeNome
        dadoCompleto['sobrenome'] = recebeSobrenome
        dadoCompleto['nasc'] = datanasc
        dadosColetados.append(dadoCompleto)
        contador += 1
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
def registradorEnderecos(qtdEnderecos: int,
                         bancoDados: Escola,
                         nomeTabela=None,
                         nomeColunas=None) -> int:
    enderecos = geradorEndereco(qtdEnderecos)
    for contador, endereco in enumerate(enderecos):
        bancoDados.cadastroEndereco(endereco['logradouro'],
                                    endereco['numero'],
                                    endereco['bairro'],
                                    endereco['complemento'],
                                    nome_tabela=nomeTabela,
                                    nome_colunas=nomeColunas)
    return contador + 1


@logTempoExecucao
def registradorAluno(qtdAluno: int,
                     bD: Escola,
                     nomeT=None,
                     nomeC=None,
                     nomeTabEnd=None,
                     pkTabEnd=None) -> int:
    registros: list = geradorDadosAlunos(qtdAluno)
    consultaEnderecos = bD.retornarIntervalo(nomeTabEnd, pkTabEnd, qtdAluno)
    for contador, dados in enumerate(registros):
        bD.cadastroTabelas(dados['cpf'], dados['nome'], dados['sobrenome'], int(consultaEnderecos[contador][0]),
                           nome_tabela=nomeT,
                           nome_colunas=nomeC)
    return contador + 1


@logTempoExecucao
def atualizadorRegistrosViaPKDataAniversario(bD: Escola, nomeT=None, nomeC=None, nomeCPesquisa=None, cond=None):
    Faker.seed(763)
    data = Faker(locale='pt-BR')
    chavesP = bD.retornarValorTabela(nome_tabela=nomeT, nome_coluna=nomeCPesquisa)
    numeroColunas: int = bD.contadorItens(nome_tabela=nomeT)[0]
    for i in range(numeroColunas):
        atualizacao = data.date_between(start_date="-60y", end_date="-16y")
        bD.atualizarTabelas(atualizacao, nome_tabela=nomeT, nome_colunas=nomeC, condicao=f"{cond}'{next(chavesP)[0]}'")
    return i + 1


postgresSQL = Escola(host, porta, 'db_escola', 'fernandomendes', senha)

QTD_REGISTROS = 1000

# registradorEnderecos(QTD_REGISTROS,
#                      postgresSQL,
#                      nomeColunas='(logradouro, numero, bairro, complemento)',
#                      nomeTabela='cadastros_endereco')

# registradorAluno(bD=postgresSQL, qtdAluno=QTD_REGISTROS,
#                  nomeT='cadastros_aluno',
#                  nomeC='(cpf, nome_aluno, sobrenome_aluno, endereco)',
#                  nomeTabEnd='cadastros_endereco', pkTabEnd='cod_end')

# atualizadorRegistrosViaPKDataAniversario(postgresSQL, nomeT='cadastros_aluno', nomeC='dt_nasc', nomeCPesquisa='cpf', cond='cpf=')
postgresSQL.fecharConexao()
