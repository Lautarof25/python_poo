########################## autos

# Importamos nuestra clase
from autos import Auto

# Creamos el objeto auto

auto_1 = Auto("Fiat","Palio","2010","Azul")
auto_2 = Auto("Ford","mustage","2018","Rojo")

print(auto_1.marca)
print(auto_2.marca)
print(auto_1.modelo)
print(auto_2.modelo)
print(auto_1.anio)
print(auto_2.anio)
print(auto_1.color)
print(auto_2.color)

# Modificar ruedas
print(auto_1.ruedas)

auto_1.ruedas = 5

print(auto_1.ruedas)

# Podemos modificar las variables de la clase para todos los objetos

Auto.ruedas = 2

# Acciones

auto_1.manejar()
auto_1.detener()

############################# animal

from animal import *

conejo = Conejo()
pez = Pez()
aguila = Aguila()

print(conejo.vive)
pez.comer()
aguila.comer()
aguila.volar()
conejo.correr()
pez.nadar()

############################### her_multinivel

from her_multinivel import *

perro = Perro()

print(perro.vive)
perro.comer()
perro.ladrar()

############################# her_multiple

from her_multiple import *

conejo = Conejo()
aguila = Aguila()
pez = Pez()

conejo.huir()
aguila.cazar()
pez.huir()
pez.cazar()


############################### sobreescribir

from sobreescribir import *

conejo = Conejo()
conejo.comer()

################################ Chaining
# Llamar multiples métodos secuencialmente
# Cada método llama a una acción del mismo objeto

from chaining import Auto

auto = Auto()

auto.encender()\
    .conducir()\
    .frenar()\
    .apagar()

########################## super
# Es usado para dar acceso a los métodos de clases padres
# Retorna un objeto temporal de una clase padre cuando es usada

from super import *

cuadrado = Cuadrado(3,3)
cubo = Cubo(3,3,3)

print(cuadrado.area())
print(cubo.volumen())

###################### abstract
# PREVIENE a los usuarios de crear un objeto de una Clase
# Sus métodos deben ser sobrescritos por sus hijos
# Es una clase fantasma
# La clase abstracta contiene Uno o más métodos.
# El método abstracto Está declarado pero no implementado

from abstract import Vehiculo,Auto,Moto

# Podemos hacer que se creen vehiculos de auto y moto, 
# pero no de su clase padre

auto = Auto()
moto = Moto()

auto.conducir()
moto.detener()

####################### Objetos como argumento

from objeto_arg import *

auto_1 = Auto()
auto_2 = Auto()
auto_3 = Auto()

moto_1 = Moto()

cambiar_color(auto_1,"Rojo")
cambiar_color(auto_2,"Azul")
cambiar_color(auto_3,"Verde")
cambiar_color(moto_1,"Negro")

print(auto_1.color)
print(auto_2.color)
print(auto_3.color)
print(moto_1.color)

#####################  typing
# La clase de un objeto es menos importan que los métodos y atributos
# La clase no es verificado si los mínimos atributos/metodos están presentes
# "Si camina como pato y hace cuak, debe ser un pato""

from typing import *

pato = Pato()
gallina = Gallina()
persona = Persona()

persona.atrapar(pato)
persona.atrapar(gallina)