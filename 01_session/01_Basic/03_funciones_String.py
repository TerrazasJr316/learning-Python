# Capitalize

"""
lo que hace esta función es convertir
a mayúscula la primera leta de la
variable que guarda una cadena de texto
"""

dir = "demo de la dirección uno"
dir = dir.capitalize()

print(dir)

# Casefold

"""
Esta función lo que hace es convertir
la variable de cadena de texto a minúscula
si esque se encuentra algun caracter en mayúscula
"""

nom = "Josue Terrazas Mendoza"
nom = nom.casefold()

print(nom)

# Center

"""
Esta función se encarga de
añadir un espacio de n ppixeles
entre la primera letra y ultima
de la cadena de texto
"""
dato = "Chevrolet"
dato = dato.center(30)

print(dato)

# Count

"""
Permite contar el numero de palabras
que se solicite dentro de una cedana
de texto
"""

mensaje = "Las manzanas son rojas, las manzanas son mi fruta favorita y las manzanas verdes es la que mas me gusta"
message = mensaje.count("manzanas")

print("Existe la palabra manzanas: " + str(message))