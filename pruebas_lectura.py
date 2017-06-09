"""Practica de apertura de archivos y diccionario
E: un archivo
S: la informacion de los archivos
"""
archivo_estacion = open('Estacion.txt','r+')
e = archivo_estacion.readline()
dict = eval(e)
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
    archivo_estacion.write("a")
    
