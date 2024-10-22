#Haz una función que devuelva el facotrial de un numero

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(6))
