from enum import Enum


class Atmosfera(Enum):
    TROPOSFERA = 12
    ESTRATOSFERA = 50
    MESOSFERA = 80
    TERMOSFERA = 300
    EXOSFERA = 500


class Planeta:
    def __init__(self, nombre, distanciaAlSol, tipoAtmosfera, idNaveAsignada):
        if not nombre:
            raise ValueError("El nombre del planeta es inválido")
        self.nombre = nombre
        if distanciaAlSol <= 0:
            raise ValueError("La distancia al sol es inválida")
        self.distanciaAlSol = distanciaAlSol
        if isinstance(tipoAtmosfera, Atmosfera):
            raise ValueError("El tipo de atmósfera es inválido")
        self.tipoAtmosfera = tipoAtmosfera
        self.idNaveAsignada = idNaveAsignada
        idNaveAsignada = None

    def esHabitable(self):
        if 142_000_000 < self.distanciaAlSol and self.distanciaAlSol < 250_000_000:
            return True
        return False

    def temperaturaAproximada(self):
        return self.tipoAtmosfera / (self.distanciaAlSol / 10_000_000)
