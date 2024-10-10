from .carro_compra import CarroCompras
from .libro import Libro
from .libro_existente_error import LibroExistenteError
from .libro_agotado_error import LibroAgotadoError
from .existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(self.catalogo[isbn])
        
        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro

    def agregar_libro_a_carrito(self, isbn, cantidad):
        if isbn not in self.catalogo:
            raise ValueError(f"No se encontró ningún libro con ISBN {isbn} en el catálogo")
        
        libro = self.catalogo[isbn]
        
        if libro.existencias == 0:
            raise LibroAgotadoError(libro)
        
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro, cantidad)

        libro.existencias -= cantidad
        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)