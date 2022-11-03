class Predador:

    def cazar(self):
        print("Cazando")

class Presa:

    def huir(self):
        print("Huyendo")

class Conejo(Presa):
    pass

class Aguila(Predador):
    pass

class Pez(Presa, Predador):
    pass

