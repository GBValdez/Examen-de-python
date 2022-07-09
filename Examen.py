from ast import Break, Num, Str
from cgitb import text
from distutils.debug import DEBUG
import os
from re import I
import string
from timeit import repeat
from turtle import pos
from typing import Text
import requests
from setuptools import PackageFinder
import math


def COnseguir_clase(Clase:string) -> string :
    Clase= Clase.upper()
    Indicio:int= Conseguir_inicio(Clase)
    Indicio= Buscar_ini_elemento(Indicio)
    Elemento:string= Que_elemento(Indicio)
    Texto:string= Contenido[Indicio:len(Contenido):1]
    Elemento= Extraccion_de_elemento(Elemento,Texto)
    Elemento= Extraccion_de_informacion(Elemento)
    print(Elemento)

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


def Extraccion_de_elemento(clase:string,Texto:string) -> string:
    actual:string=""
    Contador:int=0
    pos:int=0
    for i in range(0,len(Texto)):
        #print(Texto[i:i+len(clase)+1:1])
        #print(Texto[i:i+len(clase)+3:1])

       # if math.floor(i/100)*100==i:
        #    input("Enter")
         #   os.system("cls")
        
        if Texto[i:i+len(clase)+1:1]== "<"+clase:
            Contador+=1
            #print(Texto[i:i+len(clase)+1:1])

        if Texto[i:i+len(clase)+3:1]== "</"+clase+">":
            Contador-=1

        if Contador==0:
            pos=i
            break
    return Texto[0:i+len(clase)+3:1]
    


def Buscar_ini_elemento(Inicio:int) ->int:
    letra:string=""
    pos:int=0
    while letra!='<':
        pos+=1
        letra=Contenido[Inicio-pos]
    return Inicio-pos

def Conseguir_inicio(Texto:string) -> int:
    Actual:string= ''
    Pos:int =0
    for i in range(0,len(Contenido)):
        if Actual==Texto:
            return i

        Actual+=Contenido[i]
        if not Comparar(Actual,Texto):
            Actual=''


def Comparar(Texto:string,Base:string) -> bool:
    for i in range(0,len(Texto)):
        if Texto[i]!= Base[i]:
            return False
    return True 

Enlace:string="http://mattfarley.ca"
Pagina:requests= requests.get(Enlace)
Contenido:string= Pagina.text
Contenido= Contenido.upper()
#print(Contenido)
COnseguir_clase("\"section projects is-medium is-white has-text-centered\"")


