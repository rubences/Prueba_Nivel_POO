from subclases.coche import Coche


class Camioneta(Coche):
    def __init__(self, marca, modelo, capacidad_carga, velocidad, cilindrada):
        super().__init__(marca, modelo, velocidad, cilindrada)
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return f"Camioneta(marca={self.marca}, modelo={self.modelo}, velocidad={self.velocidad}, cilindrada={self.cilindrada}, capacidad_carga={self.capacidad_carga})"