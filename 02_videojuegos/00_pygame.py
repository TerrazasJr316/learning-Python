import pygame
from personaje import Cubo


ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode([ANCHO, ALTO])

jugando = True

cubo = Cubo(100, 100)

def gestionar_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad

while jugando:
    eventos = pygame.event.get()
    
    teclas = pygame.key.get_pressed()
    
    gestionar_teclas(teclas)
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
            
    VENTANA.fill("white")
    cubo.dibujar(VENTANA)
    pygame.display.update()
    
quit()