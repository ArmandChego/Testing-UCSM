import pytest
from calculadora import *

@pytest.mark.parametrize('operacion, valores, resultado', {
    ('SUMA', (10,20,40,50,60), 180),
    ('RESTA', (15,5), 10),
    ('RESTA', (15,), 15), # Se agrego la coma en (15,) para que sea una tupla con un solo elemento. (15) solo es un entero, por eso daba error
})
def test_calculadora(operacion,valores, resultado):
    respuesta = calculadora(operacion,*valores)
    assert respuesta == resultado