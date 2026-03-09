productos = []

def agregar_producto():
    Nombre = input("Ingresa el nombre del producto: ")
    Precio = int(input("Ingresa el precio del producto: "))
    Cantidad = int(input("Ingrese la cantidad del producto: "))
    almacena = {
        "Nombre": Nombre,
        "Precio": Precio,
        "Cantidad": Cantidad
    }
    productos.append(almacena)
    print("Se agrego correctamente")
   
def listar_Productos():
    print("\n" + "="*65)
    print(f"{'Nombre':<15} | {'Precio':<6} | {'Cantidad':<10}")
    print("-" * 65)
    for p in productos:
        Nombre = p["Nombre"]
        Precio = p["Precio"]
        Cantidad = p["Cantidad"]
        
        print(f"{Nombre:<15} | {Precio:<6} | {Cantidad:<10.2f} ")
    print("="*65 + "\n")