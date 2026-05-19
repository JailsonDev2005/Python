from rich import print
from abc import ABC, abstractmethod

class Funcionario(ABC):

    sal_min = 1.612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    @abstractmethod
    def anlisar_sal(self):
        pass
        


class Horista(Funcionario):
    def __init__(self, nome, valor_hora=7.37, horas_trab=220):
        super().__init__(nome)
        self.valor_horas = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = valor_hora * horas_trab

    def calc_sal(self):
        self.salario = self.sal_bruto - (Funcionario.inss / 100)

    def anlisar_sal(self):
        base = self.salario / Funcionario.sal_min
        print(f"o salario de {self.nome} e de R${self.salario:.2f} e corresponde a {base:.2f} salarios minimos")




class Mensalista(Funcionario):
    pass
