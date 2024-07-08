"""
Simula el jeugo de adivinar el numero
"""

import random

ordenador = random.randint(1,100)
intentos = 0

while True:
    usuario = int(input("Introduce tu intento: "))
    intentos+=1

    if usuario > ordenador:
        print("Te has pasado")
    elif usuario < ordenador:
        print("Te has quedado corto")
    else:
        print(f"Bien, el numero era {ordenador}")
        print(f"Intentos: {intentos}")
        break