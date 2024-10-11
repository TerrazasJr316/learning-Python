"""
Función que devuelva el
numero contenido dentro de
una frase
"""

def devolver_numero(frase):
    numero = []
    for letra in frase:
        if letra.isdigit():
            numero.append(int(letra))
    return numero

print(devolver_numero("Hola que tal 3 adios 1 josue 21"))