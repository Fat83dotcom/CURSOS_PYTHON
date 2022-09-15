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
    contador = 0
    while contador < qtdAlunos:
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
        dadoCompleto['cpf'] = cpfsListados[contador]
        dadoCompleto['nome'] = recebeNome
        dadoCompleto['sobrenome'] = recebeSobrenome
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
                     bancoDados: Escola,
                     nomeTabela=None,
                     nomeColuna=None,
                     nomeTabEnd=None,
                     pkTabEnd=None) -> int:
    registros: list = geradorDadosAlunos(qtdAluno)
    consultaEnderecos = bancoDados.retornarIntervalo(nomeTabEnd, pkTabEnd,
                                                     qtdAluno)
    for contador, dados in enumerate(registros):
        bancoDados.cadastroTabelas(dados['cpf'], dados['nome'], dados['sobrenome'], int(consultaEnderecos[contador][0]),
                                   nome_tabela=nomeTabela,
                                   nome_colunas=nomeColuna)
    return contador + 1


postgresSQL = Escola(host, porta, 'db_escola', 'fernandomendes', senha)

QTD_REGISTROS = 10000

registradorEnderecos(QTD_REGISTROS,
                     postgresSQL,
                     nomeColunas='(logradouro, numero, bairro, complemento)',
                     nomeTabela='cadastros_endereco')

registradorAluno(bancoDados=postgresSQL, qtdAluno=QTD_REGISTROS,
                 nomeTabela='cadastros_aluno',
                 nomeColuna='(cpf, nome_aluno, sobrenome_aluno, endereco)',
                 nomeTabEnd='cadastros_endereco', pkTabEnd='cod_end')

postgresSQL.fecharConexao()
