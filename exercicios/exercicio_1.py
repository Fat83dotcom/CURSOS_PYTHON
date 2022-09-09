'''1. Crie uma classe que modele uma pessoa
(a) Atributos: nome, idade e enderec¸o
(b) Metodos: mostrar enderec¸o e alterar enderec¸o
'''


class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrarEndereco(self):
        print(self.endereco)
