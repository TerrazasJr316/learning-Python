"""
Haz una funcion qe crea y devuelve una lista con n nunmeros enteros con valores entre a y b
"""

import random

def crear_lista(n,a,b):
    lsita = []
    for i in range(n):
        lsita.append(random.randint(a,b))
    return lsita

print(crear_lista(5,1,10))