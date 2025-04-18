"""
Funciones matemáticas para la calculadora
"""


def sumar(a, b):
    """
    Función para sumar dos números.
    :param a: Primer número
    :param b: Segundo número
    :return: Suma de a y b
    """
    return a + b


def restar(a, b):
    """
    Función para restar dos números.
    :param a: Primer número
    :param b: Segundo número
    :return: Resta de a y b
    """
    return a - b


def multiplicar(a, b):
    """
    Función para multiplicar dos números.
    :param a: Primer número
    :param b: Segundo número
    :return: Producto de a y b
    """
    return a * b


def dividir(a, b):
    """
    Función para dividir dos números.
    :param a: Primer número
    :param b: Segundo número
    :return: Cociente de a y b
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """
    Función para elevar un número a una potencia.
    :param a: Base
    :param b: Exponente
    :return: Resultado de a elevado a la potencia de b
    """
    return a**b


def modulo(a, b):
    """
    Función para calcular el módulo de dos números.
    :param a: Primer número
    :param b: Segundo número
    :return: Módulo de a y b
    """
    if b == 0:
        raise ZeroDivisionError("No se puede calcular el módulo por cero")
    return a % b
