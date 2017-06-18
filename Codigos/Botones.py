from tkinter import*
from PIL import Image
import PIL
from PIL import ImageTk
import pygame
import time

pygame.init()


def cargarImagen(nombre,tamaño):
    im = pygame.image.load("../Imagenes/Botones/"+str(nombre)+".jpg")
    pic = pygame.image.tostring(im, 'RGBA')
    image= Image.frombytes('RGBA', tamaño, pic)
    tkimage= ImageTk.PhotoImage(image)
    return tkimage


root= Tk()
root.title("Botones")
root.minsize(500,100)
root.resizable(width=NO,height=NO)

canvas= Canvas(root,width=500,height=300, bg="White")
canvas.place(x=0,y=0)



Boton1 = cargarImagen("button1",(64,64)) 
Btn1= Button(root, image=Boton1, command=None, bd=0)
Btn1.place(x=50,y=50)
