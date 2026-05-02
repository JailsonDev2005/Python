from rich import print
from poligono import *

def main():

    d = Quadrado(12)
    print(f"perimetro = {d.perimetro()}")
    print(f"area = {d.area()}")

    c = Circulo()
    print(f"perimetro = {c.perimetro():.1f}")
    print(f"area = {c.area():.1f}")


if __name__ == "__main__":
    main()