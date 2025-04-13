import math

# funcion original con errores
def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):  # El rango no incluye la raiz entera (falta +1), por lo que puede omite sqrt(n)
        if (number % check) == 0:
            return False
    return True

# Funcion corregida
def isPrime2(number):
    if number == 2:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):  # Recorre hasta la raiz incluida, y solo impares (ya se excluyo el 2)
        if number % check == 0:
            return False
    return True

# Funciones de prueba
def test_is_prime():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    assert isPrime(25) == False  #Falla con la funcion original


def test_is_prime2():
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(4) == False
    assert isPrime2(5) == True
    assert isPrime2(20) == False
    assert isPrime2(21) == False
    assert isPrime2(22) == False
    assert isPrime2(23) == True
    assert isPrime2(24) == False
    assert isPrime2(25) == False # Ya no falla con la segunda funcion
