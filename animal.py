class Animal:
    vive = True

    def comer(self):
        print("Este animal está comiendo ")

    def dormir(self):
        print("Este animal está durmiendo ")

class Conejo(Animal):

    def correr(self):
        print("Corriendo")

class Pez(Animal):

    def nadar(self):
        print("Nadando")

class Aguila(Animal):

    def volar(self):
        print("Volando")
