import pygame
from 01_personaje import cubo
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode([ANCHO, ALTO])

jugando = True

cubo = Cubo(100, 100)

while jugando:
    eventos = pygame.event.get()
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
        
    cubo.dibujar
    pygame.display.update()
    
quit()