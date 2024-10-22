"""Haz una funcion que devuelva si una letra es vocal o no"""

vocals = ["a","e","i","o","u",]
def is_vocal(x):
    if x.lower() is vocals:
        return True
    else:
        return False

print(is_vocal("a"))
