from personagem import *
from rich import inspect

def main():
    p1 = Guerreiro("Superman", 200)
    p2 = Mago("apolo", 200)
    p1.atacar(p2, 200)
    p2.cura()

if __name__ == "__main__":
    main()