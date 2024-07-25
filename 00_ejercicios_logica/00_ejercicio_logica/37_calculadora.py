"""
Haz una calculadora
"""

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

operacion = input("Intruduce una operacion (+ - * /): ")

match operacion:
    case "+":
        res = num1 + num2;
    case "-":
        res = num1 - num2;
    case "*":
        res = num1 * num2;
    case "/":
        res = num1 / num2;

print(f"El resultado es {num1} {operacion} {num2} = {res}")
