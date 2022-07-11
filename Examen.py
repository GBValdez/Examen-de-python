import string
import tkinter
from tokenize import String
from turtle import color
import requests
import math

#Funcion para buscar el precio y el nombre del producto
def Buscar_precio():
    Clave= Codigo.get()
    link="https://guatemaladigital.com/Producto/" + Clave
    pag:requests=requests.get(link)
    Contenido:String= pag.text
    Contenido= Contenido.upper()
    for i in range(len(Contenido),0,-1):
        if Contenido[i:i+len("\"precioquetzales\":"):1]=="\"PRECIOQUETZALES\":":
            break
    pos= i+ len("\"precioquetzales\":")
    num:string=""
    cantidad:int=0
    while Contenido[pos]!=",":
        num+=Contenido[pos]
        cantidad+=1
        if cantidad>30 and Contenido[pos]==" ":
            num+="\n"
            cantidad=0
        pos+=1

    Resultado["text"]="Precio Actual: Q" + num


    for i in range(0,len(Contenido)):
        if Contenido[i:i+len("<TITLE>"):1]=="<TITLE>":
            break
    pos= i+ len("<TITLE>")
    num=""
    while Contenido[pos]!="|":
        num+=Contenido[pos]
        pos+=1
    Producto["text"]=num


#Creamos los elementos de la interfaz
ventana= tkinter.Tk()
ventana.geometry("600x600")
ventana.title("Guatemala Digital")
etiqueta=tkinter.Label(ventana,text="Guatemala Digital",bg="#ff9f1a", font="arial 50", fg="white")
etiqueta.pack(fill= tkinter.X)
Codigo= tkinter.Entry(ventana,font="arial 20",bg="#0078bb",fg="white")
Codigo.pack()
Boton= tkinter.Button(ventana,text="Buscar", command= Buscar_precio)
Boton.pack()
Instrucciones= tkinter.Label(ventana,text="Hola, para ver el nombre del producto que busca y su precio, escriba el codigo en la caja de texto y luego presione el boton", wraplength="500")
Instrucciones.pack()

Producto= tkinter.Label(ventana, font="arial 18", width="400", wraplength="500", )
Producto.pack()
Resultado= tkinter.Label(ventana, font="arial 12")
Resultado.pack()
ventana.mainloop()


#Hola