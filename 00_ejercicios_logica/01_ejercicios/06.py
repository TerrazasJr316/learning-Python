import re
texto = "Contacto: ana@example.com, pedro@mail.com"
correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print(correos)