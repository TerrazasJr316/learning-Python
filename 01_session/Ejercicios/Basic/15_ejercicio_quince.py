"""
15.- Escribe un programa que pida al usuario que introduza una frase en consola y una vocal, y despúes
muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

frase = input("Dame la frase: ")
vocal = input("Introduce una vocal en minúsculas: ")

print(frase.replace(vocal, vocal.upper()))
