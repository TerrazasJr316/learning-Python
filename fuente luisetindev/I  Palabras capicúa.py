#Función que devuelva si una palabra es capicua se lee igual al reves

def capicua(palabra):
    reves = ""
    for i in range(len(palabra)-1,-1,-1):
        reves += palabra[i]
    return palabra == reves

print(capicua("hola"))
print(capicua("radar"))