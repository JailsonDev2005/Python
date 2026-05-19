from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod


class Funcionario(ABC):
    salario_minimo = 1612
    desconto_inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0
        

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def analisar_salario(self):
        pass


class Horista(Funcionario):

    def __init__(self, nome, valor_hora=7.37, qtd_hora=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_hora = qtd_hora
        self.salario_bruto = self.valor_hora * self.qtd_hora


    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss / 100)
        self.salario_min = self.salario / Funcionario.salario_minimo


    def analisar_salario(self):
         conteudo = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario_min:.1f} salario minimo[/]."
         painel = Panel(conteudo, title="Análise de Salário", width=50)
         print(painel) 


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto


    def calcular_salario(self):
        self.salario_bruto = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss / 100)
        self.salario_min = self.salario_bruto / Funcionario.salario_minimo

    def analisar_salario(self):
        conteudo = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.salario_bruto:.2f}[/] e corresponde e [yellow]{self.salario_min:.1f} salário minimos[/]"
        painel = Panel(conteudo,title="Analise de Sálario", width=50)
        print(painel)