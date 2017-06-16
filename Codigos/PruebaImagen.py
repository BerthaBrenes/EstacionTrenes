from tkinter import*
from threading import Thread
import threading
from PIL import Image
import PIL
from PIL import ImageTk
import pygame
import time

pygame.init()


#    _____________
#___/Cargar Imagen

im = pygame.image.load("../Imagenes/TrenEscala.png")
pic = pygame.image.tostring(im, 'RGBA')
(w,h)=(293,343)
image= Image.frombytes('RGBA', (w,h), pic)


#______________________________

im2 = pygame.image.load("../Imagenes/Estacion Isometrica Light.png")
pic2 = pygame.image.tostring(im2, 'RGB')
(m,n)=(550,401)
image2= Image.frombytes('RGB', (m,n), pic2)



#     ________
#____/Ventana

root=Tk()
root.title("Prueba imagenes")
root.minsize(550,401)

tkimage= ImageTk.PhotoImage(image)
tkimage2= ImageTk.PhotoImage(image2)

canvas= Canvas(root,width=550,height=600,bg="dark gray")
canvas.create_image(200,200, image= tkimage2)
canvas.create_image(150, 200, image=tkimage)


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
