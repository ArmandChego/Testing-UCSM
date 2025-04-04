# REALIZAR UNA FUNCION DE SUMATORIA O RESTA en la cual reciba n parametros
# SUMAR | RESTAR
# LIST | TUPLE | DICT | SET
def calculadora(operacion:str, *parametros:tuple[int,...] ) -> int:
    resultado = 0
    if operacion == 'SUMA':
        # resultado = sum(parametros)
        for numero in parametros:
            resultado += numero

    elif operacion == 'RESTA':
        resultado = parametros[0]
        if(len(parametros) != 1):
            for numero in parametros[1:]:
                resultado -= numero

    elif operacion == 'MULTIPLICACION':  # Nueva operacion para multiplicar
        resultado = 1
        for numero in parametros:
            resultado *= numero
    
    elif operacion == 'DIVISION':   # Nueva operacion para dividir
        if len(parametros) < 2:
            raise ValueError("Se necesitan dos numeros para dividir")
        resultado = parametros[0]
        for numero in parametros[1:]:
            if numero == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            resultado /= numero

    else:
        raise 'Operacion incorrecta'

    return resultado

