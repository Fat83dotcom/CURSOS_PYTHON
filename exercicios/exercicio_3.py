'''
3. Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matrı́cula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie métodos para acessar o nome e a média do aluno.
(a) Permita ao usuário entrar com os dados de 5 alunos.
(b) Encontre o aluno com maior média geral.
(c) Encontre o aluno com menor média geral
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovação
'''


class AlunosADS:
    def __init__(self, nome, matricula, notaProva):
        self.nome = nome
        self.matricula = matricula
        self.notaProva = notaProva

    def mostraNome(self):
        return self.nome

    def mediaAluno(self):
        numeroDeNotas = len(self.notaProva)
        if numeroDeNotas > 0:
            soma = 0
            for nota in self.notaProva:
                soma += nota

            media = soma / numeroDeNotas
            return round(media, 1)
        else:
            return 'Não há notas para calcular a media'


# aluno1 = AlunosADS('fernando', 'mat', [2, 4, 5])
# aluno2 = AlunosADS('maria', 'matri', [4, 5, 6])

qtdAlunos = 5
contador = 0
alunosCadastrados = []

while contador < qtdAlunos:
    nome = input(f'\nDigite o nome do {contador + 1}º aluno: ').title()
    matricula = input(f'Digite a matricula do {contador + 1}º aluno: ')
    notaProva = []
    for i in range(3):
        notaProva.append(float(input(f'Digite a nota da {i + 1}ª prova: ')))

    alunosCadastrados.append(AlunosADS(nome, matricula, notaProva))
    contador += 1

alunoMaiorNota = []
alunoMenorNota = []

for i in range(len(alunosCadastrados)):
    if i == 0:
        alunoMaiorNota.append({'nome': alunosCadastrados[i].mostraNome(), 'nota': alunosCadastrados[i].mediaAluno()})
        alunoMenorNota.append({'nome': alunosCadastrados[i].mostraNome(), 'nota': alunosCadastrados[i].mediaAluno()})

    if alunoMaiorNota[-1]['nota'] == alunosCadastrados[i].mediaAluno() and i != 0:
        alunoMaiorNota.append({'nome': alunosCadastrados[i].mostraNome(), 'nota': alunosCadastrados[i].mediaAluno()})
    if alunoMaiorNota[-1]['nota'] < alunosCadastrados[i].mediaAluno() and i != 0:
        alunoMaiorNota.clear()
        alunoMaiorNota.append({'nome': alunosCadastrados[i].mostraNome(), 'nota': alunosCadastrados[i].mediaAluno()})

    if alunoMenorNota[-1]['nota'] == alunosCadastrados[i].mediaAluno() and i != 0:
        alunoMenorNota.append({'nome': alunosCadastrados[i].mostraNome(), 'nota': alunosCadastrados[i].mediaAluno()})
    if alunoMenorNota[-1]['nota'] > alunosCadastrados[i].mediaAluno() and i != 0:
        alunoMenorNota.clear()
        alunoMenorNota.append({'nome': alunosCadastrados[i].mostraNome(), 'nota': alunosCadastrados[i].mediaAluno()})

print('\nO(s) aluno(s) com maiores médias foi(foram): \n')
for alunos in alunoMaiorNota:
    for k, v in alunos.items():
        print(f'{k} {v}', end=' - ')
        if k == 'nota':
            print('Aprovado.' if v >= 6 else 'Reprovado.')

print('\nO(s) aluno(s) com menores médias foi(foram): \n')
for alunos in alunoMenorNota:
    for k, v in alunos.items():
        print(f'{k} {v}', end=' - ')
        if k == 'nota':
            print('Aprovado.' if v >= 6 else 'Reprovado.')
