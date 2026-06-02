import sqlite3 as sql

class Database:
    def __init__(self, db_name="base.db"):
        self.db_name = db_name
        
    def conectar(self):
        conexion = sql.connect(self.db_name)
        conexion.execute("PRAGMA foreign_keys = ON;")
        return conexion


    def crear_base_espacial():
        conexion = sql.connect('agencia_espacial.db')
        cursor = conexion.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS naves (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_nave TEXT NOT NULL,
                modelo TEXT,
                capacidad_pasajeros INTEGER
            );
            CREATE TABLE IF NOT EXISTS astronautas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                rango TEXT, -- Comandante, Especialista, Piloto
                horas_vuelo INTEGER,
                id_nave INTEGER,
                FOREIGN KEY (id_nave) REFERENCES naves (id)
            );
            CREATE TABLE IF NOT EXISTS planetas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_planeta TEXT NOT NULL,
                distancia_al_sol REAL, -- En UA (Unidades Astronómicas)
                tipo_atmosfera TEXT,
                id_nave_asignada INTEGER,
                FOREIGN KEY (id_nave_asignada) REFERENCES naves (id)
            )
            
        ''')
        naves_iniciales = [
            ('Odyssey I', 'Exploradora', 5),
            ('Galactic Titan', 'Carguero', 20),
            ('Star Voyager', 'Interceptor', 2)
        ]
        
        cursor.executemany('INSERT INTO naves (nombre_nave, modelo, capacidad_pasajeros) VALUES (?, ?, ?)', naves_iniciales)

        conexion.commit()
        conexion.close()
        print("Base de datos 'agencia_espacial.db' creada exitosamente.")