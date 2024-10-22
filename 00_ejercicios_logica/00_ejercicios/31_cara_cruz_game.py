"""
Simula el juego de cara o cruz
"""
import random

opciones = ["cara", "cruz"]
usuario = input("cara o cruz: ").lower()

if usuario not in opciones:
    print("Error")
    quit()

resultado = random.choice(opciones)

print("El resultado es: ", resultado)

if resultado == usuario:
    print("Haz ganado")
else:
    print("Haz perdido")