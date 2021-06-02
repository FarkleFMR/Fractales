#Creado por Leonardo Fariña y Murillo Aldecoba
#Fecha de creación: 25/05/2020 10:10 pm
#Última modificación: 01/06/2020 21:31 pm
#Versión 3.9.2

#Importación de librerias


import pygame, math
import random
import time
from os import mkdir
from random import choice
from PIL import Image
import numpy as np




#Definicion de funciones


def dibujarArbolAux(x1, y1, angulo, angulo_de_ramificaciones,diametro_nivel,diametro_tronco,ramificaciones,decremento_pro,rango_pro):
    '''
    Entradas:
        x1(Posición en X de la pantalla de pygame)
        y1(Posición en Y de la pantalla de pygame)
        angulo(Dirección para donde se creara el arbol)
        angulo_de_ramificaciones(Rango de ángulos de las ramas entre si)
        diametro_nivel(Rango de longitud entre cada nivel de profundidad)
        diametro_tronco(Rango de grosor de la rama)
        ramificaciones(Rango de la cantidad de ramas a dibujar)
        decremento_pro(Rango de decrementación de la longitud)
        rango_pro(Rango de la profundidad)
    Funcionalidad:
        Elegir la profundidad del arbol y su grosor inicial
        Hacer la llamada a la función dibujarArbol con todos los parametros con la profundidad y el grosor
    Salida:        
        None
    '''
    profundidad = random.randint(rango_pro[0], rango_pro[1])
    diametro_troncoR = random.randint(diametro_tronco[0], diametro_tronco[1])    
    dibujarArbol(x1, y1, angulo, profundidad, angulo_de_ramificaciones,diametro_nivel,diametro_troncoR,ramificaciones,decremento_pro,rango_pro)


def dibujarArbol(x1, y1, angulo, profundidad, angulo_de_ramificaciones,diametro_nivel,diametro_tronco,ramificaciones,decremento_pro,rango_pro):
    '''
    Entradas:
        x1(Posición en X de la pantalla de pygame)
        y1(Posición en Y de la pantalla de pygame)
        angulo(Dirección para donde se creara el arbol)
        profundidad(Profundidad que tendra el árbol)
        angulo_de_ramificaciones(Rango de ángulos de las ramas entre si)
        diametro_nivel(Rango de longitud entre cada nivel de profundidad)
        diametro_tronco(Grosor de la rama)
        ramificaciones(Rango de la cantidad de ramas a dibujar)
        decremento_pro(Rango de decrementación de la longitud)
        rango_pro(Rango de la profundidad)
    Funcionalidad:
        Dibujar el fractal en la pantalla de pygame
    Salida:
        None
    '''
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
        pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2), diametro_tronco)
        while ramas > 0:
           angulo_aux2 *= choice([-1, 1])
           angulo_aux = angulo_aux2 * random.randrange(ramasR)           
           dibujarArbol(x2, y2, angulo + angulo_aux , profundidad - decremento_proR,angulo_de_ramificaciones,diametro_nivel,diametro_tronco-1,ramificaciones,decremento_pro,rango_pro)           
           ramas = ramas - 1
           
        
def input(event):
    '''
    Entradas:
        event(Evento de cierre)
    Funcionalidad:
        Cerrar la ventana de pygame
    Salida:
        None
    '''
    if event.type == pygame.QUIT:
        exit(0)

def generacion_de_fractales(angulo1,angulo2,diametronivel1,diametronivel2,grozor1,grozor2,ramificacion1,ramificacion2,decremento1,decremento2,profundidad1,profundidad2,nombre_imagen,padre,madre,nivel_gen):
    '''
    Entradas:
        angulo1,angulo2 (Rango de ángulos de las ramas entre si)
        diametronivel1,diametronivel2 (Rango de longitud entre cada nivel de profundidad)
        grozor1,grozor2 (Rango de grosor de la rama)
        ramificacion1,ramificacion2 (Rango de la cantidad de ramas a dibujar)
        decremento1,decremento2 (Rango de decrementación de la longitud)
        profundidad1,profundidad2 (Rango de la profundidad)
        nombre_imagen (Nombre del fractal a generar)
        padre (Padre que se uso para generar el fractal)
        madre (Madre que se uso para generar el fractal)
        nivel_gen (Nivel de generación)
        
        
    Funcionalidad:
        Generar fractales y guardarlos en una imagen
        
    Salida:
        None
    '''
    gen = []
    screen.fill((255,255,255))
    dibujarArbolAux(300, 550, -90,
        [angulo1,angulo1+angulo2],[diametronivel1,diametronivel2],
        [grozor1,grozor2],[ramificacion1,ramificacion2],
        [decremento1,decremento2],[profundidad1,profundidad2])
    pygame.image.save(screen,carpeta+"\\"+nombre_imagen+".bmp")
    gen.append([nombre_imagen,[angulo1,angulo1+angulo2],[diametronivel1,diametronivel2],[grozor1,grozor2],
                [ramificacion1,ramificacion2],[decremento1,decremento2],[profundidad1,profundidad2],
                 [padre,madre]
                ])
    generaciones[nivel_gen] += gen
    
    
def creacion_pobla_ini():
    '''
    Entradas:
        None
    Funcionalidad:
        Crear la población inicial para el algoritmo genético
    Salida:
        None
    '''
    n = 0
    while n < 10:
        angulo1 = random.randint(1, 90)
        angulo2= random.randint(1,90)
        diametronivel1 = random.randint(4, 4)
        diametronivel2= random.randint(diametronivel1,4)
        grozor1 = random.randint(4, 10)
        grozor2= random.randint(grozor1,10)
        ramificacion1 = random.randint(1, 7)
        ramificacion2= random.randint(ramificacion1,7)
        decremento1 = random.randint(1,1)
        decremento2= random.randint(decremento1,1)
        profundidad1 = random.randint(3, 7)
        profundidad2= random.randint(profundidad1,7)
        generacion_de_fractales(angulo1,angulo2,diametronivel1,diametronivel2,grozor1,grozor2,ramificacion1,ramificacion2,decremento1,decremento2,profundidad1,profundidad2,imagenames[n],n,n,0)
        n = n+1



def fitness(ruta_figura,nombre_imagen):
    '''
    Entradas:
        ruta_figura (figura a la que queremos que se parezca el fractal)
        nombre_imagen (fractal al que compararemos con la figura)
    Funcionalidad:
        Sacar un valor entre 0 y 1 de que tan parecida es la imagen(nombre_imagen) a la figura(ruta_figura)
        Siendo 1 totalmente iguales y 0 totalmente diferentes
    Salida:
        fitness
    '''
    fitness = 0
    im = Image.open(ruta_figura)
    im = im.resize((300,300), Image.ANTIALIAS)
    arrayIm = np.array(im)
    
    im2 = Image.open(nombre_imagen)
    im2 = im2.resize((300,300), Image.ANTIALIAS)
    arrayIm2 = np.array(im2)
    
    fila = 0
    columna = 0
    puntIgua = 0
    puntIguab = 0
    punt = 0
    color = 0
    change = 0
    while fila < 300:
        while columna < 300:
            color = arrayIm[fila][columna][0]            
            if color == 0:
                change = 1            
            if change == 1:
                punt += 1
                if color  == arrayIm2[fila][columna][0]:
                    puntIgua += 1                  
            columna += 1
        columna = 0
        fila += 1
    fitness = ((puntIgua)*100)/punt/100
    return fitness






#Programa principal

## Main
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
imagenames = ["A","B","C","D","E","F","G","H","I","J"]
generaciones =[[]]
'''
generaciones:
    [
Nivel de población 0 ->  [Nombre, [34, 98], [4, 4], [6, 7], [2, 7], [1, 1], [4, 6], [0, 0]]
Nivel de población 1 ->  ['A', [34, 98], [4, 4], [6, 7], [2, 7], [1, 1], [4, 6], [0, 0]]
    ]
'''

carpeta = "Poblacion"     
try:
    mkdir(carpeta)
except:
    print("Carpeta "+carpeta+" Creada")
    
creacion_pobla_ini()

def seleccion(niv_gen,nomb_fig):
    fractal_num=0
    avr = 0
    while fractal_num < 9:
        porcentaje = fitness(nomb_fig,carpeta+"\\"+generaciones[niv_gen][fractal_num][0]+".bmp")
        if porcentaje > 0.75:
            avr += 1-(((porcentaje-1)*4)*-1)
        fractal_num += 1        
    fractal_num=0
    while fractal_num < 9:
        porcentaje = fitness(nomb_fig,carpeta+"\\"+generaciones[niv_gen][fractal_num][0]+".bmp")
        if porcentaje > 0.75:
            generaciones[niv_gen][fractal_num].append(round(((1-(((porcentaje-1)*4)*-1))/avr), 3))
        else:
            generaciones[niv_gen][fractal_num].append(0)
        fractal_num += 1


nomb_fig = "Figuras/Fig1.bmp"
niv_gen = 0

seleccion(niv_gen,nomb_fig)

i= 0
while i < 9:
    print(generaciones[0][i])
    i += 1









