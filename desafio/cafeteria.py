from abc import ABC,abstractmethod

class Bebidas(ABC):

        def incio(self):
                return "--- Iniciando o Preparo"
        
        def fim(self):
                return "\n--- Bebida Pronta ---"
    
        @abstractmethod
        def prepara(self):
                pass
        
class Cafe(Bebidas):

        def prepara(self):
                conteudo = self.incio()
                conteudo += "\n1. Fervendo água a 100 graus Celsius."
                conteudo += "\n2. Passando água pressurizada pelo pó de café moido."
                conteudo += "\n3. Servindo em xicara pequena."
                conteudo += self.fim()
                print(conteudo)

        


class Cha(Bebidas):

        def prepara(self):
                conteudo = self.incio()
                conteudo += "\n1. Fervendo água a 100 graus Celsius."
                conteudo += "\n2. Mergulha o sachê de ervas na água."
                conteudo += "\n3. Servindo na caneca de porcelana com limâo."
                conteudo += self.fim()
                print(conteudo)
        

class Leite(Bebidas):

        def prepara(self):
                conteudo = self.incio()
                conteudo += "\n1. Fervendo água a 100 graus Celsius."
                conteudo += "\n2. Passando vapor pressurizado pelo bico do leite."
                conteudo += "\n3. Servindo na caneca grande, ja com café."
                conteudo += self.fim()
                print(conteudo)