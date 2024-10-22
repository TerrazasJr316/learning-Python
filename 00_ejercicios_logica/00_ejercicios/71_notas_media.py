"""
Programa que reciba notas
de clase hasta que la nota
introducida sea -1. El
programa debe imprimir la
media
"""

nota = 0
total = 0
contador_notas = 0

while nota != -1:
    nota = float(input("Introduce una nota: "))
    
    if nota != -1:
        contador_notas += 1
        total = nota

print(f"Media: {total/contador_notas}")