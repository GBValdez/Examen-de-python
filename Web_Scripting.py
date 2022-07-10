from ast import Break, Num, Str
from asyncio.windows_events import NULL
from cgitb import text
from distutils.debug import DEBUG
from glob import glob
from operator import truediv
import os
from re import I
import string
from timeit import repeat
from turtle import pos
from typing import Text
from xml.dom.minidom import Element
from certifi import where
import requests
from setuptools import PackageFinder
import math

global_pos:int=0
global_cantidad:int=0
#Aqui se realizar la operacion principal
def Operacion_Principal(Clase:string,Elemento:string,cantidad:int):
    global global_pos
    global_pos=0
    global global_cantidad
    global_cantidad=0
    romper:bool=False
    while global_pos<len(Contenido)-1 and not romper:
        COnseguir_clase(Clase,Elemento)
        if global_cantidad>=cantidad and cantidad>0:
            romper=True
        
#Aqui se extraera la informacion de cada elemento
def COnseguir_clase(Clase:string,ELMNT:string) -> int :
    Clase= Clase.upper()
    #Buscaremos la clase que queremos
    Indicio:int=Empezar(Clase)
    #Indicio:int= Conseguir_inicio(Clase)
    #Buscaremos el inicio del elemento
    Indicio= Buscar_ini_elemento(Indicio)
    #Buscamos que etiqueta es nuestro elemento
    Elemento:string= Que_elemento(Indicio)
    Elemnt:string=Elemento
    #Cortaremos el texto de la web para que sea mas facil de leer
    Texto:string= Contenido[Indicio:len(Contenido):1]
    #Extraeremos el elemento de la web
    Elemento= Extraccion_de_elemento(Elemento,Texto,Indicio)
    #Eliminamos las etiquetas y nos quedamos con la informacion que nos es util
    if Elemnt==ELMNT or ELMNT=="":
        global global_cantidad
        global_cantidad+=1
        Elemento= Extraccion_de_informacion(Elemento)
        print(Elemento)



def Conseguir_inicio(Texto:string) -> int:
    Actual:string= ''
    for i in range(global_pos,len(Contenido)):
        if Actual==Texto:
            return i
        Actual+=Contenido[i]
        if Comparar(Actual,Texto):
            Actual=''
    return i

def Empezar(Texto:string) -> int: 
    pos_init=0
    romper:bool=False
    while pos_init<len(Contenido) and not romper:
        pos:int=Conseguir_inicio("CLASS=")+1
        pos_init=pos
        if pos_init<len(Contenido)-1:
            while Contenido[pos]!="\"":
                pos+=1
            clase:string= Contenido[pos_init:pos:1]
            #print(clase)
            if clase.find(Texto)==-1:
              global global_pos
              global_pos=pos
            else:

                romper=True
    return pos
        
        


def Buscar_Key_clase(pos:int) -> int:
    Actual:string= ''
    for i in range(global_pos,len(Contenido)):
        if Actual=="CLASS=":
            return i
        Actual+=Contenido[i]
        if Comparar(Actual,"CLASS="):
            Actual=''
    return i





def Comparar(Texto:string,Base:string) -> bool:
     return Texto != Base[0:len(Texto):1]


def Buscar_ini_elemento(Inicio:int) ->int:
    letra:string=""
    pos:int=0
    while letra!='<':
        pos+=1
        letra=Contenido[Inicio-pos]
    return Inicio-pos


def Que_elemento(inicio:int) ->string:
    elemento:string=""
    for i in range(inicio+1,len(Contenido)):
        if Contenido[i]==" ":
            break
        elemento+=Contenido[i]
    return elemento


def Extraccion_de_informacion(texto:string) ->string:
    Final:string=""
    num_letra:int=0
    j:int=0
    while num_letra<len(texto):
        if texto[num_letra]=="<":
            j=num_letra
            romper:bool=False
            while j<len(texto) and not romper :
                if texto[j]==">":
                    romper=True  
                    num_letra=j+1
                j+=1

        if num_letra<len(texto) and texto[num_letra]!="<":
            Final+= texto[num_letra]
            num_letra+=1
    return Final


def Extraccion_de_elemento(clase:string,Texto:string,indicio:int) -> string:
    actual:string=""
    Contador:int=0
    pos:int=0
    for i in range(0,len(Texto)):
        if Texto[i:i+len(clase)+1:1]== "<"+clase:
            Contador+=1

        if Texto[i:i+len(clase)+3:1]== "</"+clase+">":
            Contador-=1

        if Contador==0:
            pos=i
            break
    global global_pos
    global_pos= indicio+i+len(clase)+4
    return Texto[0:i+len(clase)+3:1]
    



        
Enlace:string="https://guatemaladigital.com/Producto/10129945"
Pagina:requests= requests.get(Enlace)
Contenido:string= Pagina.text
Contenido= Contenido.upper()
print(Contenido)
Operacion_Principal("naranja-text","",-1)
