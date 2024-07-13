"""
Haz un juego de memoria
"""

import random
import time
import os

minimo = 1
maximo = 9

while True:
    numero = str(random.randint(minimo, maximo))
    print(f"Recuerda el numero {numero}...")
    time.sleep(1.5)
    os.system("cls")
    intento = input("Introduce el numero: ")
    
    if intento == numero:
        print("Bien, lo haz adivinado")
        maximo *= 10
        minimo *= 10
    else:
        print("mal, el nuemro era, ", numero)
        break