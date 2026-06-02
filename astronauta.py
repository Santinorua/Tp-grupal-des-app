from enum import Enum


class Rango(Enum):
    PILOTO = 1,
    ESPECIALISTA = 1.5,
    COMANDANTE = 1.75,


class Astronauta:
    SALARIO_BASE = 104000
    VET_HORAS_DE_VUELO = 80
    MULT_HORAS_DE_VUELO = 0.10

    def __init__(self, nombre: str, apellido: str, rango: Rango, horas_de_vuelo: int, nave: str):
        self.nombre = nombre
        self.apellido = apellido
        self.rango = rango
        self.horas_de_vuelo = horas_de_vuelo
        self.nave_id = nave

    def is_veteran(self) -> bool:
        return self.horas_de_vuelo >= Astronauta.VET_HORAS_DE_VUELO

    def is_rookie(self) -> bool:
        return self.horas_de_vuelo == 0

    def salary(self) -> int:
        return int(Astronauta.SALARIO_BASE * self.rango.value[0] + Astronauta.MULT_HORAS_DE_VUELO * self.horas_de_vuelo)
