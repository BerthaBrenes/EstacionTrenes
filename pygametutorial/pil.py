from tkinter import *
from PIL import Image
import PIL
from PIL import ImageTk

root = Tk()
root.title("Estacion de trenes")
root.minsize(700,400)
root.resizable(width = NO,height = NO)

main = Canvas(root,width = 700,height = 500)
im1 = Image.open("TrenEscala.png")
photo = ImageTk.PhotoImage(im1)
lnFondo = Label(root,image = photo)
lnFondo.place(x=0, y = 0)
width= 600
height =700

main.pack(side = TOP,expand = True,fill = BOTH)
root.mainloop()
