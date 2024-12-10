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
# FUNCION REGISTRAR PRODUCTOS
def registrar_producto():
    print("\n --- Registro de Producto Nuevo ---")

    nombre= input("Nombre del producto:").strip()
    descripcion= input("Descripción del producto:").strip()

    while True:    
        try:
            precio= float(input("Precio del producto:"))
            if precio > 0:
                break
            else:
                print("Entrada inválida. Debe ingresar un número decimal mayor a 0.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un valor numérico decimal mayor a 0.")

    while True:
        try:
            cantidad= int(input(f"Cantidad en stock de {nombre}:"))
            if cantidad >= 0:
                break
            else:
                print("Entrada inválida. El stock no puede ser negativo.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un valor numérico entero mayor a 0.")

    categoria= input("Categoría del producto:").strip()

    conexion= sqlite3.connect("C:\\Users\\ASUS\\Desktop\\proyectoTienda - TP FINAL\\inventario.db")
    cursor= conexion.cursor()

    try:
        cursor.execute('''
            INSERT INTO productos (Código, Nombre, Descripción, Cantidad, Precio, Categoria)
            
            VALUES (NULL, ?, ?, ?, ?, ?)''',
            (nombre, descripcion, cantidad, precio, categoria)
        )

        id_producto= cursor.lastrowid
        codigo= f"PROD{id_producto}"

        cursor.execute('''
        UPDATE productos SET Código = ? WHERE id = ?''',
        (codigo, id_producto))

        conexion.commit()
        print(f"Producto registrado con éxito. Código asignado: {codigo}")

    except sqlite3.IntegrityError:
        print("Error. No se pudo registrar el producto.")

    finally:
        conexion.close()


# FUNCION BUSCAR UN PRODUCTO POR CODIGO (opcion2)
def buscar_producto():
    print("\n --- Busqueda de Producto ---")
    codigo= input("Ingrese el código del producto que desea buscar: ").strip()
    
    conexion= sqlite3.connect("C:\\Users\\ASUS\\Desktop\\proyectoTienda - TP FINAL\\inventario.db")
    cursor= conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE Código= ?",(codigo,))
    producto= cursor.fetchone()
    
    conexion.close()
    
    if producto:
        _, codigo, nombre, descripcion, cantidad, precio, categoria =producto
        print(f"\nProducto encontrado con el código: {codigo}")
        print(f"Nombre      :   {nombre}")
        print(f"Descripcion :   {descripcion}")
        print(f"Cantidad    :   {cantidad}")
        print(f"Precio      :   $ {precio}")
        print(f"Categoría   :   {categoria}")
    else:
        print(f"No se encontró el producto registrado bajo el código: {codigo}")

# FUNCION LISTAR PRODUCTOS(opcion 5)
def listar_productos():
    print("\n --- LISTA DE PRODUCTOS ---")
    conexion= sqlite3.connect("C:\\Users\\ASUS\\Desktop\\proyectoTienda - TP FINAL\\inventario.db")
    cursor= conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos= cursor.fetchall()
    conexion.close()
    
    if not productos:
        print("El inventario está vacío.")
    else:
        for _, codigo, nombre, descripcion, cantidad, precio, categoria in productos:
            print(f"\nCódigo:           {codigo}")
            print(f"Nombre:         {nombre}")
            print(f"Descripcion:    {descripcion}")
            print(f"Cantidad:       {cantidad}")
            print(f"Precio:         $ {precio}")
            print(f"Categoría:      {categoria}")
            print("\n ------\n")       



#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    inicializar_bbdd()

    while True:
        mostrar_menu()

        try:
            opcion= int(input("Seleccione una opción (1-7):"))

            if opcion == 7:
                print("Saliendo del sistema. ¡Hasta pronto!")
                break
            elif opcion == 1:
                registrar_producto()
            elif opcion == 2:
                buscar_producto()
            elif opcion == 5:
                listar_productos()
            else:
                print("Opción no váida. Por favor, seleccione entre 1 y 7.")
        except ValueError: 
            print("Opción no válida. Por favor, ingrese un valor numérico.")