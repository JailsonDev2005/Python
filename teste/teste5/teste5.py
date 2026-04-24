from rich import print
from rich.panel import Panel

class TV:
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 6


    def __init__(self, canal = 1, volume = 2):
        self.canal_atual = canal
        self.volume_atual = volume
        self.tv_ligada:bool = False

    def mostra_tv(self):
        conteudo = ""
        if self.tv_ligada == False:
            conteudo = f":prohibited: [red]A TV esta desligada[/]"
        else:
            conteudo += "CANAL = "
            for canal in range(self.canal_min, self.canal_max+1):
                if self.canal_atual == canal:
                    conteudo += f" [white on yellow] {canal} [/] "
                else:
                    conteudo += f" {canal} "

            conteudo += "VOLUME = "
            for volume in range(self.volume_min, self.volume_max+1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"
            

        
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)


    def liga_desliga(self):
        if self.tv_ligada == False:
            self.tv_ligada = True
        else:
            self.tv_ligada = False


    def canal_mais(self):
        if not self.canal_atual == self.canal_max:
            self.canal_atual += 1
        else:
            self.canal_atual = self.canal_min



    def canal_menos(self):
        if not self.canal_atual == self.canal_min:
            self.canal_atual -= 1
        else:
            self.canal_atual = self.canal_max


    def volume_mais(self):
        self.volume_atual += 1

    def volume_menos(self):
        self.volume_atual -= 1



t1 = TV(1, 2)


while True:
    t1.mostra_tv()
    conntrole = str(input(f"< CH >  - VOL + "))
    match conntrole:
        case "@":
            t1.liga_desliga()
        case "<":
            t1.canal_menos()
        case ">":
            t1.canal_mais()
        case "-":
            t1.volume_menos()
        case "+":
            t1.volume_mais()
        case "0":
            break

    print(f"\n"*30)