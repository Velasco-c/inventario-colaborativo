productos = []

def entero(Mensaje):
    while True:
        try:
            Numero = int(input(Mensaje))
            return Numero
        except ValueError as e:
            print(f"Tipo de error es : {e}")

def decimal(Mensaje):
    while True:
        try:
            Numero = float(input(Mensaje))
            return Numero
        except ValueError as e:
            print(f"Tipo de error es : {e}")
        
def agregar_producto():
    Productos_contenido = entero("Ingrese la cantida de productos a agregar: ")
    for i in range(0,Productos_contenido):
        Nombre = input("Ingresa el nombre del producto: ")
        Precio = decimal("Ingresa el precio del producto: ")
        Cantidad = entero("Ingrese la cantidad del producto: ")
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