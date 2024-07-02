"""
Haz una funcion que cuente el numero
de palabras que tiene un archivo de
texto
"""

def cuenta_palabras(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        return len(data.split())
    
print(cuenta_palabras('datos.txt'))