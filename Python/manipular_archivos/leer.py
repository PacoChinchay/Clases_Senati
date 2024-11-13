import os

ruta = os.path.dirname(os.path.abspath(__file__)) + "\\"
print("Ruta del archivo:", ruta)

try:
    with open(ruta + "archivo.txt", "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo, start=1):
            linea = linea.rstrip("\n")
            print(f"{i:4d}: {linea}")
except FileNotFoundError:
    print("El archivo 'archivo.txt' no se encuentra en la ruta especificada.")
