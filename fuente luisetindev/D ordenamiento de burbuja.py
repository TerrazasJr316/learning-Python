#Ordena lista con algoritmo burbuja

def bubblee_short(lista):
        for i in range(len(lista)):
            for j in range(0, len(lista) - 1 - i):
                if lista[j] > lista[j + 1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux
    
mi_lista = [1,3,2,14,143,39,0]
bubblee_short(mi_lista)
print(mi_lista)                