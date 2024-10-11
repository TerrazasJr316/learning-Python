"""
Haz una funcion que pida una frase y devuelva el numero
de palabras que tiene
"""

def contar():
    frase = input(": ")
    palabras = frase.split(" ")
    return len(palabras)

print(contar())
