"""
Haz una función que sume
los primeros n numeros
utilizando recursividad
"""
def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n-1)
    
print(suma_recursiva(34))
