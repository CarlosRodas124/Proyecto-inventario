from datetime import datetime
from tabulate import tabulate 
from agregar_producto import agregar_producto
from buscar_producto import buscar_producto
from registro_venta import registro_venta
from muestra_inventario import mostrar_inventario
from reporte_ventas import reporte_ventas
from bitacora import registrar_bitacora


while True:
    opcion = input(
        "\n --- MENÚ PRINCIPAL---\n"
        "Escribe la acción que desea realizar.\n"
        "agregar | buscar | mostrar inventario | vender | reporte ventas | salir \n\n"
        ).lower().strip()
    if opcion == "agregar":
        agregar_producto()
    elif opcion == "buscar":
        buscar_producto()
    elif opcion == "mostrar inventario":
        mostrar_inventario()
    elif opcion == "vender":
        registro_venta()
    elif opcion == "reporte ventas":
        reporte_ventas()
    elif opcion == "salir":
        print(" Saliendo del programa ")
        break
    else:
        print (" Accion invalida. Intente de nuevo")