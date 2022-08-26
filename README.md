# Gravedad de planetas

  

Es curioso |conocer la gravedad de otros planetas para saber cómo se van a comportar si es que el ser humano llega a explorarlos, la gravedad nos puede decir demasiadas cosas sobre el planeta, pero lo más importante es saber cómo es que la masa y las fuerzas van a interactuar con él, la gravedad nos puede decir cual es el peso de las personas si es que llegan a habitarlo, nos puede decir las fuerzas de escape e incluso si nos puede indicar si el planeta es habitable o no.

  

## Objetivos

  

El objetivo de esta aplicación es comparar la gravedad de planetas externos a nuestro sistema y saber cuánta similitud hay en la gravedad obtenida con respecto a los planetas de nuestro sistema solar. Con la información obtenida se puede saber como es la gravedad del planeta ingresado, se puede saber si se parece a la gravedad de la tierra o a la gravedad de cualquier otro planeta dentro de nuestro sistema solar, además, esta información podría ocuparse para simular la caída de un objeto en alguna interfaz gráfica.

  

## Algoritmo y pseudocodigo

  

Variables:

EARTH = 9.807

MARS = 3.721

JUPITER = 24.79

SATURN = 10.44

URANUS = 8.87

VENUS = 8.87

NEPTUNE = 11.15

MERCURY = 3.7

planet_gravity

time

distance

similarity

selection

  

## Algoritmo:

-   Se obtiene la selección de lo que el usuario quiere obtener (Si quiere obtener la gravedad del planeta, el tiempo de caída o la distancia)
    
-   Se ingresan los datos de lo que se pide ingresar (puede ser tiempo y distancia, gravedad del planeta y tiempo, o gravedad del planeta y distancia)
    
-   Si se eligió obtener la gravedad del planeta, indicará su gravedad y su similitud con algún planeta de nuestro sistema solar
    
-   Si se eligió obtener el tiempo de caída, se indicará el tiempo en segundos
    
-   Si se eligió obtener la distancia de la caída del objeto, se indicará la distancia en metros
    

  

## Pseudocódigo:

Inicio

1.  Escribir: “Selecciona qué es lo que quieres obtener: \n(1)Obtener la gravedad del planeta \n(2)Obtener el tiempo en el que cae el objeto\n(3)Obtener la distancia de la caída del objeto\n…”
    
2.  Leer selection
    
3.  Si selection es igual a 1 entonces
    

4.  Escribir "Proporciona el tiempo en el que cae el objeto: "
    
5.  Leer time
    
6.  Escribir "Proporciona la altura a la que se encuentra el objeto: "
    
7.  Leer distance
    
8.  planet_gravity = (2*distance) / math.pow(time, 2)
    
9.  similarity = planet_gravity * 100 / Planeta
    
10.  Escribir “La gravedad es de “ + planet_gravity + “ y su similitud con Planeta es de 00000”
    

11.  Si selection es igual a 2 entonces
    

12.  Escribir "Proporciona la gravedad del planeta: "
    
13.  Leer planet_gravity
    
14.  Escribir "Proporciona la altura a la que se encuentra el objeto: "
    
15.  Leer distance
    
16.  time = math.sqrt((distance*2)/planet_gravity)
    
17.  Escribir “El tiempo de caída es de “ + time + “ segundos”
    

18.  Si selection es igual a 3 entonces
    

19.  Escribir "Proporciona la gravedad del planeta: "
    
20.  Leer planet_gravity
    
21.  Escribir "Proporciona el tiempo en el que cae el objeto: "
    
22.  Leer time
    
23.  distance = 0.5 * planet_gravity * math.pow(time, 2)
    
24.  Escribir “La distancia de caída del objeto es de “ + distance + “ metros”

fin 
