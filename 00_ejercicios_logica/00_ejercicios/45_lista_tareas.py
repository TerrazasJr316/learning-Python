"""
Haz un programa que permita crear y listar tareas
"""

lista_tareas = []

opcion = 0

while opcion != 3:
    print("1. ver lista")
    print("2. añadir lista")
    print("3. salir")
    opcion = int(input("Elige: "))
    
    if opcion == 1:
        for i,tarea in enumerate(lista_tareas):
            print(f"{i}. {tarea}")
    elif opcion == 2:
      nueva_tarea = input("Introduce una nueva tarea para introducir: ")
      lista_tareas.append(nueva_tarea)
      
            