"""Ejercicio 2: Cotización de Envíos (Herencia y Polimorfismo)"""


class Envio:

    def __init__(self, peso_kg, distancia_km):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base):
        return monto_base

    def __str__(self):
        return f"{type(self).__name__} ({self.peso_kg} kg, {self.distancia_km} km)"


class EnvioEstandar(Envio):

    def calcular_costo(self, monto_base):
        return monto_base * 1.05  


class EnvioExpress(Envio):

    def calcular_costo(self, monto_base):
        return monto_base * 1.15  


def crear_envios():
    """Devuelve una lista mixta de envíos."""
    return [
        EnvioEstandar(2.5, 120),
        EnvioExpress(1.0, 450),
        EnvioEstandar(10, 800),
        EnvioExpress(5.5, 60),
    ]


def cotizar_envios(envios, monto_base):
    """Recorre la lista y calcula el costo de cada envío (polimorfismo)."""
    print(f"Monto base del paquete: ${monto_base:,.2f}\n")
    for envio in envios:
        print(f"{envio} -> costo total: ${envio.calcular_costo(monto_base):,.2f}")


def main():
    cotizar_envios(crear_envios(), 20_000)


if __name__ == "__main__":
    main()