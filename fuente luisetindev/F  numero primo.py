#Haz una función que devuelva SI un numero n es primo o NO}

def es_primo(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

print(es_primo(5))
print(es_primo(28))