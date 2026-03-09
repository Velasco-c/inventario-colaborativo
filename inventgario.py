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
   
    