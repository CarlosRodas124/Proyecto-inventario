from tabulate import tabulate
from bitacora import registrar_bitacora
#muestra todo el inventario
def mostrar_inventario():
    inventario = []
    with open ("inventario.txt", "r", encoding="utf-8") as inv:
        for linea in inv:
            nombre, cantidad, precio = linea.strip().split(",")
            inventario.append((nombre, int(cantidad), precio))
            
    print (tabulate(inventario, headers=["Producto", "Cantidad", "Precio"], tablefmt="grid")) 
    registrar_bitacora("Se mostro el inventario")