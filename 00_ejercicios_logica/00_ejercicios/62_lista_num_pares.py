"""
Dada una lista de numeros enteros
imprime solo los numeros pares
"""

lista = [1, 2, 3, 4, 5, 1]

for numero in lista:
    if numero % 2 == 0:
        print(numero)