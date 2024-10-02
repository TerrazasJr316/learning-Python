"""
Para que sirve la función
"enumerate()"
"""

lista = ["manzana", "pera", "mandarina"]

print(list(enumerate(lista)))

for i, fruta in enumerate(lista):
    print(f"{fruta} es la {i + 1} fruta")