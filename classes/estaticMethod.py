from random import randint


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @staticmethod
    def geradorId():
        nAleatorio = randint(0, 1000000)
        return nAleatorio


p1 = Pessoa('Fernando')

print(p1.geradorId())

print(Pessoa.geradorId())
