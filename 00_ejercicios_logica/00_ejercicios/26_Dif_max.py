"""
Haz una función que devuelva
la diferencia maxima entre
2 elementos de una lista
"""

def diferencia_maxima(lista):
    if len(lista) <= 1:
        return 0
    lista.sort()
    min = lista[0]
    max = lista[-1]
    return max-min
print(diferencia_maxima([1,9,8,3,2,11]))
