from abc import ABC, abstractmethod

class Vehiculo(ABC):

    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def detener(self):
        pass

class Auto(Vehiculo):

    def conducir(self):
        print("Manejando el auto")

    def detener(self):
        print("Deteniendo el auto")

class Moto(Vehiculo):

    def conducir(self):
        print("Manejando la moto")

    def detener(self):
        print("Deteniendo la moto")

