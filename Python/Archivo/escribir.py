import os

def escribir_linea(archivo):
    msg = input("Escriba su mensaje (escriba 'salir' para terminar): ")
    while msg.lower() != "salir":
        archivo.write(msg + "\n")
        msg = input("Escriba su mensaje (escriba 'salir' para terminar): ")

ruta = os.path.dirname(os.path.abspath(__file__)) + "\\"
nombre_archivo = "archivo.txt"

print("Ruta del archivo:", ruta)

try:
    with open(ruta + nombre_archivo, "w", encoding="utf-8") as archivo:
        escribir_linea(archivo)
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encuentra en la ruta especificada.")
