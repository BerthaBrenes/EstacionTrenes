from random import randrange
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

archivo_estacion = open('Estacion.txt','r+')
diccionario = []

root=Tk()
root.title("Prueba imagenes")
root.minsize(830,700)
root.resizable(width = NO,height= NO)

flag_tren = True
flag_vagon = True


tren = cargar_imag("MacroTren.png",(160,187))
fondo = cargar_imag("EstacionMacro.png",(830,604))
vagon = cargar_imag("MacroVagon.png",(110,134))

canvas= Canvas(root,width=825,height=604,bg="dark gray")
canvas.create_image(410, 300, image=fondo)##posiciones

def create_fondo():
    canvas.create_image(410, 300, image=fondo)##posiciones
canvas.place(x=0,y=0)
panel_control = Canvas(root,width = 830,height=100,bg = "black")
panel_control.place(x= 0,y = 600)


"""
E: Recibe el contenido del archivo txt
S:lo convierte en un diccionario
"""
for linea in archivo_estacion:
    linea = linea.rstrip("\n")#quita el \n de nueva linea
    ruta = linea.split(",")#separa el archivo en una lista de rutas
    diccionario = diccionario + [ruta]



"""Clase Maquina
E: -numero de identificacion
   - Capacidad de vagones
"""
class Maquina:
    def __init__(self,num,cap):
        self.num_maquina = num
        self.cap_vagones = cap
        self.canvas = canvas
        self.x_tren = 580
        self.y_tren = 90
    def capacidad_vagones(self):
        return self.cap_vagones
    def mostrar_maquina(self):
        return("numero de maquina",self.num_maquina)
    def crear_maquina(self):
        print(self.num_maquina)
        self.canvas.create_image(580,90, image=tren,tags =self.num_maquina)
    def move_maquina(self):
        global flag_tren
        self.x_tren
        self.y_tren
        while flag_tren :
            self.x_tren -= 1
            self.y_tren += 1
            #self.canvas.canvasy(self.y_tren, gridspacing=None)
            #self.canvas.canvasx(self.x_tren, gridspacing=None)
            #print(self.x_tren)
            self.canvas.move(self.num_maquina,-0.98,0.85)
            if(self.x_tren <= 200):
                flag_tren = False
            time.sleep(0.01)
    def hilo_maquina(self):
        d = Thread(target= self.move_maquina,args =( ))
        d.start()
"""Clase Vagon
E: son los nodos de la lista doblemente enlazada, tiene un vaagon anterior
y un vagpn siguiente
S:el valor de la capacidad de personas por Vagon
"""
class Vagon():
    def __init__(self, next = None,prev = None,cap= None,tags = None):
        self.next = next
        self.prev = prev
        self.capacidad_pers = cap
        self.num_vagon = None
        self.tags = tags
        self.canvas = canvas
        self.x_pos = 660
        self.y_pos= 20
        self.maq1 = None
    def __str__(self):
        return self.capacidad_pers
    def vagon1(self,mq):
        self.maq1 = mq
    def crear_vagon(self,i):
        self.canvas.create_image(660,20, image=vagon,tags = self.tags+str(i))##posiciones
        if i == 1:
            #print("primero")
            print("primero=",str(i))
            self.canvas.tag_raise(self.maq1,self.tags+str(i))
        else:
            print("segundos=",str(i))
            self.canvas.tag_lower(self.tags+str(i),self.tags+str(i-1))
    def quita_vagon(self,i):
        self.canvas.delete(self.tags+str(i))
    def move_vagon(self,i):
        flag_vagon = True
        self.x_pos
        self.y_pos
        while flag_vagon :
            self.x_pos -= 1
            self.y_pos += 1
            #print(self.x_pos)
            self.canvas.move(self.tags+str(i),-0.95,0.83)
            if(self.x_pos <= (227+(i*64))):
                flag_vagon = False
            time.sleep(0.01)
    def hilo_vagon(self,i):
        d = Thread(target= self.move_vagon,args =(i,))
        d.start()



"""Clase Tren
E: numero de identificacion
    ruta y hora que debe realizar
S: el tren, ademas puede enganchar vagones, quitar vagones y reiniciar
"""
class Tren():
    def __init__(self,num,ruta,hora):
        self.identificador = num
        self.ruta = ruta
        self.hora = hora
        self.maq = Maquina(self.identificador,1)
        self.head = None
        self.tail = None
        self.lenght = 0
    def get_hora(self):
        return self.hora
    def reiniciar(self):
        self.hora = None
        self.ruta = None
        self.identificador = None
    def setear_vagones(self,valor):
        self.maq = Maquina(self.identificador,valor)
    def mostrar(self):
        print("identificador del tren",self.identificador)
        print("ruta:", self.ruta)
        print("hora",self.hora)
        print("num de maquina:",self.maq.num_maquina)
        print("capacidad de vagones:",self.maq.cap_vagones)
        print("Capacidad de personas:",self.printL())
    def __len__(self):
        return self.lenght
    def enganchar_al_inicio(self):
        if self.__len__() > 0 :# caso 1 cuando hay mas de un vagon
            self.head = Vagon(next = self.head, cap = randrange(20))
            self.head.next.prev = self.head
            self.lenght += 1
        else:#caso 2 cuadno no hay vagones
            self.head =Vagon(cap = randrange(20))
            self.tail = self.head
            self.lenght +=1
    def enganchar_al_final(self):
        if self.__len__() < int(self.maq.cap_vagones):
            if self.__len__() > 0 :# caso 1 cuando hay vagones
                self.tail = Vagon(prev =self.tail,cap = randrange(20),tags="Vagon")
                self.tail.prev.next = self.tail
                self.lenght +=1
                self.tail.crear_vagon((self.__len__()))
                time.sleep(0.5)
                self.tail.hilo_vagon((self.__len__()))

                #self.tail.mover_2vagon()
            else: #caso 2 cuando no hay vagones
                self.head =Vagon(cap = randrange(20),tags="Vagon")
                self.tail = self.head
                self.lenght +=1
                self.tail.vagon1(self.maq.num_maquina)
                self.tail.crear_vagon((self.__len__()))
                time.sleep(0.5)
                self.tail.hilo_vagon((self.__len__()))

        else:
            self.maq.cap_vagones += 1
            self.tail = Vagon(prev =self.tail,cap = randrange(20),tags="Vagon")
            self.tail.prev.next = self.tail
            self.lenght +=1
            self.tail.crear_vagon((self.__len__()))
            time.sleep(0.5)
            self.tail.hilo_vagon((self.__len__()))

    def enganchar_al_medio(self):
        if self.__len__() == 1:#caso 1 cuando solo hay un vagon
            self.tail = Vagon(prev =self.tail,cap = randrange(20))
            self.tail.prev.next = self.tail
            self.lenght +=1
        elif self.__len__() >= 2:#caso 2 cuando hay mas de dos vagones
            self.lenght +=1
            pos = (self.__len__()//2)-1
            cont = 0
            indice = self.head
            while pos >= cont: #mientras contador sea menor a la mitad de la lista
                if pos == cont: #cuando este en una posicion anterior
                    indice.next = Vagon(next = indice.prev,prev = indice.next,cap= randrange(10))
                    indice.next.next = indice.next.prev
                cont +=1
                indice = indice.next
        else:# caso 3 cuando no hay vagones
            self.head =Vagon(cap = randrange(20))
            self.tail = self.head
            self.lenght +=1
    def quitar_vagon(self):# quitar vagones
        if self.__len__() >0:
            if self.__len__() == 1:# caso uno cuando hay un solo vagon
                self.head.quitar_vagon(self__len__())
                self.head = None
                self.tail = None
                self.lenght -=1
            else:#caso 2 cuando hay mas de 1 vagon
                self.tail.quitar_vagon(self__len__())
                self.tail = self.tail.prev
                self.tail.next = None
                self.lenght -=1
        else:# cuando no hay vagones
            return "tren sin vagones"
    def reiniciar(self):# reiniciar el tren es decir borrar los vagones y lo datos de hora y ruta pues ya llego  su destino
        self.ruta = None
        self.hora = None
        create_fondo()
        while self.__len__() != 0:
            self.head = None
            self.tail = None
            self.lenght -=1
    def printL(self): #muestra los datos que hay en la lista
        indice = self.head
        suma = []
        while indice != None:
            suma = suma + [indice.__str__()]
            indice = indice.next
        return suma
    def dibuje_tren(self):
        self.maq.crear_maquina()
        time.sleep(0.5)
        self.maq.hilo_maquina()
        for i in range(int(self.maq.cap_vagones)):
            self.enganchar_al_final()

trenes = [Tren(diccionario[0][0],diccionario[0][1],diccionario[0][2]),Tren(diccionario[1][0],diccionario[1][1],diccionario[1][2]), Tren(diccionario[2][0],diccionario[2][1],diccionario[2][2]), Tren(diccionario[3][0],diccionario[3][1],diccionario[3][2]), Tren(diccionario[4][0],diccionario[4][1],diccionario[4][2]), Tren(diccionario[5][0],diccionario[5][1],diccionario[5][2])]
#tren7 = Tren(diccionario[6][0],diccionario[6][1],diccionario[6][2])
"""
Funcion para generar la hora de la estacion
Ademas de que revisa la hora que es para sacar los trenes de la estacion
"""
def hora():
    i = 0
    global diccionario
    global archivo_estacion
    while True:
        time.sleep(4)
        i +=1
        hora = " "+str(i) + ":00pm"
        print(hora)
        for a in range(6):
            if hora == trenes[a].get_hora():
                trenes[a].reiniciar()
                print(trenes[a].mostrar())
    archivo_estacion.close()
botton_generar = Button(panel_control,text="Vagon Extra",command=trenes[1].enganchar_al_final,bg="gray",fg="white",width=4, height = 1)
botton_generar.place(x=220,y = 30)
botton_mostrar = Button(panel_control,text="Mostrar",command=trenes[1].mostrar,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=220,y = 60)
botton_mostrar = Button(panel_control,text="Borrar",command=trenes[1].dibuje_tren,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=200,y = 60)

#a = Thread(target =hora, args =())
#a.start()
root.mainloop()
