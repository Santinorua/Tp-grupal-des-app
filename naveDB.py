import sqlite3


conexion = sqlite3.connect('agencia_espacial.db')
cursor = conexion.cursor()

def query_create_nave(nave):
    cursor.execute('INSERT INTO naves (nombre_nave, modelo, capacidad_pasajeros) VALUES (?, ?, ?)', (nave.nombre_nave, nave.modelo, nave.capacidad_pasajeros))
    conexion.commit()

def query_read_all_naves():
    cursor.execute('SELECT * FROM naves')
    return cursor.fetchall()

def query_read_one_nave(id):
    cursor.execute('SELECT * FROM naves WHERE id = ?', (id))
    return cursor.fetchone()

def query_update_nave(id, nave):
    cursor.execute('UPDATE naves SET nombre_nave = ?, modelo = ?, capacidad_pasajeros = ? WHERE id = ?', (nave.nombre_nave, nave.modelo, nave.capacidad_pasajeros, id))
    conexion.commit()

def query_delete_nave(id):
    cursor.execute('DELETE FROM naves WHERE id = ?', (id))
    conexion.commit()

