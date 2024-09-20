Teoría previa
En este ejercicio vas a trabajar el concepto de herencia un poco más en profundidad, aprovechando para introducir un nuevo concepto muy importante que te facilitará la vida.
Hasta ahora sabemos que una clase heredada puede fácilmente extender algunas funcionalidades, simplemente añadiendo nuevos atributos y métodos, o sobreescribiendo los ya existentes. Como en el siguiente ejemplo:
class Vehiculo():
def __init__(self, color, ruedas):
self.color = color
self.ruedas = ruedas
def __str__(self):
return "Color {}, {} ruedas".format( self.color, self.ruedas )
class Coche(Vehiculo):
def __init__(self, color, ruedas, velocidad, cilindrada):
self.color = color
self.ruedas = ruedas
self.velocidad = velocidad
self.cilindrada = cilindrada
def __str__(self):
return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )
coche = Coche("azul", 150, 4, 1200)
print(coche)