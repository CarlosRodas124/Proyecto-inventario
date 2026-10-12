from tabulate import tabulate
from datetime import datetime
from bitacora import registrar_bitacora
#registra una venta
def registro_venta():
    producto = input("Ingrese el nombre del producto que desea vender: ").lower()
    cantidad_vendida = int(input("Ingrese la cantidad que desea vender: "))
    precio_vendido = float(input("Ingrese el precio del producto que desea vender: "))

    inventario = []
    encontrado = False

    # Leer inventario principal
    with open("inventario.txt", "r", encoding="utf-8") as inv:
        for linea in inv:
            nombre, cantidad_stock, precio_stock = linea.strip().split(",")
            inventario.append([nombre, int(cantidad_stock), precio_stock])

    # Buscar producto y validar stock
    for item in inventario:
        if item[0] == producto:
            encontrado = True
            if cantidad_vendida <= item[1]:
                item[1] -= cantidad_vendida
                fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Registrar la venta
                with open("registro_ventas.txt", "a+", encoding="utf-8") as ventas:
                    ventas.write(f"{fecha_hora} | {producto},{cantidad_vendida},{precio_vendido}\n")

                print("Venta registrada correctamente.")
                registrar_bitacora(f"Se registro una venta de {cantidad_vendida} unidades, de {producto} a {precio_vendido} quetzales cada unidad ")

                # Reescribir inventario actualizado
                with open("inventario.txt", "w", encoding="utf-8" ) as inv:
                    for prod, cant, prec in inventario:
                        inv.write(f"{prod},{cant},{prec}\n")
            else:
                print(f"No hay stock suficiente. Disponible: {item[1]}, solicitado: {cantidad_vendida}")

    if not encontrado:
        print("Producto no encontrado en inventario.")
        
    

