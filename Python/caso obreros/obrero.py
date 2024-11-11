class Obrero:
    def __init__(self, nombre, enero, febrero, marzo, abril, mayo, junio):
        self.nombre = nombre
        self.produccion = {
            "Enero": enero,
            "Febrero": febrero,
            "Marzo": marzo,
            "Abril": abril,
            "Mayo": mayo,
            "Junio": junio
        }

    def actualizar_produccion(self, mes, prod):
        if mes in self.produccion:
            self.produccion[mes] = prod
        else:
            print(f"Mes {mes} no válido.")

    def mostrar_informacion(self):
        produccion_mensual = "   ".join(f"{self.produccion[mes]:>5}" for mes in self.produccion)
        print(f"{self.nombre:<8} {produccion_mensual}   {self.total_obrero():>6}")

    def total_obrero(self):
        return sum(self.produccion.values())

    @staticmethod
    def total_por_mes(obreros):
        totales_por_mes = {mes: 0 for mes in obreros[0].produccion}
        for obrero in obreros:
            for mes, produccion in obrero.produccion.items():
                totales_por_mes[mes] += produccion
        return totales_por_mes

    @staticmethod
    def calcular_porcentajes(totales_por_mes):
        total_general = sum(totales_por_mes.values())
        porcentajes = {mes: (produccion / total_general * 100) for mes, produccion in totales_por_mes.items()}
        return porcentajes


class Empresa:
    def __init__(self):
        self.lista_obreros = []

    def agregar_obrero(self, obrero):
        self.lista_obreros.append(obrero)

    def eliminar_obrero(self, nombre):
        self.lista_obreros = [obrero for obrero in self.lista_obreros if obrero.nombre != nombre]

    def buscar_obrero(self, nombre):
        for obrero in self.lista_obreros:
            if obrero.nombre == nombre:
                return obrero
        print(f"Obrero {nombre} no encontrado.")
        return None

    def mostrar_todos(self):
        self.cabecera()
        for obrero in self.lista_obreros:
            obrero.mostrar_informacion()
        print("*****************************************************************\n")

    def ordenar_por_nombre(self):
        self.lista_obreros.sort(key=lambda obrero: obrero.nombre)

    def cabecera(self):
        print("\n*****************************************************************")
        print("Reporte semestral de Producción")
        print("*****************************************************************")
        print("Obrero   Enero   Febrero  Marzo    Abril   Mayo    Junio    Total")
        print("-----------------------------------------------------------------")

    def reporte_con_totales_y_porcentajes(self):
        self.cabecera()
        for obrero in self.lista_obreros:
            obrero.mostrar_informacion()

        total_mes = Obrero.total_por_mes(self.lista_obreros)
        porcentajes = Obrero.calcular_porcentajes(total_mes)

        print("\nTotales por mes:")
        for mes, total in total_mes.items():
            print(f"{mes}: {total}")

        print("\nPorcentajes por mes:")
        for mes, porcentaje in porcentajes.items():
            print(f"{mes}: {porcentaje:.2f}%")
        print("*****************************************************************")

    def reporte_por_obrero(self, obrero):
        self.cabecera()
        obrero.mostrar_informacion()
        
        total_mes = obrero.produccion
        total_general = obrero.total_obrero()
        porcentajes = {mes: (produccion / total_general * 100) for mes, produccion in total_mes.items()}

        print("\nTotales por mes para", obrero.nombre)
        for mes, total in total_mes.items():
            print(f"{mes}: {total}")

        print("\nPorcentajes por mes para", obrero.nombre)
        for mes, porcentaje in porcentajes.items():
            print(f"{mes}: {porcentaje:.2f}%")
        print("*****************************************************************")

    def reporte_grafico(self):
        for obrero in self.lista_obreros:
            print(f"\nProducción de {obrero.nombre}")
            print("Meses      | Producción")
            print("-" * 30)
            for mes, produccion in obrero.produccion.items():
                barras = "#" * int(produccion / 10)  # Ajusta el divisor para cambiar la escala
                print(f"{mes:<10} | {barras} ({produccion})")
                
        self.cabecera2()
        for obrero in self.lista_obreros:
            total = obrero.total_obrero()
            promedio = total / len(obrero.produccion)
            print(f"{obrero.nombre:<8} {total:>6}   {promedio:>6.2f}", end="   ")
            porcentaje_total = (total / sum([o.total_obrero() for o in self.lista_obreros])) * 100
            barras = "#" * int(porcentaje_total / 2)
            print(f"{barras} ({porcentaje_total:.2f}%)")
        print("*****************************************************************")

    def cabecera2(self):
        print("\nNombre   Total   Promedio   Porcentaje\n" + "-" * 50)


def menu():
    empresa = Empresa()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            lista_obreros = cargar_datos()
            for obrero in lista_obreros:
                empresa.agregar_obrero(obrero)
        
        elif opcion == "2":
            empresa.mostrar_todos()
        
        elif opcion == "3":
            empresa.reporte_con_totales_y_porcentajes()
        
        elif opcion == "4":
            empresa.ordenar_por_nombre()
            empresa.reporte_con_totales_y_porcentajes()
        
        elif opcion == "5":
            nombre = input("Ingrese el nombre del obrero: ")
            obrero = empresa.buscar_obrero(nombre)
            if obrero:
                empresa.reporte_por_obrero(obrero)
        
        elif opcion == "6":
            nombre = input("Ingrese el nombre del obrero a modificar: ")
            obrero = empresa.buscar_obrero(nombre)
            if obrero:
                mes = input("Ingrese el mes a modificar: ")
                produccion = int(input("Ingrese la nueva producción: "))
                obrero.actualizar_produccion(mes, produccion)
                empresa.reporte_por_obrero(obrero)
        
        elif opcion == "7":
            nombre = input("Ingrese el nombre del obrero a eliminar: ")
            empresa.eliminar_obrero(nombre)
            empresa.mostrar_todos()
        
        elif opcion == "8":
            empresa.reporte_grafico()
        
        elif opcion == "9":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")


def mostrar_menu():
    print("[1] Cargar datos Obreros")
    print("[2] Mostrar datos Obreros")
    print("[3] Reporte con Totales y Porcentajes")
    print("[4] Ordenar reporte por nombre")
    print("[5] Buscar y reportar un obrero específico")
    print("[6] Modificar datos del Obrero y mostrar cambios")
    print("[7] Eliminar Obrero y mostrar reporte actualizado")
    print("[8] Gráfica de producción")
    print("[9] Salir")


def cargar_datos():
    cantidad = int(input("Ingrese cantidad de obreros: "))
    obreros = []
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del obrero {i + 1}: ")
        produccion = [int(input(f"Ingrese producción para {mes}: ")) for mes in ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]]
        obreros.append(Obrero(nombre, *produccion))
    print(f"Obreros agregados de manera exitosa: {cantidad}\n")
    return obreros


if __name__ == "__main__":
    menu()
