"""
Haz una función que pida los numeros que el usuario quiera e imprima la medida de todos
"""

numero = 0
total = 0
contador = 0

while numero != 1:
    numero = int(input("Introduce un numero o -1 para salir: "))
    if numero != -1:
        total += numero
        contador += 1
        print(f"La medida es: {total / contador}")