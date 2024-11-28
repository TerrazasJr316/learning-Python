# Ejemplos con VARIABLES (parte 1)

a = 20
b = 30
c = a + b

print(c)

a = 1300
b = 1500
multiplicacion = a * b

print(multiplicacion)

nom = "Josue"
ap = "Terrazas"
am = "Mendoza "

print(nom)
print(ap)
print(am)

nc = nom + " "+ " " + ap + " " + am

print(nc)

# Ejemplos con VARIABLES (parte 2)

a = 20
b = 30
print("La suma es: ", str(a + b))

print("La multiplicación es: ", str(a * b))

print("La división es: ", str(a / b))

print("La operación es: ", str((a * b) - (a - b)))

# Ejemplos con VARIABLES (parte 3)

a = 30
b = 20
a = a + (20 - 5) * (a * a)
suma = (a * a ) + b
nom = "Josue"

print ("El resultado es: " + str(a))

print (type(a))
print (type(b))
print (type(a))

# Ejemplos con VARIABLES (parte 4) --- INPUT ---

nom = input ("Dame tu nombre: ")
#lo que hace la funcion input es siempre almacena datos de tipo String
#habra que convertir el dato a tipo de dato numerico

print ("Tu nombre es: " + nom)

nom = "Josue"
ap = input ("Dame tu apellido: ")
num1 = 5
num2 = float(input("Dame el segundo nombre"))

#por coma:
# print("Nombre ", nom)
# print("Apellido", ap)

# por signo +
print("Nombre " + nom)
print("Apellido " + ap)
print("Nombre " + nom + " Apellido " + ap)
print("Numero 1 " + str (num1))
print("Numero 2 " + str (num2))

# funcion f
print(f"Numbre {nom} Apellido {ap} Numero1 = {num1} Numero2 = {num2}")
print(f"Suma es igual {num1} + {num2} = {num1 + num2}")