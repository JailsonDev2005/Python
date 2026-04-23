from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, pagina):
        self.titulo = titulo
        self.total_paginas = pagina
        self.pagina_atual = 1

        
        
        
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.total_paginas} páginas[/] no total. Você está na [yellow]página {self.pagina_atual}[/][/]")
    
    def avancar_pagina(self, qtd=1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                cont += 1
                print(f"Pág{self.pagina_atual} :triangular_flag_on_post: ", end="")
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")


    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False

l1 = Livro("10 coisas que aprendi", 10)
l1.avancar_pagina(10)
