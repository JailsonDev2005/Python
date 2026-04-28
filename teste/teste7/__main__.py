from rich import print, inspect
from classesex005 import Pessoa, Aluno, Professor, Funcionario


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