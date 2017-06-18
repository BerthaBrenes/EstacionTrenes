from tkinter import*
from threading import Thread
import threading
from PIL import Image
import PIL
from PIL import ImageTk
import pygame
import time

pygame.init()

def cargar_imag(nombre,tamaño):
    im = pygame.image.load("Imagenes/"+str(nombre))
    pic = pygame.image.tostring(im, 'RGBA')
    image= Image.frombytes('RGBA', tamaño, pic)
    tkimage= ImageTk.PhotoImage(image)
    return tkimage
#    _____________
#___/Cargar Imagen
"""
im = pygame.image.load("Imagenes/TrenEscala.png")
pic = pygame.image.tostring(im, 'RGBA')
(w,h)=(293,343)
image= Image.frombytes('RGBA', (w,h), pic)


#______________________________

im2 = pygame.image.load("Imagenes/Estacion Isometrica Light.png")
pic2 = pygame.image.tostring(im2, 'RGB')
(m,n)=(550,401)#tamaños
image2= Image.frombytes('RGB', (m,n), pic2)#
"""


#     ________
#____/Ventana

root=Tk()
root.title("Prueba imagenes")
root.minsize(1000,1000)

#tkimage= ImageTk.PhotoImage(image)
#tkimage2= ImageTk.PhotoImage(image2)
image2 = cargar_imag("TrenEscala.png",(293,343))
image = cargar_imag("EstacionLight.jpg",(550,401))

canvas= Canvas(root,width=550,height=600,bg="dark gray")
canvas.create_image(150, 200, image=image)##posiciones
canvas.create_image(200,200, image=image2)##posiciones

canvas.place(x=0,y=0)




##pygame.init()
##surf = pygame.image.load('bridge.png')
##
### export as string / import to PIL
##image_str = pygame.image.tostring(surf, 'RGB')         # use 'RGB' to export
##w, h      = surf.get_rect()[2:]
##image     = Image.fromstring('RGB', (w, h), image_str) # use 'RGB' to import
##
### create Tk window/widgets
##root         = Tkinter.Tk()
##tkimage      = ImageTk.PhotoImage(image) # use ImageTk.PhotoImage class instead
##canvas       = Tkinter.Canvas(root)
##
##canvas.create_image(0, 0, image=tkimage)
##canvas.pack()
