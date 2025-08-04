# --- Base de Datos en Memoria ---
inventario = [
    { "id": 1, "nombre": "Laptop Pro", "precio": 1500.99, "stock": 15 },
    { "id": 2, "nombre": "Mouse Inalámbrico", "precio": 25.50, "stock": 100 },
    { "id": 3, "nombre": "Teclado Mecánico", "precio": 89.90, "stock": 50 }
]

# --- Funciones de la Aplicación ---

def mostrar_inventario():
    """Muestra todos los productos del inventario."""
    print("\n--- Inventario Actual ---")
    if not inventario:
        print("El inventario está vacío.")
        return
        
    for producto in inventario:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['stock']}")

def agregar_producto():
    """Pide datos al usuario y añade un nuevo producto al inventario."""
    print("\n--- Añadir Nuevo Producto ---")
    # Asignamos un ID automáticamente
    nuevo_id = inventario[-1]["id"] + 1 if inventario else 1
    
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    stock = int(input("Stock inicial: "))
    
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    
    inventario.append(nuevo_producto)
    print(f"¡Producto '{nombre}' añadido con éxito!")
    
def actualizar_stock():
    """Busca un producto por su ID y actualiza su stock."""
    try:
        id_producto = int(input("\nIngrese el ID del producto a actualizar: "))
    except ValueError:
        print("Error: El ID debe ser un número.")
        return # Salimos de la función si la entrada no es un número

    producto_encontrado = None # Usaremos esta variable para guardar el producto si lo hallamos

    # 1. Primero, buscamos el producto en todo el inventario
    for producto in inventario:
        if producto['id'] == id_producto:
            producto_encontrado = producto
            break # Si ya lo encontramos, no necesitamos seguir buscando. ¡Ahorramos tiempo!

    # 2. Después de buscar, decidimos qué hacer
    if producto_encontrado:
        # Si la variable tiene algo, significa que lo encontramos
        print(f"Producto encontrado: {producto_encontrado['nombre']} (Stock actual: {producto_encontrado['stock']})")
        try:
            nuevo_stock = int(input("Ingrese la nueva cantidad de stock: "))
            producto_encontrado['stock'] = nuevo_stock # Actualizamos el diccionario
            print("¡Stock actualizado con éxito!")
        except ValueError:
            print("Error: La cantidad de stock debe ser un número.")
    else:
        # Si después de todo el bucle, la variable sigue vacía, el producto no existe
        print(f"Error: Producto con ID {id_producto} no encontrado.")
                
def menu_principal():
    """Muestra el menú principal y maneja la entrada del usuario."""
    while True:
        print("\n--- Mini-Mercado Gestor de Inventario ---")
        print("1. Mostrar inventario")
        print("2. Añadir producto")
        print("3. Actualizar Stock")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_inventario()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            actualizar_stock()           
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# --- Punto de Entrada de la Aplicación ---
if __name__ == "__main__":
    menu_principal()