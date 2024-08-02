"""
Simula el juego de piedra, papel o tijera
"""
import random

opciones = ["piedra", "papel", "tijera"]

usuario = input("Eligue: ").lower()
ordenador = random.choice(opciones)

if usuario not in opciones:
    print("Error")
    quit()

if usuario == ordenador:
    print("Empate")
elif usuario == "tijera" and ordenador == "piedra" or usuario == "piedra" and ordenador == "papel" or usuario == "papel" and ordenador == "tijera":
    print("Haz perdido")
else:
    print("Haz ganado")