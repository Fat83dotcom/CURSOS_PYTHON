import psycopg2
from abc import ABC


class BancoDeDados(ABC):
    def __init__(self, host='', port='', dbname='', user='', password='') -> None:
        self.con = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password)
        self.cursor = self.con.cursor()

    def fecharConexao(self):
        self.con.close()

    def executar(self, sql):
        self.cursor.execute(sql)

    def enviar(self):
        self.con.commit()

    def abortar(self):
        self.con.rollback()

    def buscarDados(self):
        return self.cursor.fetchall()

    def buscarUmDado(self):
        return self.cursor.fetchone()

    def buscarIntervalo(self, intervalo):
        return self.cursor.fetchmany(intervalo)

    def geradorSQLInsert(self, *args, nome_colunas=None,  nome_tabela=None):
        valores = f'{args}'
        sql = f"INSERT INTO {nome_tabela} {nome_colunas} VALUES {valores}"
        return sql

    def geradorSQLUpdate(self, *args, nome_colunas=None, nome_tabela=None, condicao=None):
        valores = args[0]
        sql = f"UPDATE {nome_tabela} SET {nome_colunas}=('{valores}') WHERE {condicao}"
        print(sql)
        return sql

    def verificadorEnderecoExiste(self, logradouro, numero, nome_tabela=''):
        sql = f"SELECT logradouro, numero, cod_end  FROM {nome_tabela}"
        self.executar(sql)
        self.enviar()
        pesquisa = self.buscarDados()
        for valores in pesquisa:
            if logradouro == valores[0] and numero == valores[1]:
                return valores[-1]
        return False


class Escola(BancoDeDados):
    def __init__(self, host='', port='', dbname='', user='', password='') -> None:
        super().__init__(host, port, dbname, user, password)

    def __repr__(self) -> str:
        return super().__repr__()

    def contadorItens(self, nome_tabela=None) -> tuple:
        sql = f"SELECT COUNT(*) FROM {nome_tabela}"
        try:
            self.executar(sql)
            self.enviar()
            return self.buscarUmDado()
        except psycopg2.Error as erro:
            self.abortar()
            print(f'Não foi possivel executar a consulta! Codigo erro: {erro}')
            return erro,

    def retornaUltimaEntrada(self, nome_tabela=None, pk_tabela=None):
        sql = f"SELECT MAX({pk_tabela}) FROM {nome_tabela}"
        self.executar(sql)
        self.enviar()
        for i in self.buscarUmDado():
            yield i

    def retornarIntervalo(self, nome_tabela=None, pk_tabela=None, numero_consultas=0):
        sql = f"SELECT {pk_tabela} FROM {nome_tabela}"
        self.executar(sql)
        self.enviar()
        for i in self.buscarIntervalo(numero_consultas):
            yield i

    def retornarValorTabela(self, nome_tabela=None, nome_coluna=None):
        '''Retorna qualquer valor de uma coluna especifica na tabela. Função geradora'''
        sql = f"SELECT {nome_coluna} FROM {nome_tabela}"
        try:
            self.executar(sql)
            self.enviar()
            for i in self.buscarDados():
                yield i
        except psycopg2.Error as erro:
            print(f'Não foi possivel executar a consulta! Código do erro: {erro}')
            return erro,

    def cadastroTabelas(self, *args, nome_tabela=None, nome_colunas=None):
        sql = self.geradorSQLInsert(*args, nome_colunas=nome_colunas, nome_tabela=nome_tabela)
        try:
            self.executar(sql)
            self.enviar()
        except psycopg2.Error as erro:
            self.abortar()
            print('O registro não foi efetuado com sucesso!')
            print(erro)

    def atualizarTabelas(self, *args, nome_tabela=None, nome_colunas=None, condicao=None):
        sql = self.geradorSQLUpdate(*args, nome_tabela=nome_tabela, nome_colunas=nome_colunas, condicao=condicao)
        try:
            self.executar(sql)
            self.enviar()
        except psycopg2.Error as erro:
            self.abortar()
            print(f'Não foi possivel atualizar a tabela. Codigo do erro: {erro}')

    def cadastroEndereco(self, logradouro, numero, bairro, complemento, nome_tabela='', nome_colunas='') -> int:
        verificaExistencia = self.verificadorEnderecoExiste(logradouro, numero, nome_tabela=nome_tabela)
        if verificaExistencia:
            return verificaExistencia
        else:
            sql = self.geradorSQLInsert(logradouro, numero, bairro, complemento,
                                        nome_colunas=nome_colunas, nome_tabela=nome_tabela)
            self.executar(sql)
            self.enviar()
            codigoExistente = self.verificadorEnderecoExiste(
                logradouro, numero, nome_tabela=nome_tabela)
            return codigoExistente


if __name__ == '__main__':
    pass
