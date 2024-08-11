"""
15.- Escribe un programa que pregunte al usuario la fecha de su nacimiento en  formato dd/mm/aaaa y
muestra por pantalla, el día, el mes y el año.
"""

fecha = input("Introduce la fecha con el formato dd/mm/aaaa: ")
dia = fecha[:2]
mes = fecha[3:5]
anio = fecha[6:]

print("El día es: ", dia)
print("El mes es: ", mes)
print("El año es: ", anio)
