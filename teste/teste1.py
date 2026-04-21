from rich import print
from rich.panel import Panel


class Churrasco:
    carne_padrao:int = 0.4
    valor_padrao:int = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def carne_recomendada(self):
        return Churrasco.carne_padrao * self.quant
    
    def custo_total(self):
        return self.carne_recomendada() * Churrasco.valor_padrao
    
    def valor_cada(self):
        return self.custo_total() / self.quant

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/]  com [blue]{self.quant} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.carne_padrao}kg e cada kg custa R${Churrasco.valor_padrao:.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.carne_recomendada():.3f}kg[/] de carne"
        conteudo += f"\nO custo total de será de [green]R${self.custo_total():.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.valor_cada():.2f}[/] para participar."
        pai = Panel(conteudo,title=f"{self.titulo}", width=58)
        print(pai)



c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()