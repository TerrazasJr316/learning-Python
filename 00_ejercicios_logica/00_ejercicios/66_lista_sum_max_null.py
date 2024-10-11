"""
Haz una función que acepte una
lista de eneteros como parametro y
devuelva la suma de todos los
elementos (sin max())
"""

def suma_total(lista):
    total = 0
    for num in lista:
        total += num
    return total

print(suma_total([1,2,3,4,5]))