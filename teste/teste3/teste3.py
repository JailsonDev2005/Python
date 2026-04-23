from rich import print
from rich.panel import Panel

class Game:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favorito = []

    
    def add_favorito(self, jogo):
        self.favorito.append(jogo)


    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome}[/]"
        conteudo += "\nJogo favoritos:"
        for jg in self.favorito:
            conteudo += f"\n:video_game: [blue]{jg}[/]"
        tela = Panel(conteudo, title=f"Jogador <{self.nick}>", width=30)
        print(tela)

g1 = Game("Jailson silva", "Hunter000")
g1.add_favorito("Clahs royale")
g1.add_favorito("Free fire")
g1.add_favorito("Call of duty")
g1.add_favorito("GTA S")
g1.ficha()