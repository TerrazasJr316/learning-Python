"""
Un número a es factorPorDigito de
b si todos los digitos de a son 
divisores de b.
Por ejemplo 132 es factorPorDigito de 6.
Hacer una función que reciba dos
números enteros y devuelva True en caso
de que el primero sea FactorPorDigito del
segundo y False en caso contrario
"""

def es_factor_digito(a,b):
    a = str(a)
    for digito in a:
        if b % int(digito) != 0:
            return False
    return True

print(es_factor_digito(132,6))