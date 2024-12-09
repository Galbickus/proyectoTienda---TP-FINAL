import sqlite3

#CREAR LA BASE DATOS Y LA TABLA DE PRODUCTOS.

def inicializar_bbdd():
    conexion= sqlite3.connect("C:\\Users\\ASUS\\Desktop\\proyectoTienda - TP FINAL\\inventario.db")
    cursor= conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Código TEXT UNIQUE,
            Nombre TEXT NOT NULL,
            Descripción TEXT,
            Cantidad INTEGER NOT NULL CHECK(cantidad >= 0),
            Precio REAL NOT NULL CHECK(precio > 0),
            Categoria TEXT
        )
    ''')

    conexion.commit()
    conexion.close()
