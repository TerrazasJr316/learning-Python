"""
Funcion que multiplique 2 numeros sin utilizar * y devuelva el resutlado
"""

from operator import mul


def multiplica(a,b):
    total = 0
    for i in range(a):
        total += b
    return total

print(multiplica(2,4))
print(multiplica(3,98))