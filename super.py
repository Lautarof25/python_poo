class Rectangulo:

    def __init__(self, longuitud, ancho):
        self.longuitud = longuitud
        self.ancho = ancho

class Cuadrado(Rectangulo):

    def __init__(self,longuitud, ancho):
        super().__init__(longuitud,ancho)

    def area(self):
        return self.longuitud*self.ancho

class Cubo(Rectangulo):

    def __init__(self, longuitud, ancho,alto):
        super().__init__(longuitud, ancho)
        self.alto = alto

    def volumen(self):
        return self.longuitud*self.ancho*self.alto