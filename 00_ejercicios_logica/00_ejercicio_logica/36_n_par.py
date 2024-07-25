"""
Haz una funcion que devuelva si un numero n es par o no
"""

def es_par(n):
    if n % 2 == 0:
        return f"{n} es par"
    else:
        return f"{n} es impar"
    
print(es_par(11))
print(es_par(100))