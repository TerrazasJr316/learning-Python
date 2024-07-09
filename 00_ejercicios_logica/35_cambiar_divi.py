""""
Haz un programa para cambiar de divisa
"""

divisas = {
    "USD":1.09,
    "MXN":18.06,
}

cantidad = int (input("Introduce la cantidad:"))
simbolo = input("Intrudce el simbolo de la divisa: ")
if simbolo not in divisas:
    print("Ha habido un erro!")
else:
    total = cantidad * divisas[simbolo]
    print(f"Cantidad total {total:.2f} {simbolo}")