"""
12.- Escribir un programa que pregunte el nombre completo del usuario en la consola y despúes muestre
por pantalla el nombre del usuario tres veces, una con todas las letras minúsculas, otra con todas las
letras mayúsculas y otro solo con la primera letra del nombre y de los apellidos en mayúscula. El
usuario puede introducir su nombre combinando mayúsculas y munúsculas como quiera.
"""

nom = input("Dame tu  nombre completo: ")
minusculas = nom.lower()
mayusculas = nom.upper()
primer = nom.title()

print(minusculas)
print(mayusculas)
print(primer)