from tabulate import tabulate
from datetime import datetime
from bitacora import registrar_bitacora
#busca un producto 

def buscar_producto():
    producto = input("Ingrese el producto que desea buscar ").lower().strip()
    resultado = []
    
    with open ("inventario.txt", "r", encoding="utf-8") as inventario:
        for linea in inventario:
            nombre, cantidad, precio = linea.strip().split(",")
            if producto in nombre.lower():
                resultado.append((nombre, cantidad, precio))
    if resultado: 
        print(tabulate(resultado, headers=["Producto", "Cantidad", "Precio"]))
        registrar_bitacora(f"Se busco un producto producto{producto}")
    else:
        print("No se encontro ningun producto vuelva a intentarlo ")
        
        registrar_bitacora(f"Se busco un producto {producto}")
        
