"""
Haz una función que pase de segundos a dias, horas, minutos
"""

def convertir_segundos(seg):
    dias = seg // 86400
    seg %= 86400
    horas = seg // 3600
    seg %= 3600
    minutos = seg // 60
    seg %= 60

    return f"{dias} dias, {horas} horas, {minutos} minutos, {seg} segundos"

print(convertir_segundos(100000))