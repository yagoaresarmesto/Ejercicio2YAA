from monedas import Dolar
from monedas import Libra
from monedas import Yen


def escribir_menu():
    print('\nCONVERSOR DE MONEDAS\n1. Dólares\n2. Libras\n3. Yens\n0. Salir')


def pedir_opcion():
    print('Escoja una opción: ', end='')


def leer_opcion():
    try:
        op = int(input())
    except ValueError:
        op = None
    finally:
        return op


def convertirADolares():
    dolar =float(input("Escribe la cantidad en DÓLARES para convertir a euros: "))
    d = Dolar(dolar)
    print('Cantidad en euros:', d.cantidadEnEuros(),"€")


def convertirABritishPound():
    libra= float(input("Escribe la cantidad en LIBRAS para convertir a euros: "))
    l = Libra(libra)
    print('Cantidad en libras:', l.cantidadEnEuros(),"€")


def convertirAJapaneseYen():
    yen = float(input("Escribe la cantidad en YENES para convertir a euros: "))
    y = Yen(yen)
    print('Cantidad en yenes:', y.cantidadEnEuros(),"€")


if __name__ == '__main__':
    while True:
        escribir_menu()
        pedir_opcion()
        opcion = leer_opcion()
        if opcion == 0:
            exit(0)
        elif opcion == 1:
            convertirADolares()
        elif opcion == 2:
            convertirABritishPound()
        elif opcion == 3:
            convertirAJapaneseYen()
        else:
            print('Opción no válida, elige una opción válida')
