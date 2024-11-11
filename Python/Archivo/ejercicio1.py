import os

def escribir_linea(archivo):
    cantidad_obreros = int(input("Defina la cantidad de obreros que desea ingresar al sistema: "))
    
    num = 1  
    for _ in range(cantidad_obreros):
      codigo_obrero = f"EMP{num}"
      nombre_obrero = input("Nombre completo: ")
      fecha_obrero = input("Fecha de nacimiento (dd/mm/aaaa): ")
      cargo_obrero = input("Cargo: ")
      sueldo_obrero = input("Sueldo: ")

      linea = f"{codigo_obrero}, {nombre_obrero}, {fecha_obrero}, {cargo_obrero}, {sueldo_obrero}\n"

      archivo.write(linea)
      num += 1

ruta = os.path.dirname(os.path.abspath(__file__)) + "\\"
nombre_archivo = "empleados.txt" 

print("Ruta del archivo:", ruta)

try:
    with open(ruta + nombre_archivo, "w", encoding="utf-8") as archivo:
        escribir_linea(archivo)
    print(f"Los datos de los empleados han sido guardados en {ruta + nombre_archivo}")
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se pudo escribir.")
