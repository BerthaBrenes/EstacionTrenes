"""Listas de 3 proyecto de progra
Consiste en 3 objetos
una clase padre que administra la cantidad de trenes
una calse tren que se encarga de administras los vagones
una clase vagon que es como el nodo
"""
from random import randrange
from threading import Thread
import time
archivo_estacion = open('Estacion.txt','r+')
diccionario = []

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
    def capacidad_vagones(self):
        return self.cap_vagones
    def mostrar_maquina(self):
        return("numero de maquina",self.num_maquina)
"""Clase Vagon
E: son los nodos de la lista doblemente enlazada, tiene un vaagon anterior
y un vagpn siguiente
S:el valor de la capacidad de personas por Vagon
"""
class Vagon():
    def __init__(self, next = None,prev = None,cap= None):
        self.next = next
        self.prev = prev
        self.capacidad_pers = cap
        self.num_vagon = None
    def __str__(self):
        return self.capacidad_pers
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
        self.maq = Maquina(self.identificador,randrange(5))
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
        if self.__len__() >0:# caso 1 cuando hay vagones
            self.tail = Vagon(prev =self.tail,cap = randrange(20))
            self.tail.prev.next = self.tail
            self.lenght +=1
        else: #caso 2 cuando no hay vagones
            self.head =Vagon(cap = randrange(20))
            self.tail = self.head
            self.lenght +=1
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
                self.head = None
                self.tail = None
                self.lenght -=1
            else:#caso 2 cuando hay mas de 1 vagon
                self.tail = self.tail.prev
                self.tail.next = None
                self.lenght -=1
        else:# cuando no hay vagones
            return "tren sin vagones"
    def reiniciar(self):# reiniciar el tren es decir borrar los vagones y lo datos de hora y ruta pues ya llego  su destino
        self.ruta = None
        self.hora = None
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

a = Thread(target =hora, args =())
a.start()

