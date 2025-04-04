#Ejercicio 2
import pytest
from hypothesis import given  # Importado para generar datos de prueba automaticos
from hypothesis.strategies import integers  # Importado para generar enteros aleatorios como datos de prueba
from colas import Queue 

@given(integers())  # Genera enteros aleatorios para la prueba
def test_enqueue_dequeue(value):
    q = Queue()
    q.enqueue(value)  # Agrega el valor a la cola
    assert q.dequeue() == value  # Verifica que el valor extraido sea el mismo

@given(integers())
def test_size(value):
    q = Queue()
    q.enqueue(value) 
    assert q.size() == 1  # Verifica que el tamano sea 1 despues de un enqueue

def test_is_empty():
    q = Queue()
    assert q.is_empty()

def test_dequeue_empty():
    q = Queue()
    try:
        q.dequeue()  # Intenta hacer dequeue en una cola vacia
        assert False, "IndexError"
    except IndexError:
        pass

def test_front_empty():
    q = Queue()
    try:
        q.front()  # Intenta acceder al primer elemento en una cola vacia
        assert False, "IndexError"
    except IndexError:
        pass

@given(integers())
def test_front(value):
    q = Queue()
    q.enqueue(value)
    assert q.front() == value  # Verifica que el primer valor en la cola sea el que se ingreso

def test_str():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert str(q) == "[1, 2, 3]"  # Verifica que la representacion en cadena sea correcta
