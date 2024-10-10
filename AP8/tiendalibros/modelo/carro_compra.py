from tiendalibros.modelo.item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.items = []

    @staticmethod
    def validar_isbn(isbn):
        if not isbn or not isinstance(isbn, str):
            raise ValueError("El ISBN debe ser una cadena válida no vacía.")
    
    @staticmethod
    def validar_cantidad(cantidad):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")
    
    @staticmethod
    def validar_precio(precio):
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
    
    def agregar_item(self, libro, cantidad):
        try:
            self.validar_isbn(libro.isbn)
            self.validar_precio(libro.precio)
            self.validar_cantidad(cantidad)

            for item in self.items:
                if item.libro.isbn == libro.isbn:
                    item.cantidad += cantidad
                    return item

            nuevo_item = ItemCompra(libro, cantidad)
            self.items.append(nuevo_item)
            return nuevo_item
        
        except ValueError as ve:
            print(f"Error de validación al agregar el libro: {str(ve)}")
        except Exception as e:
            print(f"Error inesperado al agregar el libro: {str(e)}")
    
    def quitar_item(self, isbn):
        try:
            self.validar_isbn(isbn)
            self.items = [item for item in self.items if item.libro.isbn != isbn]
        
        except Exception as e:
            print(f"Error al quitar el libro: {str(e)}")

    def calcular_total(self):
        try:
            return sum(item.calcular_subtotal() for item in self.items)
        except Exception as e:
            print(f"Error al calcular el total: {str(e)}")
            return 0

    def mostrar_items(self):
        try:
            if not self.items:
                print("El carrito está vacío.")
                return
            
            for item in self.items:
                print(f"ISBN: {item.libro.isbn}, Título: {item.libro.titulo}, "
                      f"Cantidad: {item.cantidad}, Precio: {item.libro.precio}, Subtotal: {item.calcular_subtotal()}")
            print(f"\nTotal: {self.calcular_total()} monedas.")
        
        except Exception as e:
            print(f"Error al mostrar los items del carrito: {str(e)}")
    
    def vaciar_carrito(self):
        try:
            self.items.clear()
        except Exception as e:
            print(f"Error al vaciar el carrito: {str(e)}")