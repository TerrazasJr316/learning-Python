"""
Haz una programa que diga cuentos dias llevas vivo a partir de tu fecha de nacimiento
"""

from datetime import datetime

def dias_vivo(fecha_nacimiento):
    hoy = datetime.now()
    nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    dias_vivo = (hoy-nacimiento).days
    return dias_vivo

tu_fecha = input("Indroduce tu fecha de nacimiento (DIA-MES-AÑO): ")
dias = dias_vivo(tu_fecha)
print(f"Llevas {dias} dias vivo")