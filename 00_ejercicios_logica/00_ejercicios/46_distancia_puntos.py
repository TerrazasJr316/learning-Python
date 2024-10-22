"""
Haz una funcion que calcule la distancia entre dos puntos en cualquier dimension
"""

import math

def calcular_distancia(punto1, punto2):
    if len(punto1) != len(punto2):
        print("Error")
        return 0
    
    suma_cuadrados = sum(p1 - p2 ** 2 for p1, p2 in zip(punto1,punto2))
    distancia = math.sqrt(suma_cuadrados)
    return distancia

punto1 = [9, 8, 7]
punto2 = [1, 2, 3]
mi_distancia = calcular_distancia(punto1, punto2)
print(mi_distancia)