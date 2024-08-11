"""
Haz un programa protegido por usuario y contraseña
"""

user = "Jr316"
password = "b#w$sdo(f'4340"

user_input = input("Introduce tu usuario: ")
password_input = input("Introduce tu contraseña: ")

if user != user_input or password != password_input:
    print("Datos incorrectos")
    quit()
    
print("Estas dentro")