# Estacion de Trenes
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
CE-1102 Taller de Programación
Tercer Proyecto Programado
La estación del tren-TEC

## 1. Introducción.
Se va a desarrollar un simulador básico de un tren, implementando los conceptos de
programación orientada a objetos, específicamente mediante el uso de listas doblemente
enlazadas, archivos planos y una interfaz gráfica.

## 2. Simulador del tren.
Se va a simular el funcionamiento de una estación de trenes, desde el punto de vista
del controlador de transportes. La idea es manejar la llegada y salida de trenes desde la
estación del TEC (se calcula que va a construirse en 2048), en los procesos que van
desde abordaje de pasajeros, control de capacidad de los vagones, decisiones sobre una
ruta y salida del tren hacia la ruta planeada. Con respecto a la llegada de trenes el
proceso incluye que los pasajeros se bajen del tren y lo desocupen.
Otro concepto de importancia para un futuro ingeniero es desarrollar la capacidad de
trabajar en grupo (en nuestro caso 2 personas), en el cual tenga definidas funciones,
roles y responsabilidades con el objetivo de conseguir el éxito del proyecto.
## 3. Descripción Funcional Programa.
La presentación de la interfaz con el usuario es totalmente libre y será un elemento
importante dentro de la calificación del proyecto. Se puede utilizar cualquier motor de
interfaz gráfica para el proyecto.
La simulación va a presentar el funcionamiento de llegadas y salidas de trenes,
pudiendo administrarse la cantidad de pasajeros, la cantidad de vagones a asignar por
cada tren y otros aspectos. No se van a considerar aspectos como capacidades de la vía
férrea ni tampoco seguridad en el manejo y asignación de rutas. Tampoco se van a
manejar filas de pasajeros (colas) ni pagos de para adquirir los tiquetes.
El simulador debe tener una serie de botones o menús que permitan realizar las
siguientes funciones:

- Iniciar simulación: lee los datos de un archivo de configuración.
- Lista de rutas por hora: para la siguiente hora muestra todos los trenes que tiene planeada una salida o llegada.
- Estimación de demanda por ruta: por medio de esta opción se genera un número aleatorio de la cantidad de personas que van a viajar en una de las rutas a manejar en la hora. Aplica solo para salidas de trenes.

## Administración de vagones: 
- El controlador puede realizar de forma manual o automática la asignación de vagones para una ruta, de acuerdo a la demanda.
- Los vagones libres son cargados desde el archivo de configuración.
- Salida de tren: desaparece de la lista de trenes a administrar.
- Llegada de tren: se registra la llegada y se liberan los vagones.
- Todas estas funciones deben mostrar elementos gráficos que permitan al controlador lo que está pasando.

El modelo de objetos básico se presenta a continuación:
Tren.
Atributos
Número de tren: identificador del tren
Ruta: descripción de la ruta a nivel de destinos. Ej: San José – TEC,
TEC – Alajuela.
Hora: hora de salida o llegada del tren.
Máquina: identificador de la máquina
Vagones: lista doblemente enlazada con los vagones que llevará el tren.

El objeto Tren va a mantener los siguientes punteros sobre la lista de vagones:
head: puntero al primer vagón.
tail: puntero al último vagón

Métodos
Enganchar al inicio
Enganchar al final
Enganchar en el medio
Quitar vagón
Salir
Llegar
Máquina.
Atributos
Número de máquina: identificador de la máquina.
capacidad: cantidad de vagones que puede manejar la máquina.
Métodos
Vagón-tren.
Atributos
Número de vagón: identificador del vagón.
next: puntero al siguiente vagón.
prev: puntero al vagón anterior
capacidad: cantidad de pasajeros máximos del vagón.
Métodos
Vagón.
Atributos
Número de vagón: identificador del vagón.
next: puntero al siguiente vagón.
prev: puntero al vagón anterior
capacidad: cantidad de pasajeros máximos del vagón.
Métodos
Carga de datos: carga de un archivo de texto llamado “estacion.txt” los datos
necesarios para crear las instancias de los trenes y rutas que va a manejarse. Debe
definir la estructura del archivo, así como el formato y forma de acceso que vaya a
utilizarse. El archivo debe contener la información necesaria sobre:
Rutas: incluyendo llegadas y salidas.
Vagones disponibles

## Modelo de objetos.
Pueden existir algunos métodos que se requieran y no estén descritos en
la presente definición. Pueden realizarse modificaciones al modelo de
objetos enunciado, siempre y cuando las mismas se documenten.

