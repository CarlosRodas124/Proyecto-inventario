from tabulate import tabulate
from datetime import datetime
from bitacora import registrar_bitacora
#agregar un nuevo producto al inventario 
def agregar_producto():
    nombre = input("Ingrese el nombre del producto ").lower().strip()
    cantidad = int(input("Ingrese la cantidad de producto que desea agregar" ))
    precio = float(input("Ingrese el precio del producto"))
    with open ("inventario.txt", "a+", encoding="utf-8") as inventario:
        inventario.write(f"{nombre},{cantidad},{precio}\n")
    print ("Su producto hacido agregado correctamente ")
    registrar_bitacora(f"Se agrego el Procuto{nombre} con {cantidad} unidades y un precio de {precio} quetzales ")
    
