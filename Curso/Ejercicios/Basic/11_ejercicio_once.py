# Ejercicios con cadenas de texto

"""
11.- Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima
por pantalla en líneas distintas el nombre del usuario tantas veces como el numero introducido.
"""

nom = input("Dame tu nombre: ")
num = int(input("Dame un número entero: "))

print((nom + "\n") * int(num))
