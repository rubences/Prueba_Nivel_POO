from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta


if __name__ == "__main__":
    mi_vehiculo = Coche("Rojo", 4, 180, 2000)
    print(mi_vehiculo)
    mi_vehiculo2 = Bicicleta("Azul", 4, 150, 1200)
    print (mi_vehiculo2)
    mi_vehiculo3 = Camioneta("Ford", "Fiesta", 1000)
    print (mi_vehiculo3)
    
