"""
Juego en python
en el que el usuario
adivine el numero es
divisor de otro
"""

import random

divisor = random.randint(1,10)
dividendo = random.randint(1,100)

usuario = input(f"{dividendo} / {divisor} da resto 0?: ")

respuesta = dividendo % divisor == 0

if usuario == "si" and respuesta == True or usuario == "no" and respuesta == False:
    print("Hemos ganado")
else:
    print("Hemos perdido")