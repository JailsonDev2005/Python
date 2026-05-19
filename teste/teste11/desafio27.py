from funcionario import *
from rich import inspect

def main():
    f1 = Horista("Jailson", 12, 200)
    f1.calcular_salario()
    f1.analisar_salario()


    f1 = Mensalista("Karla", 9500)
    f1.calcular_salario()
    f1.analisar_salario()
if __name__ == "__main__":
    main()