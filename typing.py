class Pato:

    def caminar(self):
        print("Caminando como pato")

    def hablar(self):
        print("haciendo cuack")

class Gallina:

    def caminar(self):
        print("Caminando como gallina")

    def hablar(self):
        print("Haciendo co co ro co")

class Persona:

    def atrapar(self,pato):
        pato.caminar()
        pato.hablar()
        print("Atrapando al animal")