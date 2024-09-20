from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta


if __name__ == "__main__":
    mi_vehiculo = Coche("Rojo", 4, 180, 2000)
    print(mi_vehiculo)
    mi_vehiculo2 = Bicicleta("Azul", "Montaña", "Azul", "Deportiva")
    print(mi_vehiculo2)
    mi_vehiculo3 = Camioneta("Ford", "Fiesta", 1000)
    print (mi_vehiculo3)
    mi_vehiculo4 = Motocicleta("Negra", 2, 220, 1000)
    print (mi_vehiculo4)

