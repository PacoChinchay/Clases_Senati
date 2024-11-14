productos = []

def cargar_productos():
    cantidad_productos = input("Ingrese la cantidad de productos [Max. 10]: ")

    if cantidad_productos.isnumeric() and int(cantidad_productos) <= 10:
        cantidad_productos = int(cantidad_productos)
        
        for i in range(1, cantidad_productos + 1):
            nombre_prod = input(f"Nombre del producto {i}: ")
            
            try:
                precio_prod = int(input(f"Precio del producto {i}: "))
                cantidad_prod = int(input(f"Cantidad de {nombre_prod}: "))
                
                if precio_prod <= 0 or cantidad_prod <= 0:
                    print("Error: El precio y la cantidad deben ser positivos.")
                    continue
                
                producto = {
                    "nombre": nombre_prod,
                    "precio": precio_prod,
                    "cantidad": cantidad_prod
                }
                productos.append(producto)
                
            except ValueError:
                print("Error: El precio y la cantidad deben ser números enteros.")
                continue

        print("Productos cargados exitosamente")
    else:
        print("Error: Ingrese un número válido de productos (1-10).")

def vista_previa(productos):
    if not productos:
        print("No hay productos cargados.")
        return

    print("\nVista Previa de Productos")
    print("***************************")
    print("Nombre       | Precio Unitario | Cantidad | Subtotal")
    print("-----------------------------------------------")

    total_productos = 0
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        total_productos += 1
        
        print(f"{nombre:<12} | {precio:<14} | {cantidad:<8} | {subtotal:<8}")

    print("-----------------------------------------------")
    print(f"Cantidad de productos: {total_productos}")
    print("\nNota: Esta vista previa no incluye IGV u otros cargos adicionales de una factura oficial.")

def generar_factura(productos):
    if not productos:
        print("No hay productos cargados.")
        return

    cliente = input("Ingrese nombre del cliente: ")
    ruc = input("Ingrese n° RUC: ")

    print("\nPeru Delivery")
    print("****************************************************")
    print(f"Cliente: {cliente}")
    print(f"RUC: {ruc}")
    print("****************************************************")
    print("Cantidad | Descripción    | Valor Unitario | Importe")
    print("----------------------------------------------------")

    subtotal_general = 0
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        subtotal_general += subtotal
        
        print(f"{cantidad:<8} | {nombre:<14} | {precio:<14} | {subtotal:<8}")

    igv = round(subtotal_general * 0.18, 2)
    subtotal_general_sin_igv = subtotal_general - igv
    total = subtotal_general_sin_igv + igv

    print("----------------------------------------------------")
    print(f"{'Subtotal sin IGV:':>37} S/ {subtotal_general_sin_igv:.2f}")
    print(f"{'IGV (18%):':>37} S/ {igv:.2f}")
    print(f"{'Total a pagar:':>37} S/ {total:.2f}")
    print("****************************************************")

def mostrar_menu():
    print("\n*************************")
    print("      Peru Delivery      ")
    print("*************************")
    print("[1] Cargar Productos")
    print("[2] Vista Previa")
    print("[3] Generar Factura")
    print("[0] Salir")

def main():
    while True: 
        mostrar_menu()
        
        opcion = input("\nOperación a realizar: ")
        print("*************************")

        
        if opcion.isnumeric() and int(opcion) in range(0, 4):
            opcion = int(opcion)
            
            if opcion == 1:
                cargar_productos()
            elif opcion == 2:
                vista_previa(productos=productos)
            elif opcion == 3:
                generar_factura(productos=productos)
            elif opcion == 0:
                print("\nSaliendo del Sistema")
                break
        else:
            print("\nError: ingrese una opción válida\n")

main()