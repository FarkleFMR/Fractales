  
#Creado por Leonardo Fariña y Murillo Aldecoba
#Fecha de creación: 25/05/2020 10:10 pm
#Última modificación: 07/06/2020 23:47 pm
#Versión 3.9.2

#Importación de librerias


import pygame, math
import numpy as np

import random
from random import choice

import time

import os                           #Funciones sistema
from os import mkdir                #Crear carpeta
from shutil import rmtree           #Para borrar una carpeta

import copy                         #Para copiar listas
import tkinter as tk                #Interfaz
from tkinter import ttk
from tkinter import *           
from tkinter import filedialog      #Importa para escoger archivos
from functools import partial       #Importa para pasar parametros por botones
from PIL import Image, ImageTk      #Importa para poner imagenes

import pickle                       #Importamos para manjeo de archivos en binario

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
           angulo_aux = angulo_aux2 * random.randrange(ramasR)#ramas#         
           dibujarArbol(x2, y2, angulo + angulo_aux , profundidad - decremento_proR,angulo_de_ramificaciones,diametro_nivel,diametro_tronco-1,ramificaciones,decremento_pro,rango_pro)           
           ramas -= 1
           
        
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
        [angulo1,angulo2],[diametronivel1,diametronivel2],
        [grozor1,grozor2],[ramificacion1,ramificacion2],
        [decremento1,decremento2],[profundidad1,profundidad2])
    
    ima_salida = pygame.transform.scale(screen, (300, 300))
    pygame.image.save(ima_salida,carpeta+"/"+nombre_imagen+".bmp")
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
        angulo2= random.randint(angulo1,120)
        diametronivel1 = random.randint(2, 6)
        diametronivel2= random.randint(diametronivel1,6)
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



def fitness(arrayIm,nombre_imagen):
    '''
    Entradas:
        arrayIm (array con la figura a comparar)
        nombre_imagen (fractal al que compararemos con la figura)
    Funcionalidad:
        Sacar un valor entre 0 y 1 de que tan parecida es la imagen(nombre_imagen) a la figura(ruta_figura)
        Siendo 1 totalmente iguales y 0 totalmente diferentes
    Salida:
        fitness
    '''
    fitness = 0    
    im2 = Image.open(nombre_imagen)
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
                punt += 10
                if arrayIm2[fila][columna][0] == color:
                    puntIgua += 10
                    if color == 0:
                        puntIgua += 10
                        
                if arrayIm2[fila][columna][0] != color:
                    puntIgua -= 20                                                         
                
                    
            columna += 1
        columna = 0
        fila += 1
    fitness = ((puntIgua)*100)/punt/100
    if fitness <= 0:
        fitness = 0.001
    if fitness > 1:
        fitness = 1
        
    return fitness


def ingresar_indi(nuev_indiv,niv_gen):
    '''
    Entradas:
        nuev_indiv (Individuo verificado)
        niv_gen (nivel de generación del individuo)
    Funcionalidad:
        Extraer los datos del nuevo individuo y hacer la llamada de la función generacion_de_fractales()
        con los parametros extraidos
    Salida:
        None
    '''
    print("Ingr ",nuev_indiv)
    generacion_de_fractales(nuev_indiv[1][0],nuev_indiv[1][1],
                            nuev_indiv[2][0],nuev_indiv[2][1],
                            nuev_indiv[3][0],nuev_indiv[3][1],
                            nuev_indiv[4][0],nuev_indiv[4][1],
                            nuev_indiv[5][0],nuev_indiv[5][1],
                            nuev_indiv[6][0],nuev_indiv[6][1],
                            nuev_indiv[0],
                            nuev_indiv[-1][0],nuev_indiv[-1][1],
                            niv_gen)


    
def verifica_param(nuev_individuo):
    '''
    Entradas:
        nuev_individuo (Individuo con los cromosomas cambiados)
    Funcionalidad:
        Verificar que los parametros sean aceptados para la creación del fractal
        y modificarlos de ser necesario
    Salida:
        nuev_indiv (Individuo con los parametros verificados)
    '''
    # Comentario no se pudo asignar variables a nuevo_indi[indice][0] y nuevo_indi[indice][1] para hacer un código más
    # limpio, ya que por alguna razon que no se encontro en la documentación de python dejaban de funcionar las comparaciones
    nuevo_indi = nuev_individuo[:]    
    aux_temp = 0
    indice = 1
    while indice < 7:                
        if nuevo_indi[indice][0] < 1:
            nuevo_indi[indice][0] = 1
        if nuevo_indi[indice][1] < 1:
            nuevo_indi[indice][1] = 1
                
        if nuevo_indi[indice][1] < nuevo_indi[indice][0]:
            aux_temp = nuevo_indi[indice][1]
            nuevo_indi[indice][1] = nuevo_indi[indice][0]
            nuevo_indi[indice][0] = aux_temp
                
        if indice == 1:
            if nuevo_indi[indice][0] > 120:
                nuevo_indi[indice][0] = 120
            if nuevo_indi[indice][1] > 120:
                nuevo_indi[indice][1] = random.randint(nuevo_indi[indice][0],120) 
                
        if indice == 2:
            if nuevo_indi[indice][0] < 2:
                nuevo_indi[indice][0] = 2
            if nuevo_indi[indice][1] < 2:
                nuevo_indi[indice][1] = 2
                
            if nuevo_indi[indice][0] > 6:
                nuevo_indi[indice][0] = 6
            if nuevo_indi[indice][1] > 6:
                nuevo_indi[indice][1] = 6
                
                
        if indice == 3:
            if nuevo_indi[indice][0] < 4:
                nuevo_indi[indice][0] = 4
            if nuevo_indi[indice][1] < 4:
                nuevo_indi[indice][1] = 4

            if nuevo_indi[indice][0] > 10:
                nuevo_indi[indice][0] = 10
            if nuevo_indi[indice][1] > 10:
                nuevo_indi[indice][1] = 10
                
        if indice == 4:
            if nuevo_indi[indice][0] > 7:
                nuevo_indi[indice][0] = 7
            if nuevo_indi[indice][1] > 7:
                nuevo_indi[indice][1] = 7
                
        if indice == 5:
            nuevo_indi[indice][0] = 1
            nuevo_indi[indice][1] = 1
            
        if indice == 6:            
            if nuevo_indi[indice][0] < 3:
                nuevo_indi[indice][0] = 3
            if nuevo_indi[indice][1] < 3:
                nuevo_indi[indice][1] = 3

            if nuevo_indi[indice][0] > 7:
                nuevo_indi[indice][0] = 7
            if nuevo_indi[indice][1] > 7:
                nuevo_indi[indice][1] = 7
                
        indice += 1
    return nuevo_indi


def cruce(padre,madre,gen,aux_nom):
    '''
    Entradas:
        padre (la posición que ocupa en la generación)
        madre (la posición que ocupa en la generación)
        gen (generación a la que pertenecen los padres)
        aux_nom (auxiliar para poner un nombre al fractal)
    Funcionalidad:
        Hacer el cruce de los cromosomas entre el padre y la madre
        Aplicarle un pequeña mutación
        Ingresar nuevos individuos a la siguiente generación
    Salida:
        None
    '''    
    # Largo de bits de cada individuo
    longi_bits_pa = 0
    longi_bits_ma = 0

    # Replicamos los individuos con un nombre nuevo, un padre nuevo,un madre nueva y los parametros en binario
    nuevos_indvs = []
    pa_ma = padre
    aux = 0
    while aux < 2:
        nuev_indv = []
        if aux == 0:
            nuev_nom = str(gen+1)+chr(64+aux_nom+1)+str(aux_nom)
        else:
            nuev_nom = str(gen+1)+chr(64+aux_nom+6)+str(aux_nom+5)
        nuev_indv.append(nuev_nom)
        indice = 1
        while indice < 7:
                nuev_indv.append([bin(generaciones[gen][pa_ma][indice][0]),
                                  bin(generaciones[gen][pa_ma][indice][1])]
                                 )                    
                if aux == 0:
                    longi_bits_pa += len(str(nuev_indv[indice][0])[2:])
                    longi_bits_pa += len(str(nuev_indv[indice][1])[2:])
                else:
                    longi_bits_ma += len(str(nuev_indv[indice][0])[2:])
                    longi_bits_ma += len(str(nuev_indv[indice][1])[2:])
                    
                indice += 1
        nuev_indv.append([padre,madre])
        pa_ma = madre
        aux += 1
        nuevos_indvs.append(nuev_indv)

    #Proceso de cambio de cromosomas   
    #Nos fijamos cual va a ser el rango de bits a cambiar
    rang_max_crom = 0
    if longi_bits_pa <= longi_bits_ma:
        rang_max_crom = longi_bits_pa
    else:
        rang_max_crom = longi_bits_ma
    chan_crom = random.randint(1,rang_max_crom)


    while chan_crom > 0:
        indice = 1
        while indice < 7:
            parametro = 0
            while parametro < 2:
                param_0 = nuevos_indvs[0][indice][parametro]
                param_1 = nuevos_indvs[1][indice][parametro]
                long_par_0 = len(str(param_0)[2:])
                long_par_1 = len(str(param_1)[2:])
                if long_par_0 == long_par_1:
                    temp_aux = param_0
                    nuevos_indvs[0][indice][parametro] = param_1
                    nuevos_indvs[1][indice][parametro] = temp_aux
                    chan_crom -= long_par_0
                elif long_par_0 < long_par_1:                
                    temp_aux = param_0
                    nuevos_indvs[0][indice][parametro] = param_1
                    nuevos_indvs[1][indice][parametro] = temp_aux
                    chan_crom -= long_par_1
                else:                                
                    temp_aux = param_0
                    nuevos_indvs[0][indice][parametro] = param_1
                    nuevos_indvs[1][indice][parametro] = temp_aux
                    chan_crom -= long_par_0   
                parametro += 1
            indice += 1


    #Pasamos todos los parametros de binario a enteros
    aux = 0
    while aux < 2:
        #Mutación
        muta_0 = 0
        muta_1 = 0
        indice_mut_1 = 0
        indice_mut_0 = 0
        #if generaciones[gen][padre][-2] < 0.75 and generaciones[gen][madre][-2] < 0.75:        
        indice_mut_1 = random.randint(1,10)
        indice_mut_0 = random.randint(1,10)
            
        indice = 1
        while indice < 7:
            num_random_ = random.randint(1,6)
            if indice_mut_0 == num_random_:
                muta_0 = random.randint(1,2) * (random.choice([-1,1]))
                indice_mut_0 = 0
            num_random_ = random.randint(1,6)
            if indice_mut_1 == num_random_:
                muta_1 = random.randint(1,2) * (random.choice([-1,1]))
                indice_mut_1 = 0

            if indice == 1:
                muta_0 = 5*muta_0*random.randint(1,4) 
                muta_1 = 5*muta_1*random.randint(1,4)
                
                
            nuevos_indvs[aux][indice][0] = int(nuevos_indvs[aux][indice][0],2)+muta_0
            nuevos_indvs[aux][indice][1] = int(nuevos_indvs[aux][indice][1],2)+muta_1

            muta_0 = 0
            muta_1 = 0
            indice += 1
        aux += 1
    #Nos fijamos si ya tenemos la nueva generación
    try:
        basu = generaciones[gen+1]
    except:
        generaciones.append([])

    #Verificamos los parametros de los individuos
    list_0 = nuevos_indvs[0][:]
    list_1 = nuevos_indvs[1][:]
    hijo_0 = verifica_param(list_0)
    hijo_1 = verifica_param(list_1)    

    #Ingresamos los individuos
    ingresar_indi(hijo_0,gen+1)
    ingresar_indi(hijo_1,gen+1)
       

def padres(padre,gen):
    '''
    Entradas:
        padre (valor entre 0 y 1)
        gen (generación a la que pertenecen los padres)
    Funcionalidad:
        Elegir un padre o madre para un nuevo fractal
    Salida:
        pa_ma (la posición que ocupa en la generación)
    '''
    pa_ma = 0
    temp_normal = 0
    pos_pa_ma = 0
    while pos_pa_ma < 10:
        temp_normal += generaciones[gen][pos_pa_ma][-2]
        if padre < temp_normal:            
            pa_ma = pos_pa_ma
            break        
        pos_pa_ma += 1        
    return pa_ma



    
def seleccion(niv_gen,arrayIm):
    '''
    Entradas:
        niv_gen (nivel de la generacion a seleccionar)
        arrayIm (array con la figura a comparar)
    Funcionalidad:
        Utilizar la función de fitness(), normalizar los valores y agregarlos en los individuos.
    Salida:
        None
    '''
    mat_por = []
    fractal_num=0
    avr = 0
    while fractal_num < 10:
        porcentaje = fitness(arrayIm,carpeta+"\\"+generaciones[niv_gen][fractal_num][0]+".bmp")
        porcentaje = (porcentaje-0.8)*5
        if porcentaje < 0:
            porcentaje = 0.001
        mat_por.append(porcentaje)       
        
        if porcentaje > 0.90:
            decim = 0.09
            aux = 12
            while decim >= -0.01:
                suma = (0.90+decim)
                if porcentaje >= suma:
                    avr += round((porcentaje*(4**30)**aux),5)
                    decim = -1
                aux -= 1
                decim -= 0.01                
        elif porcentaje > 0.85:
            avr += round((porcentaje*(4**20)),5)
        elif porcentaje > 0.80:
            avr += round((porcentaje*(4**15)),5)
        elif porcentaje > 0.75: 
            avr += round((porcentaje*(4**10)),5)
        elif porcentaje > 0.70:
            avr += round((porcentaje*(4**8)),5)
        elif porcentaje > 0.65:
            avr += round((porcentaje*(4**7)),5)
        elif porcentaje > 0.60:
            avr += round((porcentaje*(4**6)),5)
        elif porcentaje > 0.50:
            avr += round((porcentaje*(4**5)),5)
        elif porcentaje > 0.40:
            avr += round((porcentaje*(4**4)),5)
        elif porcentaje > 0.30:
            avr += round((porcentaje*(4**3)),5)
        elif porcentaje > 0.20:
            avr += round((porcentaje*(4**2)),5)
        elif porcentaje > 0.10:
            avr += round((porcentaje*(4**1)),5)    
        else:
            avr += porcentaje
        fractal_num += 1        

    fractal_num=0
    while fractal_num < 10:
        porcentaje = mat_por[fractal_num]
        
        if porcentaje > 0.90:
            decim = 0.09
            aux = 12
            while decim >= -0.01:
                suma = (0.90+decim)
                if porcentaje >= suma:
                    generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**30)**aux)/avr,3))
                    decim = -1
                aux -= 1
                decim -= 0.01                
        elif porcentaje > 0.85:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**20))/avr, 3))
        elif porcentaje > 0.80:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**15))/avr, 3))
        elif porcentaje > 0.75:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**10))/avr, 3))
        elif porcentaje > 0.70:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**8))/avr, 3))
        elif porcentaje > 0.65:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**7))/avr, 3))
        elif porcentaje > 0.60:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**6))/avr, 3))
        elif porcentaje > 0.50:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**5))/avr, 3))
        elif porcentaje > 0.40:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**4))/avr, 3))
        elif porcentaje > 0.30:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**3))/avr, 3))      
        elif porcentaje > 0.20:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**2))/avr, 3))        
        elif porcentaje > 0.10:
            generaciones[niv_gen][fractal_num].append(round((porcentaje*(4**1))/avr, 3))
        else:
            generaciones[niv_gen][fractal_num].append(porcentaje/avr)
            
        generaciones[niv_gen][fractal_num].append(porcentaje)     
        print("Fractal ",generaciones[niv_gen][fractal_num][0]," tiene un % de ",generaciones[niv_gen][fractal_num][-1], "normalizado queda ",generaciones[niv_gen][fractal_num][8])
        fractal_num += 1
    print("\n---------------\n")


def buscar_figura(arrayIm):
    '''
    Entradas:
        arrayIm (array con la figura a comparar)
    Funcionalidad:
        Utilizar el algoritmo génetico para llegar a un nivel de población parecido al de la figura(nomb_fig)
    Salida:
        None
    '''
    niv_gen = 0
    aux = 0
    bandera = 0
    while aux == 0:    
        seleccion(niv_gen,arrayIm)
        
        if niv_gen != 0:
            num_f = 0
            while num_f < 10:
                if generaciones[niv_gen][num_f][-1] >= 0.75: #(generaciones[niv_gen][0][-2] <= generaciones[niv_gen][num_f][-2])and(generaciones[niv_gen][0][-2] >= generaciones[niv_gen][num_f][-2]-0.03) and 
                    bandera = 1
                else:
                    bandera = 0
                    break
                num_f += 1

        if bandera == 1:        
            print("\n\n\n\n\n\n\n\n------------------------------Encontrado\n\n\n\n\n\n")
            aux = 1
            break

            
        nueva_fra = 0
        while nueva_fra < 5:
            pad = padres(random.random(),niv_gen)        
            mad = padres(random.random(),niv_gen)
            cruce(pad,mad,niv_gen,nueva_fra)            
            nueva_fra += 1
            
        niv_gen += 1
        if niv_gen == 4000:
            print("\n\n\n\n\n\n\n\n------------------------------NO Encontrado\n\n\n\n\n\n")
            break


def crear_car(carpeta):
    '''
    Entradas:
        carpeta (string, nombre de la carpeta a crear)
    Funcionalidad:
        Crear una carpeta con el nombre que contiene 'carpeta'
    Salida:
        None
    '''
    try:
        mkdir(carpeta)
        print("\n Se creó la carpeta "+carpeta+" \n")
    except:
        print("\n Carpeta "+carpeta+" ya Creada \n")



    



def menu(estado):
    #Recibe el path de la silueta,menu para escoger ver la poblacion inicial o
    #ver las generaciones, tambien va a correr el algortimo principal
    def volver():#Vuelve a la ventana de elegir silueta
        poblacion.destroy()
        if estado == 1:
            elegir_silueta()
        else:
            cargar()
            
    def ver_poblacion():
        global arbolactual
        global hijo
        global hijobtn
        global hijol
        arbolactual = 0
        hijo = []
        
        def verhijos(hijos):
            global hijoactual
            hijoactual = 0
            global total
            total = len(hijos)-1
            def volver():
                hijo.destroy()
                inicial.deiconify()
            def anterior():
                global hijoactual
                global total
                if hijoactual == 0:
                    hijoactual = total
                else:
                    hijoactual -=1
                images = Image.open("Poblacion/"+hijos[hijoactual]+".bmp")
                smallimg = images.resize((300,300))
                image = ImageTk.PhotoImage(smallimg)
                canvas=Canvas(master=hijo,width=300,height=300)
                canvas.place(x=120,y=20)
                canvas.image = image
                canvas.create_image(0,0,image = image,anchor = "nw")
            def siguiente():
                global hijoactual
                global total
                if hijoactual == total:
                    hijoactual = 0
                else:
                    hijoactual +=1
            
                images = Image.open("Poblacion/"+hijos[hijoactual]+".bmp")
                smallimg = images.resize((300,300))
                image = ImageTk.PhotoImage(smallimg)
                canvas=Canvas(master=hijo,width=300,height=300)
                canvas.place(x=120,y=20)
                canvas.image = image
                canvas.create_image(0,0,image = image,anchor = "nw")
            inicial.withdraw()
            hijo = Toplevel(inicial)
            hijo.geometry("600x600")
            
            images = Image.open("Poblacion/"+hijos[hijoactual]+".bmp")
            smallimg = images.resize((300,300))
            image = ImageTk.PhotoImage(smallimg)
            canvas=Canvas(master=hijo,width=300,height=300)
            canvas.place(x=120,y=20)
            canvas.image = image
            canvas.create_image(0,0,image = image,anchor = "nw")
            
            backbtn = Button(master=hijo,
                     bg = "red",
                     text = "Volver",
                     width = 5,
                     height = 3,
                     command = volver)
            backbtn.place(x=10,y=350)
            antbtn = Button(master=hijo,
                     bg = "red",
                     text = "Anterior",
                     width = 10,
                     height = 3,
                     command = anterior)
            antbtn.place(x=10,y=150)
            sigbtn = Button(master=hijo,
                         bg = "light green",
                         text = "Siguiente",
                         width = 10,
                         height = 3,
                         command = siguiente)
            sigbtn.place(x=450,y=150)
        
        def volver():
            inicial.destroy()
            poblacion.deiconify()
        def anterior():
            global arbolactual
            global hijo
            global hijobtn
            global hijol
            if arbolactual == 0:
                arbolactual = 9
            else:
                arbolactual -=1
            
            images = Image.open("Poblacion/"+generaciones[0][arbolactual][0]+".bmp")
            smallimg = images.resize((300,300))
            image = ImageTk.PhotoImage(smallimg)
            canvas=Canvas(master=inicial,width=300,height=300)
            canvas.place(x=120,y=20)
            canvas.image = image
            canvas.create_image(0,0,image = image,anchor = "nw")
            fitlabel.configure(text="Fitness: "+ str(generaciones[0][arbolactual][-1]))
            fitlabel.update()
            angulolabel.configure(text ="Rango del angulo: "+ str(generaciones[0][arbolactual][1]))
            angulolabel.update()
            diametrolabel.configure(text ="Rango del diamtro: "+ str(generaciones[0][arbolactual][2]))
            diametrolabel.update()
            grozorlabel.configure(text ="Rango del grozor del tronco: "+ str(generaciones[0][arbolactual][3]))
            grozorlabel.update()
            longitudlabel.configure(text ="Rango de las ramificaciones: "+ str(generaciones[0][arbolactual][4]))
            longitudlabel.update()
            decrementolabel.configure(text ="Rango del decremento de profundidad: "+ str(generaciones[0][arbolactual][5]))
            decrementolabel.update()
            profundidadlabel.configure(text ="Rango de la profundidad: "+ str(generaciones[0][arbolactual][6]))
            profundidadlabel.update()
            hijobtn.place_forget()
            hijol.place_forget()
            hijo = []
            for i in range(10):
                if generaciones[1][i][7][0] == arbolactual or generaciones[1][i][7][1] == arbolactual:
                    hijo+=[generaciones[1][i][0]]
            if len(hijo) > 0:
                hijobtn.configure(command=partial(verhijos,hijo))
                hijobtn.place(x=10,y=500)
            else:
                hijol.place(x=150,y=560)
            
        def siguiente():
            global arbolactual
            global hijo
            global hijobtn
            global hijol
            if arbolactual == 9:
                arbolactual = 0
            else:
                arbolactual +=1
            
            images = Image.open("Poblacion/"+generaciones[0][arbolactual][0]+".bmp")
            smallimg = images.resize((300,300))
            image = ImageTk.PhotoImage(smallimg)
            canvas=Canvas(master=inicial,width=300,height=300)
            canvas.place(x=120,y=20)
            canvas.image = image
            canvas.create_image(0,0,image = image,anchor = "nw")
            fitlabel.configure(text="Fitness: "+ str(generaciones[0][arbolactual][-1]))
            fitlabel.update()
            angulolabel.configure(text ="Rango del angulo: "+ str(generaciones[0][arbolactual][1]))
            angulolabel.update()
            diametrolabel.configure(text ="Rango del diamtro: "+ str(generaciones[0][arbolactual][2]))
            diametrolabel.update()
            grozorlabel.configure(text ="Rango del grozor del tronco: "+ str(generaciones[0][arbolactual][3]))
            grozorlabel.update()
            longitudlabel.configure(text ="Rango de las ramificaciones: "+ str(generaciones[0][arbolactual][4]))
            longitudlabel.update()
            decrementolabel.configure(text ="Rango del decremento de profundidad: "+ str(generaciones[0][arbolactual][5]))
            decrementolabel.update()
            profundidadlabel.configure(text ="Rango de la profundidad: "+ str(generaciones[0][arbolactual][6]))
            profundidadlabel.update()
            hijobtn.place_forget()
            hijol.place_forget()
            hijo = []
            for i in range(10):
                if generaciones[1][i][7][0] == arbolactual or generaciones[1][i][7][1] == arbolactual:
                    hijo+=[generaciones[1][i][0]]
            if len(hijo) > 0:
                hijobtn.configure(command=partial(verhijos,hijo))
                hijobtn.place(x=10,y=500)
            else:
                hijol.place(x=150,y=560)
            hijo = hijo



        
        poblacion.withdraw()
        inicial = Toplevel(poblacion)
        inicial.geometry("600x600")
        images = Image.open("Poblacion/"+generaciones[0][arbolactual][0]+".bmp")
        smallimg = images.resize((300,300))
        image = ImageTk.PhotoImage(smallimg)
        canvas=Canvas(master=inicial,width=300,height=300)
        canvas.place(x=120,y=20)
        canvas.image = image
        canvas.create_image(0,0,image = image,anchor = "nw")
        
        
        for i in range(10):
            if generaciones[1][i][7][0] == arbolactual or generaciones[1][i][7][1] == arbolactual:
                hijo+=[generaciones[1][i][0]]
        hijobtn = Button(master=inicial,
                        text = "Ver hijos",
                        width = 10,
                        height = 3,
                        command = partial(verhijos,hijo))
        hijobtn.place(x=10,y=500)
        hijol = Label(master=inicial,text="No tiene hijos")
        hijol.place(x=150,y=560)
        if len(hijo) > 0:
            hijol.place_forget()
        else:
            hijobtn.place_forget()
        
        backbtn = Button(master=inicial,
                     bg = "red",
                     text = "Volver",
                     width = 10,
                     height = 3,
                     command = volver)
        backbtn.place(x=10,y=440)
        antbtn = Button(master=inicial,
                     bg = "red",
                     text = "Anterior",
                     width = 10,
                     height = 3,
                     command = anterior)
        antbtn.place(x=10,y=150)
        sigbtn = Button(master=inicial,
                     bg = "light green",
                     text = "Siguiente",
                     width = 10,
                     height = 3,
                     command = siguiente)
        sigbtn.place(x=450,y=150)
        fitlabel = Label(master=inicial,text ="Fitness: "+ str(generaciones[0][arbolactual][-1]))
        fitlabel.place(x=150,y=350)
        angulolabel = Label(master=inicial,text ="Rango del angulo: "+ str(generaciones[0][arbolactual][1]))
        angulolabel.place(x=150,y=380)
        diametrolabel = Label(master=inicial,text ="Rango del diamtro: "+ str(generaciones[0][arbolactual][2]))
        diametrolabel.place(x=150,y=410)
        grozorlabel = Label(master=inicial,text ="Rango del grozor del tronco: "+ str(generaciones[0][arbolactual][3]))
        grozorlabel.place(x=150,y=440)
        longitudlabel = Label(master=inicial,text ="Rango de las ramificaciones: "+ str(generaciones[0][arbolactual][4]))
        longitudlabel.place(x=150,y=470)
        decrementolabel = Label(master=inicial,text ="Rango del decremento de profundidad: "+ str(generaciones[0][arbolactual][5]))
        decrementolabel.place(x=150,y=500)
        profundidadlabel = Label(master=inicial,text ="Rango de la profundidad: "+ str(generaciones[0][arbolactual][6]))
        profundidadlabel.place(x=150,y=530)

    def ver_generacion():
        def volver():
            gen.destroy()
            poblacion.deiconify()
        def ver():
            global arbolactual
            global hijo
            global hijobtn
            global hijol
            arbolactual = 0
            hijo = []
            def verpadres():
                global arbolactual
                def volver():
                    padres.destroy()
                    info.deiconify()
                info.withdraw()
                padres=Toplevel(info)
                padres.geometry("800x600")
                padre = generaciones[int(generacion.get())][arbolactual][7][0]
                madre = generaciones[int(generacion.get())][arbolactual][7][1]
                imagesp = Image.open("Poblacion/"+generaciones[int(generacion.get())-1][padre][0]+".bmp")
                smallimgp = imagesp.resize((300,300))
                imagep = ImageTk.PhotoImage(smallimgp)
                canvas=Canvas(master=padres,width=300,height=300)
                canvas.place(x=40,y=20)
                canvas.image = imagep
                canvas.create_image(0,0,image = imagep,anchor = "nw")
                imagesm = Image.open("Poblacion/"+generaciones[int(generacion.get())-1][madre][0]+".bmp")
                smallimgm = imagesm.resize((300,300))
                imagem = ImageTk.PhotoImage(smallimgm)
                canvas=Canvas(master=padres,width=300,height=300)
                canvas.place(x=420,y=20)
                canvas.image = imagem
                canvas.create_image(0,0,image = imagem,anchor = "nw")
                backbtn = Button(master=padres,
                         bg = "red",
                         text = "Volver",
                         width = 5,
                         height = 3,
                         command = volver)
                backbtn.place(x=10,y=350)
            def verhijos(hijos):
                global hijoactual
                hijoactual = 0
                global total
                total = len(hijos)-1
                def volver():
                    hijo.destroy()
                    info.deiconify()
                def anterior():
                    global hijoactual
                    global total
                    if hijoactual == 0:
                        hijoactual = total
                    else:
                        hijoactual -=1
                    images = Image.open("Poblacion/"+hijos[hijoactual]+".bmp")
                    smallimg = images.resize((300,300))
                    image = ImageTk.PhotoImage(smallimg)
                    canvas=Canvas(master=hijo,width=300,height=300)
                    canvas.place(x=120,y=20)
                    canvas.image = image
                    canvas.create_image(0,0,image = image,anchor = "nw")
                def siguiente():
                    global hijoactual
                    global total
                    if hijoactual == total:
                        hijoactual = 0
                    else:
                        hijoactual +=1
                
                    images = Image.open("Poblacion/"+hijos[hijoactual]+".bmp")
                    smallimg = images.resize((300,300))
                    image = ImageTk.PhotoImage(smallimg)
                    canvas=Canvas(master=hijo,width=300,height=300)
                    canvas.place(x=120,y=20)
                    canvas.image = image
                    canvas.create_image(0,0,image = image,anchor = "nw")
                info.withdraw()
                hijo = Toplevel(info)
                hijo.geometry("600x600")
                
                images = Image.open("Poblacion/"+hijos[hijoactual]+".bmp")
                smallimg = images.resize((300,300))
                image = ImageTk.PhotoImage(smallimg)
                canvas=Canvas(master=hijo,width=300,height=300)
                canvas.place(x=120,y=20)
                canvas.image = image
                canvas.create_image(0,0,image = image,anchor = "nw")
                
                backbtn = Button(master=hijo,
                         bg = "red",
                         text = "Volver",
                         width = 5,
                         height = 3,
                         command = volver)
                backbtn.place(x=10,y=350)
                antbtn = Button(master=hijo,
                         bg = "red",
                         text = "Anterior",
                         width = 10,
                         height = 3,
                         command = anterior)
                antbtn.place(x=10,y=150)
                sigbtn = Button(master=hijo,
                             bg = "light green",
                             text = "Siguiente",
                             width = 10,
                             height = 3,
                             command = siguiente)
                sigbtn.place(x=450,y=150)
            
            def volver():
                info.destroy()
                gen.deiconify()
            def anterior():
                global arbolactual
                global hijo
                global hijobtn
                global hijol
                if arbolactual == 0:
                    arbolactual = 9
                else:
                    arbolactual -=1
                
                images = Image.open("Poblacion/"+generaciones[int(generacion.get())][arbolactual][0]+".bmp")
                smallimg = images.resize((300,300))
                image = ImageTk.PhotoImage(smallimg)
                canvas=Canvas(master=info,width=300,height=300)
                canvas.place(x=120,y=20)
                canvas.image = image
                canvas.create_image(0,0,image = image,anchor = "nw")
                fitlabel.configure(text="Fitness: "+ str(generaciones[int(generacion.get())][arbolactual][-1]))
                fitlabel.update()
                angulolabel.configure(text ="Rango del angulo: "+ str(generaciones[int(generacion.get())][arbolactual][1]))
                angulolabel.update()
                diametrolabel.configure(text ="Rango del diamtro: "+ str(generaciones[int(generacion.get())][arbolactual][2]))
                diametrolabel.update()
                grozorlabel.configure(text ="Rango del grozor del tronco: "+ str(generaciones[int(generacion.get())][arbolactual][3]))
                grozorlabel.update()
                longitudlabel.configure(text ="Rango de las ramificaciones: "+ str(generaciones[int(generacion.get())][arbolactual][4]))
                longitudlabel.update()
                decrementolabel.configure(text ="Rango del decremento de profundidad: "+ str(generaciones[int(generacion.get())][arbolactual][5]))
                decrementolabel.update()
                profundidadlabel.configure(text ="Rango de la profundidad: "+ str(generaciones[int(generacion.get())][arbolactual][6]))
                profundidadlabel.update()
                hijobtn.place_forget()
                hijol.place_forget()
                hijo = []
                if int(generacion.get())!=len(generaciones)-1:
                    for i in range(10):
                        if generaciones[int(generacion.get())+1][i][7][0] == arbolactual or generaciones[int(generacion.get())+1][i][7][1] == arbolactual:
                            hijo+=[generaciones[int(generacion.get())+1][i][0]]
                if len(hijo) > 0:
                    hijobtn.configure(command=partial(verhijos,hijo))
                    hijobtn.place(x=10,y=410)
                else:
                    hijol.place(x=150,y=560)
                
            def siguiente():
                global arbolactual
                global hijo
                global hijobtn
                global hijol
                if arbolactual == 9:
                    arbolactual = 0
                else:
                    arbolactual +=1
                
                images = Image.open("Poblacion/"+generaciones[int(generacion.get())][arbolactual][0]+".bmp")
                smallimg = images.resize((300,300))
                image = ImageTk.PhotoImage(smallimg)
                canvas=Canvas(master=info,width=300,height=300)
                canvas.place(x=120,y=20)
                canvas.image = image
                canvas.create_image(0,0,image = image,anchor = "nw")
                fitlabel.configure(text="Fitness: "+ str(generaciones[int(generacion.get())][arbolactual][-1]))
                fitlabel.update()
                angulolabel.configure(text ="Rango del angulo: "+ str(generaciones[int(generacion.get())][arbolactual][1]))
                angulolabel.update()
                diametrolabel.configure(text ="Rango del diamtro: "+ str(generaciones[int(generacion.get())][arbolactual][2]))
                diametrolabel.update()
                grozorlabel.configure(text ="Rango del grozor del tronco: "+ str(generaciones[int(generacion.get())][arbolactual][3]))
                grozorlabel.update()
                longitudlabel.configure(text ="Rango de las ramificaciones: "+ str(generaciones[int(generacion.get())][arbolactual][4]))
                longitudlabel.update()
                decrementolabel.configure(text ="Rango del decremento de profundidad: "+ str(generaciones[int(generacion.get())][arbolactual][5]))
                decrementolabel.update()
                profundidadlabel.configure(text ="Rango de la profundidad: "+ str(generaciones[int(generacion.get())][arbolactual][6]))
                profundidadlabel.update()
                hijobtn.place_forget()
                hijol.place_forget()
                hijo = []
                if int(generacion.get())!=len(generaciones)-1:
                    for i in range(10):
                        if generaciones[int(generacion.get())+1][i][7][0] == arbolactual or generaciones[int(generacion.get())+1][i][7][1] == arbolactual:
                            hijo+=[generaciones[int(generacion.get())+1][i][0]]
                if len(hijo) > 0:
                    hijobtn.configure(command=partial(verhijos,hijo))
                    hijobtn.place(x=10,y=410)
                else:
                    hijol.place(x=150,y=560)
                hijo = hijo            
            gen.withdraw()
            info = Toplevel(gen)
            info.geometry("600x600")
            images = Image.open("Poblacion/"+generaciones[int(generacion.get())][arbolactual][0]+".bmp")
            smallimg = images.resize((300,300))
            image = ImageTk.PhotoImage(smallimg)
            canvas=Canvas(master=info,width=300,height=300)
            canvas.place(x=120,y=20)
            canvas.image = image
            canvas.create_image(0,0,image = image,anchor = "nw")
            
            
            if int(generacion.get())!=len(generaciones)-1:
                    for i in range(10):
                        if generaciones[int(generacion.get())+1][i][7][0] == arbolactual or generaciones[int(generacion.get())+1][i][7][1] == arbolactual:
                            hijo+=[generaciones[int(generacion.get())+1][i][0]]
            hijobtn = Button(master=info,
                            text = "Ver hijos",
                            width = 10,
                            height = 3,
                            command = partial(verhijos,hijo))
            hijobtn.place(x=10,y=410)
            hijol = Label(master=info,text="No tiene hijos")
            hijol.place(x=150,y=560)
            padrebtn = Button(master=info,
                            text = "Ver padres",
                            width = 10,
                            height = 3,
                            command = verpadres)
            padrebtn.place(x=10,y=470)

            if len(hijo) > 0:
                hijol.place_forget()
            else:
                hijobtn.place_forget()
            
            backbtn = Button(master=info,
                         bg = "red",
                         text = "Volver",
                         width = 10,
                         height = 3,
                         command = volver)
            backbtn.place(x=10,y=350)
            antbtn = Button(master=info,
                         bg = "red",
                         text = "Anterior",
                         width = 10,
                         height = 3,
                         command = anterior)
            antbtn.place(x=10,y=150)
            sigbtn = Button(master=info,
                         bg = "light green",
                         text = "Siguiente",
                         width = 10,
                         height = 3,
                         command = siguiente)
            sigbtn.place(x=450,y=150)
            fitlabel = Label(master=info,text ="Fitness: "+ str(generaciones[int(generacion.get())][arbolactual][-1]))
            fitlabel.place(x=150,y=350)
            angulolabel = Label(master=info,text ="Rango del angulo: "+ str(generaciones[int(generacion.get())][arbolactual][1]))
            angulolabel.place(x=150,y=380)
            diametrolabel = Label(master=info,text ="Rango del diamtro: "+ str(generaciones[int(generacion.get())][arbolactual][2]))
            diametrolabel.place(x=150,y=410)
            grozorlabel = Label(master=info,text ="Rango del grozor del tronco: "+ str(generaciones[int(generacion.get())][arbolactual][3]))
            grozorlabel.place(x=150,y=440)
            longitudlabel = Label(master=info,text ="Rango de las ramificaciones: "+ str(generaciones[int(generacion.get())][arbolactual][4]))
            longitudlabel.place(x=150,y=470)
            decrementolabel = Label(master=info,text ="Rango del decremento de profundidad: "+ str(generaciones[int(generacion.get())][arbolactual][5]))
            decrementolabel.place(x=150,y=500)
            profundidadlabel = Label(master=info,text ="Rango de la profundidad: "+ str(generaciones[int(generacion.get())][arbolactual][6]))
            profundidadlabel.place(x=150,y=530)





            
        poblacion.withdraw()
        gen = Toplevel(poblacion)
        gen.geometry("200x100")
        opciones=[]
        for i in range(len(generaciones)):
            if i !=0:
                opciones += [str(i)]
        opcion = StringVar(master=gen)
        generacion = ttk.Combobox(master=gen,textvariable=opcion,values=opciones)
        generacion.place(x=10,y=10)
        backbtn = Button(master=gen,
                     bg = "red",
                     text = "Volver",
                     width = 5,
                     height = 2,
                     command = volver)
        backbtn.place(x=10,y=40)

        gobtn = Button(master=gen,
                     bg = "light green",
                     text = "Ver",
                     width = 5,
                     height = 2,
                     command = ver)
        gobtn.place(x=100,y=40)
        
        
        
    poblacion = Toplevel(window)
    poblacion.geometry("280x280")
    backbtn = Button(master=poblacion,
                     bg = "red",
                     text = "Volver",
                     width = 20,
                     height = 3,
                     command = volver)
    backbtn.place(x=60,y=190)
    pbibtn = Button(master=poblacion,
                     bg = "gray",
                     text = "Ver Poblacion inicial",
                     width = 20,
                     height = 3,
                     command = ver_poblacion)
    pbibtn.place(x=60,y=50)
    pbibtn = Button(master=poblacion,
                     bg = "gray",
                     text = "Ver Generaciones",
                     width = 20,
                     height = 3,
                     command =ver_generacion)
    pbibtn.place(x=60,y=120)
    
    
    
def elegir_silueta():
    #Abre el menu para escoger la imagen desde archivos
    window.withdraw()
    archivo = ""
    def volver():#Vuelve al menu principal
        poblacion.destroy()
        window.deiconify()
    def seleccionar_img():
        #Abre mis archivos para escoger la silueta del arbol y una vez elegida
        #la coloca en la ventana
        global archivo
        archivo = filedialog.askopenfilename(title="abrir")#Abre mis archivos
        images = Image.open(archivo)
        smallimg = images.resize((300,300))
        image = ImageTk.PhotoImage(smallimg)
        canvas=Canvas(master=poblacion,width=300,height=300)
        canvas.place(x=100,y=20)
        canvas.image = image
        canvas.create_image(0,0,image = image,anchor = "nw")
    def continuar_aux():
        # Lleva al menu de ver poblacion y generacion
        #Recibe el path de la silueta
        #Se inicia el programa
        global archivo
        generaciones =[[]]
        for file in os.listdir("Poblacion"):
            os.remove(f'Poblacion/{file}')
        creacion_pobla_ini()
        im = Image.open(archivo)   
        arrayim = np.array(im)
        buscar_figura(arrayim)
        poblacion.destroy()
        menu(1)
    poblacion = Toplevel(window)
    poblacion.geometry("500x400")
    marco = Frame(master=poblacion,width=300,height=300,bd=20,relief="groove")
    marco.place(x=100,y=20)
    backbtn = Button(master=poblacion,
                     bg = "red",
                     text = "Volver",
                     width = 5,
                     height = 2,
                     command = volver)
    backbtn.place(x=20,y=340)
    selecarch = Button(master=poblacion,
                     bg = "gray",
                     text = "Seleccionar silueta",
                     width = 30,
                     height = 3,
                     command = seleccionar_img)
    selecarch.place(x=130,y=330)
    conbtn = Button(master=poblacion,
                     bg = "light green",
                     text = "Continuar",
                     width = 7,
                     height = 2,
                     command = continuar_aux)
    conbtn.place(x=420,y=340)
def cargar():
    #Abre el menu para escoger la imagen desde archivos
    window.withdraw()
    archivo = ""
    def volver():#Vuelve al menu principal
        poblacion.destroy()
        window.deiconify()
    def seleccionar_archivo():
        #Abre mis archivos para escoger la silueta del arbol y una vez elegida
        #la coloca en la ventana
        global archivo
        archivo = filedialog.askopenfilename(title="abrir")#Abre mis archivos
    def continuar_aux():
        # Lleva al menu de ver poblacion y generacion
        #Recibe el path de la silueta
        poblacion.destroy()
        menu(0)
    poblacion = Toplevel(window)
    poblacion.geometry("480x100")
    backbtn = Button(master=poblacion,
                     bg = "red",
                     text = "Volver",
                     width = 10,
                     height = 3,
                     command = volver)
    backbtn.place(x=20,y=20)
    selecarch = Button(master=poblacion,
                     bg = "gray",
                     text = "Seleccionar archivo",
                     width = 30,
                     height = 3,
                     command = seleccionar_archivo)
    selecarch.place(x=130,y=20)
    conbtn = Button(master=poblacion,
                     bg = "light green",
                     text = "Continuar",
                     width = 10,
                     height = 3,
                     command = continuar_aux)
    conbtn.place(x=380,y=20)

#-----Programa principal

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
imagenames = ["A","B","C","D","E","F","G","H","I","J"]
generaciones =[[]]


carpeta = "Poblacion"
crear_car(carpeta)



window = Tk()
window.geometry("500x420")
button1 = tk.Button(text="Elegir silueta",
                        width = 15,
                        height = 3,
                        bg = "green",
                        command=elegir_silueta)
button1.place(x=120,y=350)
   
button2 = tk.Button(text="Cargar",
                        width = 15,
                        height = 3,
                        bg = "blue",
                        command=cargar)
button2.place(x=250,y=350)
nombre = tk.Label(text="Algoritmo genético",fg="lightgreen",font=(None,20))
nombre.place(x=150,y=0)
    
image = PhotoImage(file=r"C:\Users\jenar\OneDrive\Imágenes\Arbol interfaz.png")
smaller_image = image.subsample(4,4)
canvas=Canvas(width=800,height=300)
canvas.place(x=100,y=45)
canvas.image = smaller_image
canvas.create_image(0,0,image = smaller_image,anchor = "nw")
arrayim=[]


window.mainloop()


