from datetime import datetime


class Pessoa:

    anoatual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        if not self.comendo:
            print(f'{self.nome} está comendo')
            self.comendo = True

    def pararDeComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def deixarDeFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def anoNascimento(self):
        return (self.anoatual - self.idade)


p1 = Pessoa('Fernando', 39)

# p1.comer('pera')
# p1.comer('uva')
# p1.pararDeComer()
# p1.pararDeComer()
# p1.falar('filme')
# p1.falar('maconha')
# p1.deixarDeFalar()
# p1.deixarDeFalar()

print(p1.anoatual)
print(p1.anoNascimento())
