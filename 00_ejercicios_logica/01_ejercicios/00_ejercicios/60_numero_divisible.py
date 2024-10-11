"""
Haz una funcion que reciba un numero n
y diga si es divisble por 2, 3 o 5
"""

def es_divisible(n):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return True
    return False

print(es_divisible(10))
print(es_divisible(15))
print(es_divisible(18))
print(es_divisible(37))