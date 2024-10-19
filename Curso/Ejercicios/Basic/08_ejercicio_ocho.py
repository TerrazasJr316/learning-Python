"""
8.- Escribir un programa que lea un entero positivo 'n', introducido por el usuario
y despues demuestre en pantalla la sima de todos los enteros desde 1 hasta la suma
de los primeros enteros positivos puede ser calculada de la siguiente forma: "suma = n(n + 1)/2"
"""

# Pedir el numero N
n = int(input("Dame el numero de veces: "))

suma = (n * (n + 1))/ 2
print("La suma es igual a:" , str(suma))
