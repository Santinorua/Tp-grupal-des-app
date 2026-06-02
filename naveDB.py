import sqlite3

class NaveDB:
    def __init__(self):
        self.conexion = sqlite3.connect('agencia_espacial.db')
        self.cursor = self.conexion.cursor()

    def query_create_nave(self, nave):
        self.cursor.execute('INSERT INTO naves (nombre_nave, modelo, capacidad_pasajeros) VALUES (?, ?, ?)', (nave.nombre_nave, nave.modelo, nave.capacidad_pasajeros))
        self.conexion.commit()

    def query_read_all_naves(self):
        self.cursor.execute('SELECT * FROM naves')
        return self.cursor.fetchall()

    def query_read_one_nave(self, id):
        self.cursor.execute('SELECT * FROM naves WHERE id = ?', (id))
        return self.cursor.fetchone()

    def query_update_nave(self, id, nave):
        self.cursor.execute('UPDATE naves SET nombre_nave = ?, modelo = ?, capacidad_pasajeros = ? WHERE id = ?', (nave.nombre_nave, nave.modelo, nave.capacidad_pasajeros, id))
        self.conexion.commit()

    def query_delete_nave(self, id):
        self.cursor.execute('DELETE FROM naves WHERE id = ?', (id))
        self.conexion.commit()

