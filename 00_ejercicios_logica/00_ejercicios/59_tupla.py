"""
Que es una tupla
"""

lista = [1,2,3]
tupla = (1,2,3)

print(tupla(0))

lista[0] = 2

# tupla[0] = 2 
# es inmutable

tupla = lista(tupla)
tupla[0] = 3

print(tupla)