from datetime import datetime

def registrar_bitacora(operacion):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("bitacora.txt", "a", encoding="utf-8") as bitacora:
        bitacora.write(f"{fecha_hora} - {operacion}\n")
        



        
        