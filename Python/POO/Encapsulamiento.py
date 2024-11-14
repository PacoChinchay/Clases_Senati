class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()

print(e.atributo_publico())  # Llama al método público que devuelve el atributo privado
e.metodo_publico()           # Llama al método público que ejecuta el método privado
