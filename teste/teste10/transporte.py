from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    
    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)
    

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}".replace(".", ",")


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return "[red]minino de 50km[/]"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}".replace(".",",")


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)


    def calcular_frete(self):
        if self.distancia  > 10:
            return "[red]maximo 10km[/]"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}".replace(".",",")