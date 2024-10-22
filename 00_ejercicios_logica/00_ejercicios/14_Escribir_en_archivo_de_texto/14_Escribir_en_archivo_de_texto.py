#Escribe los numero 1-100 en un archivo de texto

file = open("numeros.txt", "w")
for i in range(100):
    file.write(f"{i}\n")
file.close()
