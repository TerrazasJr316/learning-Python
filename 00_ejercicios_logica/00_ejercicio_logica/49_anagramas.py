"""
Haz una funcion que recibe dos cadenas de texto y devuelva si son anagramas entre si o no
"""

def es_anagrama(p1, p2):
    if len(p1) != len(p2):
        return False
    
    if sorted(p1) == sorted(p2):
        return True
    else:
        return  False
    
print(es_anagrama("boca", "cabo"))
print(es_anagrama("saul", "luis"))