"""
Haz un programa para aprender a sumar en poco tiempo
"""

import time
import random

aciertos = 0

tiempo_inicio = time.time()

for i in range(5):
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    correcto = numero1 + numero2

    respuesta = int(input(f"Cuanto es {numero1} + {numero2}?: "))

    if respuesta == correcto:
        print("Correcto")
        aciertos += 1
    else:
        print(f"FATAL, eñ numero era {correcto}")

tiempo_total = time.time()-tiempo_inicio
print(f"Haz ganado {tiempo_total:2f} segundos")
print(f"Tus aciertos: {aciertos}")