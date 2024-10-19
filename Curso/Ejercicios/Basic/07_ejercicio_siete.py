"""
7.-Escribir un programa que pregunte al usuario por el numero de horas trabajadas y el pago por hora
Despues debe mostrar por pantalla la paga que le corresponde 
"""

nom = input("Dame tu nombre: ")
horas = float(input("Cuantas horas trabajaste: "))
pago = float(input("Cuanto te pagan por hora: "))
total = horas * pago

print ("Saludos " + nom + "tu pago es de " + str (total))

