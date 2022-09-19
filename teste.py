from faker import Faker
# from datetime import datetime
from exercicios.Escola_DB import Escola


# resutado = [teste.bothify(text='Senhas: ??#???#????#???') for _ in range(10)]
# resultado1 = [teste.catch_phrase() for _ in range(200)]?

# print(resultado1)

# for i in range(10):
#     teste1: str = teste.geo()
#     print(teste1)


# for i in range(10):
#     print(teste.date_between(start_date="-60y", end_date="-16y"))

# print(datetime.date(1970, 4, 5))


def atualizadorRegistrosViaPKDataAniversario(bD: Escola, nomeT=None, nomeC=None, nomeCPesquisa=None, cond=None):
    Faker.seed(763)
    data = Faker(locale='pt-BR')
    chavesP = bD.retornarValorTabela(nome_tabela=nomeT, nome_coluna=nomeCPesquisa)
    numeroColunas: int = bD.contadorItens(nome_tabela=nomeT)[0]
    for i in range(numeroColunas):
        atualizacao = data.date_between(start_date="-60y", end_date="-16y")
        bD.atualizarTabelas(atualizacao, nome_tabela=nomeT, nome_colunas=nomeC, condicao=f'{cond}{next(chavesP)[0]}')


banco = Escola(host='192.168.0.4', port='5432', dbname='db_curso_boson', user='fernando', password='230383asD#')

tabela = 'cliente'
coluna = 'nome_cliente'
# valor = date_between(start_date="-60y", end_date="-16y")
condicao = 'cod_cliente='
tupla: str = ''

atualizadorRegistrosViaPKDataAniversario(bD=banco, nomeT=tabela, nomeC=coluna, nomeCPesquisa='cod_cliente', cond=condicao)


# print(banco.geradorSQLUpdate('maria', nome_colunas=coluna, nome_tabela=tabela, condicao=condicao))

# var = banco.retornarValorTabela(nome_tabela='cliente', nome_coluna='cod_cliente')
# for i in var:
#     print(i)
# print(var)
# print(var)
# print(hasattr(var, '__iter__'))

# var = iter(var)

# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))
# banco.atualizarTabelas('porra', nome_tabela=tabela, nome_colunas=coluna, condicao=condicao)

# print(banco.contadorItens(nome_tabela=tabela)[0])


banco.fecharConexao()
# if len(valor) == 1:
#     tupla = '%s'
# else:
#     n: int = len(valor)
#     tupla = (n - 1) * "%s, "
#     tupla += "%s"


# sql = f"update {tabela} set {coluna}=('{valor}') where {condicao}"


# banco.executar(sql=sql)
# banco.enviar()
# print(sql, tuple(valor))


# print(3 * '%s, ')

# p = 3 * '%s, '
# print(p)
