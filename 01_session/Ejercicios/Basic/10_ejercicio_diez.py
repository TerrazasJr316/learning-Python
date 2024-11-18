"""
10.- Una jugetería tiene mucho exito  en dos de sus productos:
payasos y muñecas. Suele haber venta por correo y la empresa de logística les cobra por peso de cada
paquete asi que deben calcular el peso de los payasos y muñecas que saldrán  de cada paquete a demanda.
Cada payaso pesa 112g y cada muñeca 75g. Escribir un programa que lea el número de payasos y muñecas
vendidos en el último pedido y calcule el peso total del paquete que será vendido
"""

peso_payaso = 112
peso_muneca = 75

numero_payasos = int(input("Dame el número de payasos a enviar: "))
numero_munecas = int(input("Dame el número de muñecas a enviar: "))

total_payasos = peso_payaso * numero_payasos
total_muneca = peso_muneca * numero_munecas

total = total_payasos + total_muneca

print("El peso total es: ", str(total))
