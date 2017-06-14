"""Practica de apertura de archivos y diccionario
E: un archivo
S: la informacion de los archivos
"""
from threading import Thread
import time
archivo_estacion = open('Estacion.txt','r+')
diccionario = []
for linea in archivo_estacion:
    linea = linea.rstrip("\n")#quita el \n de nueva linea
    ruta = linea.split(",")#separa el archivo en una lista de rutas
    horario = linea.split(",") #este es el valor de las rutas 
    diccionario = diccionario + [ruta]

print(len(diccionario))
def comparar():
    a = diccionario[1][2]
    print(a)
    if a == " 8:00pm":
        print ("yeah")
    else:
        print("no yet")
def hora():
    i = 0
    global diccionario
    global archivo_estacion
    archivo_estacion.seek(0)
    while True:
        time.sleep(4)
        i +=1
        hora = " "+str(i) + ":00pm"
        mytell = archivo_estacion.tell()
        print(hora)
        if hora == diccionario[0][2]:
            archivo_estacion.seek(mytell)
            archivo_estacion.write(diccionario[0][0] +","+ diccionario[0][1]+","+diccionario[0][2]+"\n")
            print("7 salio")
        if hora == diccionario[1][2]:
            archivo_estacion.seek(mytell)
            archivo_estacion.write(diccionario[1][0] +","+ diccionario[1][1]+","+diccionario[1][2]+"\n")
            print("8 salio")
        if hora == diccionario[2][2]:
            print("9 salio")
            archivo_estacion.seek(mytell)
            archivo_estacion.write(diccionario[2][0] +","+ diccionario[2][1]+","+diccionario[2][2]+"\n")
        else:
            print("wait")
    archivo_estacion.close()

            

a = Thread(target =hora, args =())
a.start()







"""
#rutas = str(archivo_estacion.readline())
#horario = str(archivo_estacion.readline())
#dict = eval(rutas)
#dict1 = eval(horario)
#print(dict)
def reiniciar():
    dict['rutas'] = []
    dict['horario'] = []
    lista_rutas = dict['rutas']
    lista_horas = dict['horario']
    print(lista_rutas,lista_horas)
    archivo_escribe.close()
def cambiarHora(hora):
    if isinstance(hora,int):
        horas = dict['horario']
        dict[horas[0]] = hora
def visualizar():
    lista_rutas = dict['rutas']
    lista_horas = dict['horario']
    print(lista_rutas,lista_horas)
def agregarRuta(valor):
    dict['horario'] = str(valor)
    a = dict['horario']
def prueba_condiccionario():#mas paqueteado
    f=open("mierda.txt", "r+")
    final = f.tell()
    a =str(f.readline())
    b = eval(a)
    b[0] = "12345"
    f.seek(11)
    f.writelines(b[0])
    f.seek(final)
    print(str(f.readline()))
"""
