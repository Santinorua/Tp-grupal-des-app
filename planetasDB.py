import sqlite3

from g4b import Database


class PlanetaDB:
    def __init__(self):
        self.db = Database()

    def query_create_planeta(self, planeta):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO planetas (nombre_planeta, distancia_al_sol, tipo_atmosfera, id_nave_asignada) VALUES (?, ?, ?, ?)",
            (planeta.nombre, planeta, planeta.distanciaAlSol, planeta.idNaveAsignada),
        )
        planeta.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return planeta.id

    def query_read_all_planetas(self):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM planetas")
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def query_read_planetas_con_nave(self, idNaveAsignada):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT p.id,
                       p.nombre_planeta,
                       p.distancia_al_sol,
                       p.tipo_atmosfera,
                       n.nombre_nave AS nave_asignada
                FROM planetas p
                LEFT JOIN naves n ON p.id_nave_asignada = n.id
                WHERE p.id_nave_asignada = ?
            """,
            (idNaveAsignada,),
        )
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def query_update_planeta(self, planeta, id):
        conn = self.db.conectar()
        cursor = conn.cursor()
        cursor.execute(
            """"
            UPDATE planetas SET nombre_planeta = ?, distancia_al_sol = ?, tipo_atmosfera = ?, id_nave_asignada = ? WHERE id = ?"
            """,
            (
                planeta.nombre,
                planeta.distanciaAlSol,
                planeta.tipoAtmosfera,
                planeta.idNaveAsignada,
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
