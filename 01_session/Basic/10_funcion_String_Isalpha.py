#isalpha

"""
hace la valdación si el dato
esta entre el intervalo de la
"a" a la "z".
"""

cliente =  "Josue"
impresion = cliente.isalpha()

print(impresion)

# islower

"""
valida si el dato guardado
esta en minúsculas.
"""

client = "este es un texto en minúscula"
resultado = client.islower()

print(resultado)

# isnumeric

"""
la función valida si el dato
contiene numneros "unicamente" entero
"""

numero = "9123469"
result_num = numero.isnumeric()

print(result_num)

#isuupper

"""
valida si todo el texto esta es
mayúsculas.
"""

upper = "ESTE ES UN MENSAJE EN MAYÚSCULAS"
is_upper = upper.isupper()

print(is_upper)

#  join

"""
esta función permite
unir un texto y separalo por
coma (,), comillas simples('') etc.add() 
"""

example_join = ("Josue","Terrazas","Mendoza")
result_join = "#".join(example_join)

print(result_num)

# lower

"""
permite pasar un dato a
minúsculas
"""

example_lower = "Bienvenido a Python un Lenjuage de ALTO NIVEL"
result_lower = example_lower.lower()

print(result_lower)

# lstrip

"""
recorre el espacio del lado
izquierdo
"""

example_lstrip = "Python"
result_lstrip = example_lstrip.lstrip()

print("Bienvenido a " + example_lstrip + " lenguaje de alto nivel")

# maketrans and translate

example_maketrans = "Josue Terrazas1"
result_maketrans = example_maketrans.maketrans("1", " ")

print(example_maketrans.translate(result_maketrans))

example_two_maketrans = "Josue Terrazas1234"
example_num = "1234"
example_num_change = "    "
result_two_maketrans = example_maketrans.maketrans(example_num, example_num_change)

print(example_maketrans.translate(result_maketrans))

# partition

example_partition = "Bienvenido, este mensaje esta hecho en Python"
result_partition = example_partition.partition("este")

print(result_partition)

# replace

example_raplace = "Este es un mensaje programado en PHP"
result_replace = example_raplace.replace("PHP", "Python")

print(result_replace)

# split

example_split = "Este es un mensaje programado en Python"
result_split = example_split.split()

print(result_split)

# splitlines

example_splitlines = "Este es un mensaje \n programado en Python"
result_splitlines = example_splitlines.splitlines()

print(result_splitlines)

# strip

example_strip = "Este es un manesaje programado en Python"
result_strip = example_strip.strip()

print("Bienvenido. " + result_strip)

# swapcase

example_swapcase = "Este es un manesaje programado en Python"
result_swapcase = example_swapcase.swapcase()

print(result_swapcase)

# title

example_title = "Este es un manesaje programado en Python"
result_title = example_title.title()

print(result_title)

# uper

example_uper = "Este es un manesaje programado en Python"
result_uper = example_uper.upper()

print(result_uper)

"""
Este es un texto comentado en
Python en varias lineas.
"""

'''
Este es otro ejemplo de texto
comentado en Python en varias lineas
'''