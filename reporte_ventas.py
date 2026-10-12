from tabulate import tabulate 
from datetime import datetime
from bitacora import registrar_bitacora
#genera un reporte de ventas del dia 
def reporte_ventas():
    ventas = []
    #lee el registro de ventas 
    hoy = datetime.now().strftime("%Y-%m-%d")
    with open("registro_ventas.txt", "r", encoding="utf-8") as registro_ventas:
        for linea in registro_ventas:
            fecha_hora, datos = linea.strip().split("|")
            fecha = fecha_hora.split()[0]
            if fecha == hoy:
                producto, cantidad, precio = datos.strip().split(",")
                ventas.append([producto, int(cantidad), float(precio), int(cantidad)*float(precio) ])
    #muestra el reporte de ventas del dia de hoy y lo muestra en una tabla
    if ventas:
        tabla = tabulate(ventas, headers=["Producto", "Cantidad" , "Precio", "Total"], tablefmt="grid")
        print(f"Reporte de ventas del dia de hoy {hoy}\n\n")
        print(tabla)
        

        #guarda el reporte de ventas del dia 
        with open(f"reporte_{hoy}.txt", "w", encoding="utf-8" ) as reporte:
            reporte.write(f"Reporte de ventas del dia {hoy}\n")
            reporte.write(tabla)
            registrar_bitacora(f" Se genero el reporde de ventas del dia {hoy}")
            
            
    else:
        print(f"No hay ventas registradas para el dia {hoy}")
        