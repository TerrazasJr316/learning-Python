"""
Haz una función que dibuje un cuadrado de lado N en la consola
"""

def dibujar_cuadrado(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
            print()
            
dibujar_cuadrado(4)