# Variables

my_string_variable = 'My Sring Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variabe = True
print(my_bool_variabe)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variabe)
print("Estes es el valor de:", my_bool_variabe)

# Algunas funciones del sistema
print(len(my_int_to_str_variable))
print(type(my_string_variable))

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Josue", "Terrazas", 'JR316', 20
print("Me llamo: ", name, surname, ". Mi edad es: ", age, ". Y mi alias es: ", alias)

# Inputs
name = input('¿Cual es tu nombre? ')
age = input('¿Cuantos años tienes? ')

print(name)
print(age)

# Cambiamos su tipo
name = 35
age = 'Josue'

print(name)
print(age)

# Forzamos el tipo
address: str = "Mi dirección"
address = 32
address = False
address = 1.54
print(type(address))