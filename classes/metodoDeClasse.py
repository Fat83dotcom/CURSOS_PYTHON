from datetime import datetime


class Pessoa:
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def idadePorAnoNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)


p1 = Pessoa.idadePorAnoNascimento('Feranando', 1983)
print(p1.idade)
