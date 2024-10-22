"""
Haz un programa que escriba 100 numeros al azar en
un archivo de texto
"""
import random

with open("numeros.txt", "a") as archivo:
    for i in range(100):
        archivo.write(f"{random.randint(1,100)}\n")

