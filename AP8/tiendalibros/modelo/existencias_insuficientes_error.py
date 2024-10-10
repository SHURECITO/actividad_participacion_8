from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro, cantidad_a_comprar):
        super().__init__(libro)
        self.cantidad_a_comprar = cantidad_a_comprar

    def __str__(self):
        return (f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} no tiene suficientes existencias "
                f"para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}")