import sqlite3

def crear_base_espacial():
    # Conexión (si no existe, se crea el archivo)
    conexion = sqlite3.connect('agencia_espacial.db')
    cursor = conexion.cursor()

    # 1. Tabla de NAVES
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS naves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_nave TEXT NOT NULL,
            modelo TEXT,
            capacidad_pasajeros INTEGER
        )
    ''')

    # 2. Tabla de ASTRONAUTAS (Relacionada con Naves)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS astronautas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            rango TEXT, -- Comandante, Especialista, Piloto
            horas_vuelo INTEGER,
            id_nave INTEGER,
            FOREIGN KEY (id_nave) REFERENCES naves (id)
        )
    ''')

    # 3. Tabla de PLANETAS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS planetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_planeta TEXT NOT NULL,
            distancia_al_sol REAL, -- En UA (Unidades Astronómicas)
            tipo_atmosfera TEXT,
            id_nave_asignada INTEGER,
            FOREIGN KEY (id_nave_asignada) REFERENCES naves (id)
        )
    ''')

    # Datos de ejemplo iniciales
    naves_iniciales = [
        ('Odyssey I', 'Exploradora', 5),
        ('Galactic Titan', 'Carguero', 20),
        ('Star Voyager', 'Interceptor', 2)
    ]
    
    cursor.executemany('INSERT INTO naves (nombre_nave, modelo, capacidad_pasajeros) VALUES (?, ?, ?)', naves_iniciales)

    conexion.commit()
    conexion.close()
    print("Base de datos 'agencia_espacial.db' creada exitosamente.")

