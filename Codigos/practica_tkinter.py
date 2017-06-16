
## crear bolitas
from tkinter import*
#import os
from threading import Thread
import threading
from PIL import Image
import PIL
from PIL import ImageTk
import pygame
pygame.init()
flag_tren = True
imga =  pygame.image.load("imagenes/TrenEscala1.png")

img_str =pygame.image.tostring(imga,'RGB')
w,h = imga.get_rect()[2:]
imagen = Image.fromstring('RGB',(w,h),img_str)
photo = ImageTk.PhotoImage(imagen)
def izq():
    contenedor.move("BOLA",100,0)##etiqueta: busca todos los que se llamen asi, este paramentro va a ser la cantidad de veces a incrementar
def load_img(name):
    img = Image.open("imagenes/"+str(name))
    phot = ImageTk.PhotoImage(img)
    return phot

windowA =Tk()
windowA.title("Taller")
windowA.minsize(600,600)
naveIMG = load_img("TrenEscala.gif")
fondo_img = load_img("EstacionLight.jpg")
fondo = Canvas(windowA,width =550, height = 500)
fondo.place(x=0,y=0)
x_pos =0
y_pos=0
#fondo.create_image(400,400,image= fondo_img,anchor = NW)
Label_fondo = Label(windowA,image =fondo_img,width = 550, height = 500,bg = "gray")
Label_fondo.place(x=0,y=0)
Label_img = Label(windowA,image = photo,width =293, height = 343,bg="#FF000040")
Label_img.place(x=x_pos,y=y_pos)
def move():
    global flag_tren
    global x_pos
    global y_pos
    while flag_tren:
        y_pos +=1
        x_pos +=1
        if x_pos > 200:
            flag_tren = False
        print(x_pos)
        Label_img.place(x=x_pos,y= y_pos)
def hilo_move():
    c = Thread(target= move,args =())
    c.start()
#contenedor = Canvas(windowA,width =100, height = 100, bg="gray")
#contenedor.place(x =x, y=y)

## se pueden crear line, rectangle, polygon
#contenedor.create_oval(1,1,160,160,width=0, fill ="red", tags = "BOLA")
#contenedor.create_image(50,50,image= naveIMG, anchor = NW, tags ="BOLA")
botonA = Button(windowA, width= 8, height=2, command = hilo_move, text= "Derecha")
botonA.place(x =100, y =50)
windowA.mainloop()
## cargar imagenes

