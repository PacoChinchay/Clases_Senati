from data import clientes, cuentas, movimientos
from tabulate import tabulate

def agregar_movimiento():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    cuenta_encontrada = next((c for c in cuentas if c["numero_cuenta"] == numero_cuenta), None)
    
    if cuenta_encontrada:
        tipo_operacion = input("Ingrese el tipo de operación (Depósito/Retiro): ")
        descripcion = input("Ingrese la descripción de la operación: ")
        numero_operacion = input("Ingrese el número de operación: ")
        importe = float(input("Ingrese el importe: "))
        
        saldo_contable = cuenta_encontrada["saldo_actual"] + importe if tipo_operacion == "Depósito" else cuenta_encontrada["saldo_actual"] - importe
        
        movimiento = {
            "numero_cuenta": numero_cuenta,
            "fecha_operacion": "fecha_actual",
            "descripción": descripcion,
            "numero_operacion": numero_operacion,
            "tipo_operacion": tipo_operacion,
            "importe": importe,
            "saldo_contable": saldo_contable
        }
        
        movimientos.append(movimiento)
        cuenta_encontrada["saldo_actual"] = saldo_contable
        print("Movimiento agregado exitosamente.")
    else:
        print("Cuenta no encontrada.")

def eliminar_movimiento():
    numero_operacion = input("Ingrese el número de operación a eliminar: ")
    movimiento = next((m for m in movimientos if m["numero_operacion"] == numero_operacion), None)
    
    if movimiento:
        movimientos.remove(movimiento)
        print("Movimiento eliminado exitosamente.")
    else:
        print("Movimiento no encontrado.")

def editar_movimiento():
    numero_operacion = input("Ingrese el número de operación a editar: ")
    movimiento = next((m for m in movimientos if m["numero_operacion"] == numero_operacion), None)
    
    if movimiento:
        nuevo_tipo_operacion = input("Ingrese el nuevo tipo de operación (Depósito/Retiro): ")
        nueva_descripcion = input("Ingrese la nueva descripción de la operación: ")
        nuevo_importe = float(input("Ingrese el nuevo importe: "))
        
        saldo_contable = movimiento["saldo_contable"] + nuevo_importe if nuevo_tipo_operacion == "Depósito" else movimiento["saldo_contable"] - nuevo_importe
        
        movimiento["tipo_operacion"] = nuevo_tipo_operacion
        movimiento["descripción"] = nueva_descripcion
        movimiento["importe"] = nuevo_importe
        movimiento["saldo_contable"] = saldo_contable
        
        print("Movimiento editado exitosamente.")
    else:
        print("Movimiento no encontrado.")

def generar_reporte(cuenta):
    cuenta_encontrada = next((c for c in cuentas if c["numero_cuenta"] == cuenta), None)
    
    if cuenta_encontrada:
        cliente = next((cl for cl in clientes if cl["dni_cliente"] == cuenta_encontrada["dni_cliente"]), None)
        
        movimientos_cuenta = [m for m in movimientos if m["numero_cuenta"] == cuenta]
        
        saldo_actual = cuenta_encontrada["saldo_actual"]
        saldo_contable_acumulado = 0
        for mov in movimientos_cuenta:
            if mov["tipo_operacion"] == "Depósito":
                saldo_contable_acumulado += mov["importe"]
            elif mov["tipo_operacion"] == "Retiro":
                saldo_contable_acumulado -= mov["importe"]
            mov["saldo_contable"] = saldo_contable_acumulado

        cuenta_encontrada["saldo_actual"] = saldo_contable_acumulado

        num_depositos = sum(1 for mov in movimientos_cuenta if mov["tipo_operacion"] == "Depósito")
        num_retiros = sum(1 for mov in movimientos_cuenta if mov["tipo_operacion"] == "Retiro")

        print(f"Cliente          : {cliente['nombre_cliente']}")
        print(f"Dirección        : {cliente['direccion_cliente']}")
        print(f"Distrito         : {cliente['distrito']}")

        print(f"Número de Cuenta : {cuenta_encontrada['numero_cuenta']}")
        print(f"Tipo de Cuenta   : {cuenta_encontrada['tipo_cuenta']}")
        print(f"Moneda           : {cuenta_encontrada['moneda']}")
        print(f"Saldo Actual     : {cuenta_encontrada['saldo_actual']:.2f}\n")

        print("Movimientos :\n")
        print(f"Número de Depósitos: {num_depositos}")
        print(f"Número de Retiros  : {num_retiros}\n")

        movimientos_tabla = [
            [
                mov["numero_cuenta"],
                mov["fecha_operacion"],
                mov["descripción"],
                mov["numero_operacion"],
                mov["tipo_operacion"],
                f"{mov['importe']:.2f}",
                f"{mov['saldo_contable']:.2f}"
            ]
            for mov in movimientos_cuenta
        ]
        
        headers = ["Número Cuenta", "Fecha", "Descripción", "Nro Operación", "Tipo", "Importe", "Saldo Contable"]
        print(tabulate(movimientos_tabla, headers=headers, tablefmt="rounded_grid"))
    else:
        print("No se encontró la cuenta. Verifique el número de cuenta ingresado.")

def vista_reporte_cuenta():
    #Todo: Agregar validaciones adicionales
    nro_cuenta = input("\nIngrese número de Cuenta: ")
    generar_reporte(cuenta=nro_cuenta)

def mostrar_menu():
    print("\n*************************")
    print("    Banco Continental    ")
    print("*************************")
    print("[1] Reporte de cuenta")
    print("[2] Agregar movimiento")
    print("[3] Eliminar movimiento")
    print("[4] Editar movimiento")
    print("[0] Salir")

def main():
    while True: 
        mostrar_menu()
        
        opcion = input("\nOperación a realizar: ")
        print("*************************")

        
        if opcion.isnumeric() and int(opcion) in range(0, 5):
            opcion = int(opcion)
            
            if opcion == 1:
                vista_reporte_cuenta()
            elif opcion == 2:
                agregar_movimiento()
            elif opcion == 3:
                eliminar_movimiento()
            elif opcion == 4:
                editar_movimiento()
            elif opcion == 0:
                print("\nSaliendo del Sistema")
                break
        else:
            print("\nError: ingrese una opción válida\n")

main()