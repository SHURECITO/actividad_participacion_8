import sys
from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class UIConsola:

    def __init__(self):
        self.tienda_libros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        print("\n¡Tienda de Libros!")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print("4. Salir")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar: ")
        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print(f"El libro con ISBN {isbn} ha sido retirado del carrito.")
        except Exception as e:
            print(f"Error al retirar el libro: {str(e)}")

    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea agregar: ")
        cantidad = int(input("Ingrese la cantidad de unidades: "))
        try:
            self.tienda_libros.agregar_libro_a_carrito(isbn, cantidad)
            print(f"{cantidad} unidades del libro con ISBN {isbn} han sido agregadas al carrito.")
        except LibroAgotadoError as e:
            print(f"Error: {str(e)}")
        except ExistenciasInsuficientesError as e:
            print(f"Error: {str(e)}")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

    def adicionar_un_libro_a_catalogo(self):
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        existencias = int(input("Ingrese la cantidad de existencias: "))
        try:
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"El libro '{titulo}' ha sido agregado al catálogo.")
        except LibroExistenteError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")