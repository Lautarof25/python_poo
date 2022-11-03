class Auto:
    # Variables de la clase
    ruedas = 4
    # Constructor
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
    # Métodos
    def manejar(self):
        print("Este "+self.modelo+" está andando")
    
    def detener(self):
        print("Este "+self.marca+" está detenido")

