"""
Haz un programa que pida la peda y solo te deje entrar si tiene al menos 18 años
"""

edad = int(input("Intoduce tu edad: "))

if edad >= 18:
    print("Estas dentro!")
else:
    print("No tienes la mayoria de edad")