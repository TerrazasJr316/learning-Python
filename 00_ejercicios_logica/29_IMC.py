"""
Haz una funcion que calcule el
IMC de una persona dado el peso y la
altura y lo clasifique
"""

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("peso bajo")
    elif 18.5 <= imc < 25:
        print("peso medio")
    elif 25 <= imc < 30:
        print("sobrepeso")
    else:
        print("obesidad")

calcular_imc(84, 1.90)