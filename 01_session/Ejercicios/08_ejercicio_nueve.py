"""
9.- Escrribir un programa que pida al usario su peso en (kg) y estatura en (m), cualcule
el índice de masa corporal y lo almacene en una variable y muestre por pantalla la frase:
"Ti índice de masa corporal es -- imc --" donde -- mc -- es el indice de mas corporal calculado
redondeado con dos decimales.
"""

peso = float(input("Dame tu peso en Kg: "))
estatura = float(input("Dame tu estatura en m: "))

imc= (peso /(estatura)**2)

# Forma de rodondear
imc = round(imc, 2)

print("Tu índice de masa corporañ es: ", str(imc))