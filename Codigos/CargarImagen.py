from tkinter import *
from PIL import Image
import PIL
from PIL import ImageTk


#   ___________________
#__/Ventana Principal

root = Tk()
root.title("Estacion de trenes")
root.minsize (700,400)
root.resizable (width=NO,height=NO)

#   ________
#__/Canvas

main_canvas = Canvas(root, width=700, height=500)
basewidth= 700
image = Image.open("RUTA DE LA IMAGEN")
photo= ImageTk.PhotoImage(image)
lbFondo = Label(root, image=photo)
lbFondo.place(x=0,y=0)
#   ________
#__/Fondo



main_canvas.pack(side = TOP, expand=True, fill=BOTH)
root.mainloop()
