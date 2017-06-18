from random import randrange
from tkinter import*
from threading import Thread
import threading
from PIL import Image
import PIL
from PIL import ImageTk
import pygame
from pygame.locals import *
import time
import random

pygame.init()#inicializa pygame
#carga las Imagenes
#E: el tamaño de la imagen, tamaño de la imagen y si necesita redimedionar la imagen entrega el numero tamaño de la imagen
#S: una imagen
def cargar_imag(nombre,tamaño,redimedionar = None):
    im = pygame.image.load("Imagenes/"+str(nombre))
    pic = pygame.image.tostring(im, 'RGBA')
    image= Image.frombytes('RGBA', tamaño, pic)
    if redimedionar != None:
        image =image.resize(redimedionar,Image.ANTIALIAS)
    tkimage= ImageTk.PhotoImage(image)
    return tkimage
#abre el archivo Estacion
archivo_estacion = open('Estacion.txt','r+')
diccionario = []#esta lista va a contener la informacion del archivo
#inicializa la Gui
root=Tk()
root.title("Prueba imagenes")
root.minsize(830,700)
root.resizable(width = NO,height= NO)
#son dos variables para denotar cuando un vagon salio
#___Variables globales
Tren_salida = 0
Tren_llegada = 0
Automatico = True
lista_llegada = [0,1,2,3,4,5]
lista_salida = []
#carga las imagenes principales
tren = cargar_imag("MacroTren.png",(160,187))
fondo = cargar_imag("EstacionMacro.png",(830,604))
vagon = cargar_imag("MacroVagon.png",(110,134))
mapa = cargar_imag("Mapa.gif",(497,494),(830,604))
#crear el canvas principal
canvas= Canvas(root,width=825,height=604,bg="dark gray")
canvas.create_image(410, 300, image=fondo)##posicione, carga la imagen de fondo

def create_fondo():#esta es una funcion para crear un fondo, lo que pasa es que sobrepone la imagen, utilizar para la imafen de llegada
    canvas.create_image(410, 300, image=mapa)##posiciones, crea la imagen de llegada
def create_mapa():# crea el hilo para cargar la animacion del mapa
    l = 0
    a = Thread(target =hilo_mapa, args =())
    a.start()

    #canvas.create_image(410,300, image=mapa,tags= "Mapa")##posicione
def hilo_mapa():# crear la animacion normal de cargar imagenes
    for i in range(4):
        imagen2 = cargar_imag("eva_ad" + str(i) +".gif",(504,299))
        canvas.create_image(410, 300,image = imagen2)
        time.sleep(0.5)
    time.sleep(0.5)
#coloca el canvas total en el espacion
canvas.place(x=0,y=0)
#crea el canvas del panel de control
panel_control = Canvas(root,width = 830,height=100,bg = "black")
panel_control.place(x= 0,y = 600)


"""
E: Recibe el contenido del archivo txt
S:lo convierte en una list
"""
for linea in archivo_estacion:#lee el cada lina del archivo
    linea = linea.rstrip("\n")#quita el \n de nueva linea
    ruta = linea.split(",")#separa el archivo en una lista de rutas
    diccionario = diccionario + [ruta]#lo mete en una lsita

"""Clase Maquina
esta clase va a contener la maquina es decir la cabeza del tren
esta cabeza va a tener un numero de maquina y una capacidad de vagnes que determina la cantidad de vagones a crear_maquina
"""
class Maquina:
    def __init__(self,num,cap):
        self.num_maquina = num
        self.cap_vagones = cap
        self.canvas = canvas
        self.x_tren = 580
    def capacidad_vagones(self):
        return self.cap_vagones#debuelve la capacidad de vagones
    def mostrar_maquina(self):
        return("numero de maquina",self.num_maquina)
    def crear_maquina(self):# este metodo crea una maquina es decir una cabeza del tren
        print(self.num_maquina)
        self.canvas.create_image(580,90, image=tren,tags =self.num_maquina)
    def salida_maquina(self):#simplemente mueve el canvas para la salida de la maquina
        self.canvas.move(self.num_maquina,-0.98,0.85)
        self.x_tren = 580
    def move_maquina(self):
        while self.x_tren != 200:# mueve el x hasta que sea igual a 200
            self.x_tren -= 1#controla que la maquina se posiciones en el lugar desado
            self.canvas.move(self.num_maquina,-0.98,0.85)
            time.sleep(0.01)
    def hilo_maquina(self):#crea el hilo que mueve la maquina
        d = Thread(target= self.move_maquina,args =())
        d.start()
"""Clase Vagon
E: son los nodos de la lista doblemente enlazada, tiene un vaagon anterior
y un vagpn siguiente
S:el valor de la capacidad de personas por Vagon
"""
class Vagon():
    def __init__(self, next = None,prev = None,cap= None,tags = None,i = None):
        self.next = next#siguiente
        self.prev = prev#previo
        self.capacidad_pers = cap#capacidad de personas
        self.i = i#el identificador de cada vagon y su posiciones, es decir el largo de la lista
        self.tags = tags# el taga de la creacion del vagon
        self.canvas = canvas# el canvas principal
        self.x_pos = 660#la posicion x del vagon
        self.y_pos= 20# la psiicion y del vagon
        self.s = False
    def __str__(self):
        return self.capacidad_pers
    def crear_vagon(self):#crea el vagon
        self.canvas.create_image(660,20, image=vagon,tags = self.tags+str(self.i))##posiciones
        if self.i == 0:#cuando es el primer vagon
            print("yo soy el primero",self.tags+str(self.i),str(self.capacidad_pers))
            self.canvas.tag_raise(self.tags,self.tags+str(self.i))# la funcion tag_raise lo que hace es colocar el primer tag por encima del sgundo
            #en este caso pone la maquina primero que el vagon
        else:#crea los demas vagones
            self.canvas.tag_lower(self.tags+str(self.i),self.tags+str(self.i-1))#aqui hace lo contrario y lo hace solo con los vagones
    def quitar_vagon(self):#con esta funcion elimina los vagones
        self.canvas.delete(self.tags+str(self.i))

    def cambiar_pos(self,deseado,actual):
        print(self.tags+str(deseado))
        self.canvas.addtag_below(self.tags+str(deseado),self.tags+str(actual))
        self.canvas.dtag(self.tags+str(deseado),self.tags+str(actual))
        e = Thread(target=self.mover_atras,args=())
        e.start()
        print("soy el nuevo",self.tags+str(deseado))

    def salirvagones(self):#mueve el vagon para la salida
        self.canvas.move(self.tags+str(self.i),-0.95,0.83)
        self.x_pos = 660
    def move_vagon(self):#mueve el vagon en la entrada igual que la otra funcion
        print("moviendo",self.tags+str(self.i))
        while self.x_pos != (291+(self.i*64)) : #mueve los vagones de forma proporcional a su entrada
            self.x_pos -= 1
            self.canvas.move(self.tags+str(self.i),-0.95,0.83)
            time.sleep(0.01)
    def mover_atras(self):
        print("moviedo")
        while self.x_pos != (100+(self.i*64)) : #mueve los vagones de forma proporcional a su entrada
            self.x_pos -= 1
            print(x_pos)
            self.canvas.move(self.tags+str(self.i),+1,-0.83)
            time.sleep(0.01)
    def hilo_vagon(self):#inicializa el movimiento
        d = Thread(target= self.move_vagon,args =())
        d.start()
    def llegada(self):
        #create_fondo()
        time.sleep(0.5)
        global Tren_llegada
        global Tren_salida
        Tren_llegada = 0
        Tren_salida = 0


"""Clase Tren
Es la encargada de hacer la maquina y los vagones de acuero a lo que recibe del txt pues el txt es el que le da las instancias
S: el tren, ademas puede enganchar vagones, quitar vagones y reiniciar
"""
class Tren():
    def __init__(self,num,ruta,hora_llegada,hora_salida):
        self.identificador = num#diferencia a cada tren
        self.ruta = ruta
        self.hora_llegada = hora_llegada
        self.hora_salida = hora_salida
        self.maq = Maquina(self.identificador,random.randrange(0,9))#crea una maquina con un rango aleatorio de vagones
        self.head = None
        self.tail = None
        self.lenght = 0
    def get_hora_llegado(self):# la hora de llegada
        return self.hora_llegada
    def get_hora_salida(self):# la hora de salida
        return self.hora_salida
    def setear_vagones(self,valor):
        self.maq = Maquina(self.identificador,valor)
    def mostrar(self):
        print("identificador del tren",self.identificador)
        print("ruta:", self.ruta)
        print("hora de llegada:",self.hora_llegada)
        print("hora de salida:",self.hora_salida)
        print("num de maquina:",self.maq.num_maquina)
        print("capacidad de vagones:",self.maq.cap_vagones)
        print("Capacidad de personas:",self.printL())
    def __len__(self):# obtiene el largo de la lista
        return self.lenght
    def enganchar_al_inicio(self):#engancha un tren al inicio
        if self.__len__() < int(self.maq.cap_vagones):
            if self.__len__() > 0 :# caso 1 cuando hay mas de un vagon
                self.head = Vagon(next = self.head, cap = randrange(1,20),tags =self.maq.num_maquina,i= self.__len__())#llama a crear el vagon y le asigna sus tags
                self.head.next.prev = self.head
                self.lenght += 1
            else:#caso 2 cuadno no hay vagones
                self.head =Vagon(cap = randrange(20))
                self.tail = self.head
                self.lenght +=1
        else:
            print("estoy enganchandome mas")
            self.maq.cap_vagones += 1
            self.quitar_ele(0)
            self.lenght +=1
            time.sleep(0.5)
            self.head = Vagon(next = self.head,cap = randrange(20),tags=str(self.identificador),i = 0)
            self.head.next.prev = self.head
            self.head.crear_vagon()
            self.head.hilo_vagon()
            self.enganchar_al_final()
            time.sleep(1)
    def enganchar_al_final(self):
        if self.__len__() < int(self.maq.cap_vagones):
            if self.__len__() > 0 :# caso 1 cuando hay vagones
                self.tail = Vagon(prev =self.tail,cap = randrange(20),tags=str(self.identificador),i=self.__len__())#lo mismo
                self.tail.prev.next = self.tail
                self.lenght +=1
                self.tail.crear_vagon()# primero crea el vagon
                time.sleep(0.5)
                self.tail.hilo_vagon()#despues lo mueve para que se alinee con el resto

            else: #caso 2 cuando no hay vagones
                self.head =Vagon(cap = randrange(20),tags=str(self.identificador),i = self.__len__())
                self.tail = self.head
                self.lenght +=1
                self.tail.crear_vagon() #crea el vagon con todo y la maquina
                time.sleep(0.5)
                self.tail.hilo_vagon() #lo alinea todod

        else:# este caso es en manual cuando se tiene que crear un vagon exttra
            self.maq.cap_vagones += 1
            self.tail = Vagon(prev =self.tail,cap = randrange(20),tags=str(self.identificador),i = self.__len__())
            self.tail.prev.next = self.tail
            self.lenght +=1
            self.tail.crear_vagon()
            time.sleep(0.5)
            self.tail.hilo_vagon()

    def enganchar_al_medio(self):
        if self.__len__() < int(self.maq.cap_vagones):
            print("esata no es mi condicion")
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
                pos = (self.__len__()//2)
                self.quitar_ele(pos)
                indice = self.head
                for i in range(pos):
                    indice = indice.next
                indice.next =  Vagon(next = indice.next,prev = indice,cap= randrange(10))
                indice.next.next.prev = indice.next
        else:
            if self.__len__() >2:
                print("esta es mi condicion")
                self.maq.cap_vagones += 1
                pos = (self.__len__()//2)
                indice = self.head
                for i in range(1,pos):
                    indice = indice.next
                self.quitar_ele(pos)
                indice.next =  Vagon(next = indice.next,prev = indice,cap= randrange(10),tags=str(self.identificador),i = pos)
                indice.next.next.prev = indice.next
                self.lenght +=1
                indice.next.crear_vagon()
                indice.next.hilo_vagon()
                self.enganchar_al_final()
            else:
                if self.__len__() == 1:
                    self.enganchar_al_final()
                    self.maq.cap_vagones += 1
                else:
                    self.maq.cap_vagones += 1
                    self.quitar_ele(1)
                    self.enganchar_al_final()
                    self.enganchar_al_final()

    def quitar_ele(self,ele):
        if self.__len__()>0:
            self.lenght -=1
            indice = self.head
            for i in range(ele):
                indice= indice.next
            indice.quitar_vagon()
            if(indice != self.head):
                indice.prev.next =indice.next
            else:
                self.head = indice.next,
            if(indice != self.tail):
                indice.next.prev = indice.prev
            else:
                self.tail = indice.prev

    def hilo_salida(self):# crea el hilo de la salida de la maquina y el vagon
        for a in range(600): #se mueve eesta cantidad
            self.maq.salida_maquina()#mueve la maquina
            indice =self.head# igual que en listas recorre la lista para ir moviendo cada uno de los vagones
            while indice !=None:
                indice.salirvagones()
                indice = indice.next
            time.sleep(0.01)
        time.sleep(0.5)
        create_mapa()
        self.head.llegada()
    def hilo_llegada(self):# crea el hilo de la salida de la maquina y el vagon
        for a in range(600): #se mueve eesta cantidad
            self.maq.crear_maquina()#mueve la maquina
            self.maq.hilo_maquina()
            indice =self.head# igual que en listas recorre la lista para ir moviendo cada uno de los vagones
            while indice !=None:
                indice.move_vagon()
                indice = indice.next
            time.sleep(0.01)
        time.sleep(0.5)
    def Salida(self):#genera el hilo de la Salida
        global lista_llegada
        global lista_salida
        a = Thread(target = self.hilo_salida,args=())
        a.start()
        lista_salida.append(lista_llegada[0])
        lista_llegada = lista_llegada[1:]
    def llegada_Tren(self):
        global lista_llegada
        global lista_salida
        self.maq.crear_maquina
        a = Thread(target = self.hilo_llegada,args=())
        a.start()
        lista_salida.append(lista_llegada[0])
        lista_llegada = lista_llegada[1:]
    def reiniciar(self):# reiniciar el tren es decir borrar los vagones y lo datos de hora y ruta pues ya llego  su destino
        self.ruta = None
        self.hora = None
        create_fondo()
        while self.__len__() != 0:
            self.tail.quitar_vagon(self.__len__())
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
    def dibuje_tren(self):# dibuja el tren conn su maquina y todod
        self.maq.crear_maquina()
        time.sleep(0.5)
        for i in range(int(self.maq.cap_vagones)):
            self.enganchar_al_final()
        self.maq.hilo_maquina()

trenes = [Tren(diccionario[0][0],diccionario[0][1],diccionario[0][2],diccionario[0][3]),Tren(diccionario[1][0],diccionario[1][1],diccionario[1][2],diccionario[1][3]), Tren(diccionario[2][0],diccionario[2][1],diccionario[2][2],diccionario[2][3]), Tren(diccionario[3][0],diccionario[3][1],diccionario[3][2],diccionario[3][3]), Tren(diccionario[4][0],diccionario[4][1],diccionario[4][2],diccionario[4][3]), Tren(diccionario[5][0],diccionario[5][1],diccionario[5][2],diccionario[5][3])]

#crea las instancia de la clase trenes
"""
Funcion para generar la hora de la estacion
Ademas de que revisa la hora que es para sacar los trenes de la estacion
"""
def hora():
    i = 0
    global diccionario
    global archivo_estacion
    global Automatico
    while Automatico:
        time.sleep(4)
        i = (i+1)%24# para crear la hora
        hora = " "+str(i) + ":00pm"
        print(hora)
        global Tren_salida
        global Tren_llegada
        for a in range(6):
            if hora == trenes[a].get_hora_llegado():
                if Tren_llegada == 0:
                    trenes[a].dibuje_tren()
                    print(trenes[a].mostrar())
                    Tren_llegada = 1

            if hora == trenes[a].get_hora_salida():
                if Tren_salida == 0:
                    trenes[a].Salida()
                    print(trenes[a].mostrar())
                    Tren_salida = 1
def swith_A():
    hilo_automatico()

def swith_M():
    global Automatico
    Automatico = False
j = lista_llegada[0]
botton_generar = Button(panel_control,text="Vagon Extra",command=trenes[j].enganchar_al_final,bg="gray",fg="white",width=4, height = 1)
botton_generar.place(x=220,y = 30)
botton_mostrar = Button(panel_control,text="Mostrar",command=trenes[j].mostrar,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=220,y = 80)
botton_mostrar = Button(panel_control,text="Dibujar",command=trenes[j].dibuje_tren,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=200,y = 60)
botton_mostrar = Button(panel_control,text="Salida",command=trenes[j].Salida,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=100,y = 60)
botton_mostrar = Button(panel_control,text="Llegada",command=trenes[j].llegada_Tren,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=100,y = 60)
botton_mostrar = Button(panel_control,text="Manual",command=swith_M,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=280,y = 40)
botton_mostrar = Button(panel_control,text="Automatico",command=swith_A,bg="gray",fg="white",width=4, height = 1)
botton_mostrar.place(x=260,y = 40)
#crea el tred de la hora
def hilo_automatico():
    global Automatico
    Automatico= True
    a = Thread(target =hora, args =())
    a.start()
hilo_automatico()
root.mainloop()
