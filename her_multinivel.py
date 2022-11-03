class Organismo:
    vive = True

class Animal(Organismo):

    def comer(self):
        print("Comiendo")

class Perro(Animal):

    def ladrar(self):
        print("Ladrando")