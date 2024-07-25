"""
Imprime la tabla de multiplicar de los 10 primeros numeros
"""

for i in range(1, 11):
    print("Tabla de", i)
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("\n")
        