from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"

        self.cor = escolha
        self.tampada = True

    
    def escreve(self, msg):
        if self.tampada:
            print(f":prohibited: A{self.cor} caneta[/] está tampada")
        else:
            print(f"{self.cor}{msg}[/]")


    def destanpar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def quebra_linha(self, qtd = 1):
        print("\n"*qtd)


c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destanpar()
c2.destanpar()
#c1.destanpar()


c1.tampar()
c1.escreve("sei la idiota ")
c2.escreve("sei la idiota ")
c3.escreve("sei la idiota ")
