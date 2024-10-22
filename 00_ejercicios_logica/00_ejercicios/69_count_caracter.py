"""
Haz una función que devuelva cuantas
veces aparece una letra en una cadena
de caracteres (sin count)
"""

def contar_letras(texto,letra):
    contador = 0
    for char in texto:
        if letra == char:
            contador += 1
    return contador

print(contar_letras("Hola me llamo Josué", "l"))