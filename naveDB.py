import sqlite3
from g4b import Database

class NaveDB:
    def __init__(self):
        self.db = Database()
        

    def query_create_nave(self, nave):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO naves (nombre_nave, modelo, capacidad_pasajeros) VALUES (?, ?, ?)', (nave.nombre_nave, nave.modelo, nave.capacidad_pasajeros))
        nave.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return nave.id

    def query_read_all_naves(self):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM naves')
        data = cursor.fetchall()
        conn.commit()
        conn.close()
        return data

    def query_read_one_nave(self, id):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM naves WHERE id = ?', (id))
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def query_update_nave(self, id, nave):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute('UPDATE naves SET nombre_nave = ?, modelo = ?, capacidad_pasajeros = ? WHERE id = ?', (nave.nombre_nave, nave.modelo, nave.capacidad_pasajeros, id))
        conn.commit()
        conn.close()

    def query_delete_nave(self, id):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM naves WHERE id = ?', (id))
        conn.commit()
        conn.close()

