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
    
# inicializar_bbdd()
# una vez creada la bbdd borramos el llamado a la función inicializar

#CREACIÓN DEL MENÚ DE OPCIONES.
def mostrar_menu():
    """Muestra el menú principal."""
    print("Menú para la Gestión de Productos:\n")
    print("1. Registro: Alta de productos nuevos.")
    print("2. Búsqueda: Consulta de datos de un producto específico.")
    print("3. Actualización: Modificar los datos de un producto.")
    print("4. Eliminación: Dar de baja productos.")
    print("5. Listado: Listado completo de los productos en la base de datos.")
    print("6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
    print("7. Salir.")
