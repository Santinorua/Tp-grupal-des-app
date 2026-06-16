from astronauta import Astronauta
from g4b import Database

query_update_astronauta = "UPDATE astronautas SET nombre = ?, apellido = ?, rango = ?, horas_vuelo = ?, id_nave = ? WHERE id = ?"
query_delete_astronauta = "DELETE FROM astronautas WHERE id = ?"


class AstronautaDB:
    def __init__(self):
        self.db = Database()

    def query_create_astronauta(self, astronauta: Astronauta):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO astronautas (nombre, apellido, rango, horas_vuelo, id_nave) VALUES (?, ?, ?, ?, ?)",
            (astronauta.nombre, astronauta.apellido, astronauta.rango.name, astronauta.horas_de_vuelo, astronauta.nave_id)
        )
        astronauta.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return astronauta.id

    def query_read_all_astronautas(self):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM astronautas")
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def query_read_astronautas_con_nave(self):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
                """
                SELECT * FROM astronautas WHERE id_nave IS NOT NULL
                """
        )
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def query_update_astronauta(self, astronauta: Astronauta, id):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
                "UPDATE astronautas SET nombre = ?, apellido = ?, rango = ?, horas_vuelo = ?, id_nave = ? WHERE id = ?"
                (
                astronauta.nombre,
                astronauta.apellido,
                astronauta.rango,
                astronauta.horas_de_vuelo,
                astronauta.id,
                id,
            ),
        )
        conn.commit()
        conn.close()

    def query_delete_planeta(self, id):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM planetas WHERE id = ?", (id))
        conn.commit()
        conn.close()
