# Nuestra "base de datos" en memoria: una lista de productos
inventario = [
    {
        "id": 1,
        "nombre": "Laptop Pro",
        "precio": 1500.99,
        "stock": 15
    },
    {
        "id": 2,
        "nombre": "Mouse Inalámbrico",
        "precio": 25.50,
        "stock": 100
    },
    {
        "id": 3,
        "nombre": "Teclado Mecánico",
        "precio": 89.90,
        "stock": 50
    },
    {
        "id": 4,
        "nombre": "Monitor",
        "precio": 120.59,
        "stock": 15
    }
]

# Usamos un bucle 'for' para recorrer la lista e imprimir cada producto
print("--- Inventario Completo de Mini-Mercado ---")
for producto in inventario:
    # Usamos f-strings, una forma moderna y fácil de formatear texto
    print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['stock']}")