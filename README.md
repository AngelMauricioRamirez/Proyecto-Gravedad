# Minijuego de tiempo de reacción
El tiempo de reacción es el tiempo en el que el cuerpo reacciona hacia un estímulo físico, visual o auditivo, un buen tiempo de reacción indica que un individuo puede reaccionar de manera rápida ante cualquier situación que se presente de forma inesperada. En los videojuegos, el tiempo de reacción es indispensable para poder mejorar, normalmente los jugadores que tienen mejor tiempo de reacción son jugadores más buenos que el promedio, por lo que para poder mejorar se puede optar por mejorar el tiempo de reacción visual y auditivo.

## Objetivos
El objetivo de esta aplicación es evaluar que tan bien o tan mal se encuentran los usuarios al reaccionar ante los estímulos visuales y auditivos, si una persona tiene tiempos de reacción muy elevados con respecto al promedio de un humano o con respecto a sus resultados previos, la aplicación recomendará hacer ejercicios en forma de minijuegos para poder mejorar el tiempo de reacción, con esto se intenta hacer que la persona mejore en los videojuegos, ya sea que se se los tome de forma casual o competitiva.

## Ejemplo de pseudocódigo
Variables tiempo_ms = 0, tiempo_s = 0, color = rojo

 genera numero aleatorio para tiempo_s de un numero entre 2 y 6
 

    mientras tiempo_s >= 0 repite
    	tiempo_s -= 1
    	si tiempo_s == 0 evalua
    		color = verde
    		mientras no se haga click repite
    			tiempo_ms += 1
    		si tiempo_ms < 250 
    			muestra "Tu tiempo de reaccion esta por arriba del promedio"
     	si no, si tiempo_ms > 250
    		muestra "Tu tiempo de reaccion esta por debajo del promedio"
