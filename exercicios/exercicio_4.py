'''4. Crie uma classe que modele um carro
(a) Atributos: marca, ano e preço
(b) Métodos: mostrar preço e de exibição dos dados
Leia os dados de 5 carros e um valor p, Mostre as informações de todos os carros com
preço menor que p.
'''


class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novoValor):
        if isinstance(novoValor, (int, float)):
            self._preco = novoValor
        else:
            self._preco = 'Valor incorreto.'

    def mostrarPreco(self):
        return self.preco

    def mostraDados(self):
        print(f'Marca: {self.marca}, Ano: {self.ano}')


qtdCarros = 2
contador = 0
carrosCadastrados = []

while contador < qtdCarros:
    marca = input('Digite a marca do carro:').title()
    ano = input('Digite o ano de fabricação do carro: ')
    

c1 = Carro('mercedes', '1989', "23000")

print(c1.preco)
