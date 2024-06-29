"""
13.- Escribir un programa que pregunte el nombre del usuario en la consola y despúes de el usuario lo
introduzca muestre en pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre en mayúsculas y
<n> es el número de letras que tiene el nombre
"""

nom = input("Dame tu nombre: ")
mayusculas = nom.upper()
num_letras = len(nom)

print(num_letras)

print("Mi nombre en mayúsculas es: ", mayusculas + " y tiene " + str(num_letras) + " letras" )