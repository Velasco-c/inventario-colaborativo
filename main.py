from inventgario import *

def menu_principal(): 
    menu = """ 
    1. Agregar producto 
    2.  Listar producto 
    3.  Salir
    """
    print(menu) 
    
while True: 
    menu_principal()
    opc = int(input("Ingrese alguna de las opciones: "))
    
    if opc == 3:
        print("BYE bye ")
        break
    elif opc == 1: 
        agregar_producto()
    elif opc == 2: 
        listar_Productos()
    else: 
        print("opcion invalida")