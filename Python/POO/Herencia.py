class Producto:
    def __init__(self, ref, nombre, precio, descripcion):
        self.referencia = ref
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f"Referencia  :\t{self.referencia}\n" \
               f"Nombre      :\t{self.nombre}\n" \
               f"Precio venta:\t{self.precio}\n" \
               f"Descripcion :\t{self.descripcion}\n"
      
class Adorno(Producto):
    pass

class Alimento(Producto):
    def __init__(self, ref, nombre, precio, descripcion, productor, distribuidor):
        super().__init__(ref, nombre, precio, descripcion)
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        return f"Referencia  :\t{self.referencia}\n" \
               f"Nombre      :\t{self.nombre}\n" \
               f"Precio venta:\t{self.precio}\n" \
               f"Descripcion :\t{self.descripcion}\n" \
               f"Productor   :\t{self.productor}\n" \
               f"Distribuidor:\t{self.distribuidor}\n"
    
class Libro(Producto):
    def __init__(self, ref, nombre, precio, descripcion, isbn, autor):
        super().__init__(ref, nombre, precio, descripcion)
        self.isbn = isbn
        self.autor = autor

    def __str__(self):
        return f"Referencia  :\t{self.referencia}\n" \
               f"Nombre      :\t{self.nombre}\n" \
               f"Precio venta:\t{self.precio}\n" \
               f"Descripcion :\t{self.descripcion}\n" \
               f"Isbn        :\t{self.isbn}\n"\
               f"Autor       :\t{self.autor}\n"

adorno = Adorno("A001", "Vaso decorativo", 25.50, "Un vaso de cerámica decorativo")
print(adorno)

alimento = Alimento("A002", "Arroz", 15.75, "Arroz integral", "Productor XYZ", "Distribuidor ABC")
print(alimento)

libro = Libro("L001", "El gran libro de Python", 29.99, "Un libro completo sobre Python para todos los niveles.", "978-3-16-148410-0", "Juan Pérez")
print(libro)