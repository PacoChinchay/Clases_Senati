from copy import copy

class Test:
    pass

# Crear la instancia original
test1 = Test()
# Crear una copia superficial de test1
test2 = copy(test1)

# Agregar un atributo al objeto test1
test1.mensaje = "Programación en Python"

# Comparación por referencia
print(test1 == test2)  # Esto imprimirá False porque son objetos diferentes

# Intentar acceder al atributo mensaje en test2
try:
    print(test2.mensaje)  # Esto funcionará porque es una copia superficial
except Exception as e:
    print(e)
