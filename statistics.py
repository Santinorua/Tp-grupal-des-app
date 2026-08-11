import pandas as pd
from g4b import Database
from planetas import Planeta
from planetasDB import PlanetaDB
import sqlite3 as sql



def submit_nuevos_planetas():
    df = pd.read_csv("database_planetas.csv")

    db = Database()
    db.conectar()
    db.crear_base_espacial()

    planeta_db = PlanetaDB()

    connection = sql.connect(db.db_name)
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM planetas')
    if cursor.fetchone()[0] == 0:
        for index, row in df.iterrows():
                planeta = Planeta(
                    nombre=row["nombre_planeta"],
                    distanciaAlSol=row["distancia_al_sol"],
                    tipoAtmosfera=row["tipo_atmosfera"],
                    idNaveAsignada=row["id_nave_asignada"]
                )
                planeta_db.query_create_planeta(planeta)