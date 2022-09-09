'''Crie uma classe que modele uma aluno
(a) Atributos: nome, numero de matr ´ ´ıcula e curso
(b) Metodos: mostrar curso e alterar curso
'''


class Aluno:
    def __init__(self, nome, numeroMatricula, curso):
        self.nome = nome
        self.numeroMatricula = numeroMatricula  # atributos !!!!
        self.curso = curso

    def mostrarCurso(self):
        print(self.curso)

    def trocarCurso(self, novoCurso):
        self.curso = novoCurso

    @property  # getter (Indica que esta função se comporta como um artibuto)
    def curso(self):  # Quando o atributo é chamado em algum lugar, ele vem dessa função.
        return self._curso  # É necessario que esta variavel possua um nome diferente do
        # atributo da classe, para evitar um loop bizarro.

    @curso.setter  # setter
    def curso(self, novoCurso):  # Quando um valor é atribuido ao atributo (variavel) de classe, esse valor
        if not isinstance(novoCurso, (int, float)):  # passa por esse getter e é configurado conforme
            self._curso = novoCurso  # a necessidade
        else:
            self._curso = 'Não foi possivel atrubuir o curso'


a1 = Aluno('fernando mendes oliveira', '2sd3455', 21212121)

a1.mostrarCurso()  # A atribuição no momento de instanciar a variavel a1 não satisfaz a
# condição do setter, que não aceita valores numéricos
print(a1.curso)  # Mostra uma mensagem configurada no setter
a1.trocarCurso(888888)  # A tentativa de uma nova atribuição mal suscedida
a1.mostrarCurso()  # Novamente mostra a mensagem de erro do setter
a1.trocarCurso('Análise e Desenvolvimento de Sistemas')  # Nova tentativa de atribuição
a1.mostrarCurso()  # Agora o atributo de classe recebeu o valor corretamente
