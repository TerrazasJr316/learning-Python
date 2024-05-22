class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = "Josue " #inctrudce tu nombre
        self.edad = 20
        self.genero = "Hombre"
        if edad >= 18:
            self.mayorEdad = True
        else :
            self.mayorEdad = False
            
    def imprimirDatos(self):
        print(f"Nombre:{self.nombre}\nEdad:{self.edad} \nGenero:{self.genero} \nMayor de Edad:{self.mayorEdad}")
persona1 = Persona("Josue", 20, "Hombre")
persona1.imprimirDatos()
        
            
        