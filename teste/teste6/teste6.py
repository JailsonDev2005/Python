from rich import print, inspect

class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma


    def fazer_matriucula(self):
        print(f"O aluno(a) {self.nome} fez a matricula.")



class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f"O professor(a) {self.nome} esta dando aula.")



class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    
    def bater_ponto(self):
        print(f"O funcionario(a) {self.nome} bateu o ponto.")


p1 = Pessoa("Jailson", 20)
p2 = Aluno("Paulo", 20, "Informatica", "TI01")
p2.fazer_aniversario()
p2.fazer_matriucula()
p3 = Professor("Givanildo", 41, "Geografia", "Mestrado")
p3.fazer_aniversario()
p3.dar_aula()
p4 = Funcionario("Ana", 32, "Secretaria", "atendimento")
p4.fazer_aniversario()
p4.bater_ponto()
inspect(p1)
inspect(p2)
inspect(p3)
inspect(p4)