class Nave:
    def __init__(self, nombre_nave, modelo, capacidad_pasajeros):
        self.id = None
        self.nombre_nave = nombre_nave
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros

    def entran_pasajeros(self, cantidad):
        if cantidad <= self.capacidad_pasajeros:
            return True
        else:
            return False
        
    def obtener_informacion(self):
        return f"Nave: {self.nombre_nave}, Modelo: {self.modelo}, Capacidad: {self.capacidad_pasajeros} pasajeros"
    
    def actualizar_capacidad(self, nueva_capacidad):
        self.capacidad_pasajeros = nueva_capacidad
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre_nave = nuevo_nombre


