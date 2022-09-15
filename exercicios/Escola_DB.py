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

    def geradorSQLInsert(self, *args, nome_colunas='',  nome_tabela=''):
        valores = f'{args}'
        sql1 = f"INSERT INTO {nome_tabela} {nome_colunas} VALUES {valores}"
        return sql1

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

    def cadastroTabelas(self, nome_tabela, **kwarg,):
        colunas = [v for k, v in kwarg.items()]
        sql = self.geradorSQLInsert(*colunas, nome_tabela=nome_tabela)
        try:
            self.executar(sql)
            self.enviar()
        except psycopg2.Error as erro:
            self.abortar()
            print(f'O registro {colunas}, não foi efetuado com sucesso!')
            print(erro)

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
