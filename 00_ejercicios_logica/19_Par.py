"""
Haz una funcion qie imprima todos los numeros pares entre A  y B
"""

def imprimir_pares(a, b):
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i)

imprimir_pares(2,18)