"""Ejercicio 1: Control de Inventario y Precios (Encapsulamiento y @property)"""
import warnings

PRECIO_MIN = 0
PRECIO_MAX = 10_000


def precio_es_valido(precio):
    es_numero = isinstance(precio, (int, float)) and not isinstance(precio, bool)
    return es_numero and PRECIO_MIN <= precio <= PRECIO_MAX


def mostrar_producto(producto):
    """Imprime el estado actual del producto."""
    print(f"{producto.nombre} | Precios: {producto.precios_historicos} "
          f"| Promedio: ${producto.precio_promedio:,.2f}")


class Producto:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__precios_historicos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precios_historicos(self):
        return list(self.__precios_historicos)

    @property
    def precio_actual(self):
        return self.__precios_historicos[-1] if self.__precios_historicos else None

    @precio_actual.setter
    def precio_actual(self, precio):
        if not precio_es_valido(precio):
            warnings.warn(f"Advertencia: {precio} no es válido "
                          f"(rango {PRECIO_MIN}-{PRECIO_MAX}). Registro sin cambios.")
            return
        self.__precios_historicos.append(precio)

    def registrar_precio(self, precio):
        self.precio_actual = precio

    @property
    def precio_promedio(self):
        if not self.__precios_historicos:
            return 0
        return sum(self.__precios_historicos) / len(self.__precios_historicos)


def main():
    producto = Producto("Teclado mecánico")

    for precio in (2500, 3000, 3500):
        producto.registrar_precio(precio)
    mostrar_producto(producto)

    for invalido in (-50, 15000, 10001):
        producto.registrar_precio(invalido)
    mostrar_producto(producto)

    producto.precio_actual = 4000
    mostrar_producto(producto)


if __name__ == "__main__":
    main()
