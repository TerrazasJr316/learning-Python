with open("leerTexto.txt", "r") as file:
    data = file.readlines()

for line in data:
    print(line)