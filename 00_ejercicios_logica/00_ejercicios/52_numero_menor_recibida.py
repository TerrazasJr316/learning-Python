"""
Función que devuelva el numero menor de una lista recibida por parametros
"""

def devolver_numero(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

print(devolver_numero([3,5,1,100,99,1000]))