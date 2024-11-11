import os
import pickle

def escribir_datos_binario(archivo):
    cantidad_obreros = int(input("Defina la cantidad de obreros que desea ingresar al sistema: "))
    
    for num in range(1, cantidad_obreros + 1):
        codigo_obrero = f"EMP{num}"
        nombre_obrero = input("Nombre completo: ")
        fecha_obrero = input("Fecha de nacimiento (dd/mm/aaaa): ")
        cargo_obrero = input("Cargo: ")
        sueldo_obrero = input("Sueldo: ")

        obrero = {
            "codigo": codigo_obrero,
            "nombre": nombre_obrero,
            "fecha_nacimiento": fecha_obrero,
            "cargo": cargo_obrero,
            "sueldo": sueldo_obrero
        }

        pickle.dump(obrero, archivo)

ruta = os.path.dirname(os.path.abspath(__file__)) + "\\"
nombre_archivo = "empleados.dat"

print("Ruta del archivo:", ruta)

try:
    with open(ruta + nombre_archivo, "wb") as archivo:
        escribir_datos_binario(archivo)
    print(f"Los datos de los empleados han sido guardados en {ruta + nombre_archivo}")
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se pudo escribir.")
