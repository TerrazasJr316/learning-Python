"""
Dada una lista de numeros, sustituye
las posiciones pares por '*' y
multiplica las impares por 100
"""

lista = [1,2,3,4,89,123,42]

for i in range (len(lista)):
    if i % 2 != 0:
        lista[i] = "*"
    else:
        lista[i] *= 100

print(lista)