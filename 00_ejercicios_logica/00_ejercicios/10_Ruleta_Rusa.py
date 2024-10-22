import random
ai = random.randint(1,10)
numero = -1
while numero != ai:
    numero = int(input("Introduce un numero: "))
    if numero > ai:
        print("Te haz pasado")
    elif numero < ai:
        print("Te haz quedado corto")
        
print(f"Haz terminado, el numero era {ai}")
