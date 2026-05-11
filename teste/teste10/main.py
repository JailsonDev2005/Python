from rich import print
from transporte import *
from rich.table import Table


def main():
    dist = 5
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    """frete = Drone(dist)
    print(f"O frete de {type(frete).__name__} de {dist}km é = {frete.calcular_frete()}")"""

    exibir = Table(title="Tabela de Frete")
    exibir.add_column("Distância")
    exibir.add_column("Tipo")
    exibir.add_column("Frete")

    for item in viagem:
          exibir.add_row(f"{dist}km",f"{type(viagem).__name__}",f"{item.calcular_frete()}")

    print(exibir)


if __name__ == "__main__":
        main()