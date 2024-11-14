import csv
import os

ARCHIVO = "agenda.csv"
CAMPOS = ["Nombre", "Apellido", "Telefono", "Cumpleaños"]

def leer_datos(archivo):
    datos = []
    try:
        with open(archivo, mode='r') as abierto:
            datos_csv = csv.reader(abierto)
            next(datos_csv) 
            for elemento in datos_csv:
                datos.append(elemento)
    except FileNotFoundError:
        print(f"Archivo '{archivo}' no encontrado. Creando uno nuevo.")
    return datos

def guardar_datos(datos, archivo):
    with open(archivo, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(CAMPOS) 
        writer.writerows(datos) 

def leer_busqueda():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    return nombre, apellido

def buscar(nombre, apellido, datos):
    for elemento in datos:
        if nombre in elemento[0] and apellido in elemento[1]:
            return elemento
    return None

def menu_alta(nombre, apellido, datos):
    print(f"No se encuentra {nombre} {apellido} en la agenda.")
    confirmacion = input("¿Desea ingresarlos (s/n)? ")
    if confirmacion.lower() != "s":
        return
    telefono = input("Telefono: ")
    cumpleanos = input("Cumpleaños: ")
    datos.append([nombre, apellido, telefono, cumpleanos])

def mostrar_elemento(elemento):
    print(f"{elemento[0]} {elemento[1]}")
    print(f"Telefono: {elemento[2]}")
    print(f"Cumpleaños: {elemento[3]}")

def menu_elemento():
    opcion = input("b: borrar, m: modificar, Enter continuar (b/m): ")
    return opcion.lower()

def modificar(viejo, nuevo, datos):
    indice = datos.index(viejo)
    datos[indice] = nuevo

def menu_modificacion(elemento, datos):
    nombre = input("Nuevo Nombre: ")
    apellido = input("Nuevo Apellido: ")
    telefono = input("Nuevo Telefono: ")
    cumpleanos = input("Nuevo Cumpleaños: ")
    modificar(elemento, [nombre, apellido, telefono, cumpleanos], datos)

def baja(elemento, datos):
    datos.remove(elemento)

def confirmar_salida():
    confirmacion = input("¿Desea salir (s/n)? ")
    return confirmacion.lower() == "s"

def agenda():
    datos = leer_datos(ARCHIVO)
    fin = False
    while not fin:
        os.system("cls" if os.name == "nt" else "clear")
        nombre, apellido = leer_busqueda()
        if nombre == "" and apellido == "":
            fin = confirmar_salida()
            continue
        elemento = buscar(nombre, apellido, datos)
        if not elemento:
            menu_alta(nombre, apellido, datos)
            continue
        mostrar_elemento(elemento)
        opcion = menu_elemento()
        if opcion == "m":
            menu_modificacion(elemento, datos)
        elif opcion == "b":
            baja(elemento, datos)
    guardar_datos(datos, ARCHIVO)

agenda()
