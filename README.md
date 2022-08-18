# Minijuego de tiempo de reacción
El tiempo de reacción es el tiempo en el que el cuerpo reacciona hacia un estímulo físico, visual o auditivo, un buen tiempo de reacción indica que un individuo puede reaccionar de manera rápida ante cualquier situación que se presente de forma inesperada. En los videojuegos, el tiempo de reacción es indispensable para poder mejorar, normalmente los jugadores que tienen mejor tiempo de reacción son jugadores más buenos que el promedio, por lo que para poder mejorar se puede optar por mejorar el tiempo de reacción visual y auditivo.

## Objetivos
El objetivo de esta aplicación es evaluar que tan bien o tan mal se encuentran los usuarios al reaccionar ante los estímulos visuales y auditivos, si una persona tiene tiempos de reacción muy elevados con respecto al promedio de un humano o con respecto a sus resultados previos, la aplicación recomendará hacer ejercicios en forma de minijuegos para poder mejorar el tiempo de reacción, con esto se intenta hacer que la persona mejore en los videojuegos, ya sea que se los tome de forma casual o competitiva.

## Algoritmo

 - La aplicación funcionará de manera que cuando cambie de color el objeto mostrado en pantalla o suene un ruido el usuario tenga que reaccionar lo mas rápido que pueda para medir su tiempo de reacción

- Se genera una una variable de tiempo en segundos la cual ocupará numeros de 2 a 5 de forma aleatoria, esto sirve para que el fondo del objeto cambie de color cuado termine el tiempo generado

- Cuando termina el tiempo en segundos, el fondo del objeto cambiará de color

- Cuando el objeto cambia de color, se inicia una variable de tiempo en milisegundos y deja de contarlos una vez que el usuario hace click, el tiempo se guardara en una variable llamada tiempo de racción visual

- La misma variable de tiempo en segundos vuelve a tomar un valor entre 2 y 5 la cual servirá para evaluar el tiempo de reacción auditivo, el cual, en teoría es mucho más rápido que el visual

- Cuando termina el tiempo en segundos, sonará un sonido y los milisegundos empezaran a contar justo cuando se escuche

- Cuando el usuario hace click el tiempo se guardará en una variable de tiempo de reacción auditiva

- Al final la aplicación evaluará si el tiempo de reacción del usuario se encuentra por encima del promedio o por debajo del promedio en los dos tipos de casos, tanto en visual como auditivo
