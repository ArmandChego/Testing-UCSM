import pytest
from calculadora import *

@pytest.mark.parametrize('operacion, valores, resultado', {
    ('SUMA', (10,20,40,50,60), 180),
    ('RESTA', (15,5), 10),
    ('RESTA', (15,), 15), # Se agrego la coma en (15,) para que sea una tupla con un solo elemento. (15) solo es un entero, por eso daba error
    ('RESTA', (100, 50, 25), 25),  # Resta con mas de dos numeros
    ('SUMA', (-10, -20, -30), -60),  # Suma de numeros negativos
    ('MULTIPLICACION', (2, 3), 6),  # Multiplicacion basica
    ('MULTIPLICACION', (4, 5, 2), 40),  # Multiplicacion con varios numeros
    ('MULTIPLICACION', (7,), 7),  # Multiplicar con un solo numero
    ('MULTIPLICACION', (1, 2, 3, 0), 0),  # Multiplicar con 0
    ('DIVISION', (100, 2), 50),  # Division entre dos numeros
    ('DIVISION', (50, 5, 2), 5),  # Division con varios numeros
    ("DIVISION", (10), )
})
def test_calculadora(operacion,valores, resultado):
    respuesta = calculadora(operacion,*valores)
    assert respuesta == resultado

def test_division_cero():  # Prueba de division entre cero
    with pytest.raises(ZeroDivisionError):
        calculadora("DIVISION", 10, 0)

def test_division_un_valor(): # Prueba de division con 1 solo numero
    with pytest.raises(ValueError):
        calculadora("DIVISION", 10)