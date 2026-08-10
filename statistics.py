import pandas as pd
from g4b import Database
from planetas import Planeta
from planetasDB import PlanetaDB


def submit_nuevos_planetas():
    df = pd.read_csv("database_planetas.csv")

    db = Database()
    db.conectar()
    db.crear_base_espacial()

    planeta_db = PlanetaDB()

    for index, row in df.iterrows():
        planeta = Planeta(
            nombre=row["nombre_planeta"],
            distanciaAlSol=row["distancia_al_sol"],
            tipoAtmosfera=row["tipo_atmosfera"],
            idNaveAsignada=row["id_nave_asignada"]
        )
        planeta_db.query_create_planeta(planeta)

