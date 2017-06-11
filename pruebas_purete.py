f=open("mierda.txt", "r+")
final = f.tell()
def prueba_salir():
    f.seek(9)
    f.write("   Salio    ")
    f.seek(final)
    f.seek(33)
    f.write("   Salio     ")
    
def prueba_setear1(valor):
    f.seek(9)
    f.write(str(valor))
    f.seek(final)
    
def prueba_setear2(valor):
    f.seek(33)
    f.write(str(valor)+"  ")
f.seek(9)
d = f.readlines()
def suma():
    suma = [d[0]] +[" :working"]
    print(suma)
   
