"""
Haz una funcion que devuelva el area y perimetro de un circulo
"""

import math

def circulo(radio):
    area = math.pi * radio ** 2
    perim = math.pi * radio * 2
    return area, perim
a,p = circulo(5)
print(f"Area: {a}")
print(f"Preimetro: {p}")