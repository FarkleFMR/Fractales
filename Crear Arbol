import pygame, math
import random
import time
from random import choice

pygame.init()
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
 

def dibujarArbolAux(x1, y1, angulo, angulo_de_ramificaciones,diametro_nivel,diametro_tronco,ramificaciones,decremento_pro,rango_pro):
   
    profundidad = random.randint(rango_pro[0], rango_pro[1])
    diametro_troncoR = random.randint(diametro_tronco[0], diametro_tronco[1])
    
    dibujarArbol(x1, y1, angulo, profundidad, angulo_de_ramificaciones,diametro_nivel,diametro_troncoR,ramificaciones,decremento_pro,rango_pro)


def dibujarArbol(x1, y1, angulo, profundidad, angulo_de_ramificaciones,diametro_nivel,diametro_tronco,ramificaciones,decremento_pro,rango_pro):

    if diametro_tronco <= 0:
            diametro_tronco=1
    angulo_de_ramificacionesR = random.randint(angulo_de_ramificaciones[0], angulo_de_ramificaciones[1])
    diametro_nivelR = random.randint(diametro_nivel[0], diametro_nivel[1])    
    decremento_proR = random.randint(decremento_pro[0], decremento_pro[1])

    ramasR = random.randint(ramificaciones[0], ramificaciones[1])
    ramas = ramasR
    angulo_aux = 0
    angulo_aux2 = angulo_de_ramificacionesR/ramas
    
    if profundidad > 0:
        x2 = x1 + int(math.cos(math.radians(angulo)) * profundidad * diametro_nivelR)
        y2 = y1 + int(math.sin(math.radians(angulo)) * profundidad * diametro_nivelR)
        
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), diametro_tronco)

        while ramas > 0:
           angulo_aux2 *= choice([-1, 1])
           angulo_aux = angulo_aux2 * random.randrange(ramasR)
           
           dibujarArbol(x2, y2, angulo + angulo_aux , profundidad - decremento_proR,angulo_de_ramificaciones,diametro_nivel,diametro_tronco-1,ramificaciones,decremento_pro,rango_pro)           
           ramas = ramas - 1
           
        

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

'''
Número de ramificaciones2.  Ángulo de las ramificaciones3.  Profundidad del árbol (cantidad de niveles)4.
Longitud/diámetro inicial del tronco5.  Proporción de decremento de la longitud/diámetro en cada nivel
'''

##drawTree(600, 790, -90, 10,20,5,1)
'''
X
Y
angulo

angulo_de_ramificaciones
diametro_nivel
diametro_tronco
ramificaciones
decremento_pro
rango_pro
'''
n= 100
while n > 0:


    '''
    X
    Y
    angulo

    angulo_de_ramificaciones
    diametro_nivel
    diametro_tronco
    ramificaciones
    decremento_pro
    rango_pro
    '''


    
    dibujarArbolAux(600, 700, -90,
                    [90,91],[8,8],[3,3],[5,5],[1,1],[7,7])


    
    pygame.display.flip()
    #while True:
    #    input(pygame.event.wait())
    time.sleep(0.5)
    screen.fill((0,0,0))
    n = n-1

