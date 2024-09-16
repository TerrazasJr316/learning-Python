# capitalize

"""
lo que hace esta función es convertir
a mayúscula la primera leta de la
variable que guarda una cadena de texto
"""

dir = "demo de la dirección uno"
dir = dir.capitalize()

print(dir)

# casefold

"""
Esta función lo que hace es convertir
la variable de cadena de texto a minúscula
si esque se encuentra algun caracter en mayúscula
"""

nom = "Josue Terrazas Mendoza"
nom = nom.casefold()

print(nom)

# center

"""
Esta función se encarga de
añadir un espacio de n ppixeles
entre la primera letra y ultima
de la cadena de texto
"""
dato = "Chevrolet"
dato = dato.center(30)

print(dato)

# count

"""
Permite contar el numero de palabras
que se solicite dentro de una cedana
de texto.

De igual manera de se puede agregar un
intervalo de la cadena para busque la
palabra en ese solo intervalo 
"""

mensaje = "Las manzanas son rojas, las manzanas son mi fruta favorita y las manzanas verdes es la que mas me gusta"
message = mensaje.count("manzanas")

print("Existe la palabra manzanas: " + str(message))

message = mensaje.count("manzanas", 0, 20)

print("Existe la palabra manzanas: " + str(message))

# endswith

"""
Cumple con evaluar si la variable guarda
una cadena de texto y se especifica si
termina con lo que se escriba
"""

ads = "Hola bienvenido al  mundo de Python"
result = ads.endswith("de Python")

print(result)

result = ads.endswith("de Python")

print(result)

# find

"""
Se encarga de buscar dicha cadena
de la variable que gurda la cadena de
texto recorriendo caracter por carcter
"""

example = "Esto es un ejemplo de texto"
final = example.find("Esto")

print(final)

# format

"""
se puden usar n variables y con ellas
darle el valor cualquiera que sea
"""

txt = "Mi nombre es {nom} y mi edad es de {edad}".format(nom = "Josué", edad = "21")
print(txt)

txt1 = "Mi nombre es {0} y mi edad es de {1}".format("Josué", 21)

print(txt1)

# isalnum

"""
Funcion para hacer la validación
de los datos sea alfanumericos.
"""

nombre = "Josue13?"
muestra = nombre.isalnum()

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


