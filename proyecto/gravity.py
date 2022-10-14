#se importan las funciones que se encuentran en gravity_functions
import gravity_functions as gf

finish = False

#Este ciclo solo para cuando finish es igual a True
while not finish:

    #La variable selection sirve para elegir qué accion que quiere hacer en el programa
    selection = int(input("Selecciona que es lo que quieres obtener: \n(1)Obtener la gravedad del planeta \n(2)Obtener el tiempo en el que cae el objeto\n(3)Obtener la distancia de la caida del objeto\n(4)Obtener tiro parabólico\n... "))

    #Obtener la gravedad del planeta
    if selection == 1:
        time = float(input("Proporciona el tiempo en el que cae el objeto: "))
        distance = float(input("Proporciona la altura a la que se encuentra el objeto: "))

        print(gf.grv_fun.get_similar(gf.grv_fun.get_planet_gravity(time, distance)))

    #Obtener el tiempo en el que cae el objeto
    elif selection == 2:
        planet_gravity = float(input("Proporciona la gravedad del planeta: "))
        distance = float(input("Proporciona la altura a la que se encuentra el objeto: "))

        print(f"El objeto cae en {gf.grv_fun.get_time(planet_gravity, distance)} segundos")

    #Obtener la distancia de la caida del objeto
    elif selection == 3:
        planet_gravity = float(input("Proporciona la gravedad del planeta: "))
        time = float(input("Proporciona el tiempo en el que cae el objeto: "))

        print(f"La distancia cayo desde una altura de {gf.grv_fun.get_distance(planet_gravity, time)}")

    #Obtener tiro parabólico
    elif selection == 4:
        gravity = float(input("Proporciona una gravedad para calcular el tiro parabolico: "))
        velocity = float(input("Proporciona la velocidad inicial: "))
        angle = float(input("Proporciona el ángulo de salida: "))
        height = float(input("Proporciona la altura inicial del tiro parabolico: "))
        print(gf.grv_fun.parabolic_motion(gravity, velocity, angle, height))
    
    #Si no se encuentra la opcion seleccionada manda un mensaje al usuario
    else:
        print("No se encuentra la opcion")