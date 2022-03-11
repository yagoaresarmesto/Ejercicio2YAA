from abc import ABC, abstractmethod


class Moneda(ABC):
    def __init__(self, cantidad):
        self.cantidad = cantidad;

    @abstractmethod
    def cantidadEnEuros(self):
        pass


class Dolar(Moneda):
    def cantidadEnEuros(self):
        resultado = self.cantidad * 0.89

        return resultado


class Libra(Moneda):
    def cantidadEnEuros(self):
        resultado = self.cantidad * 1.2

        return resultado

class Yen(Moneda):
        def cantidadEnEuros(self):
            resultado = self.cantidad * 0.0078

            return resultado
