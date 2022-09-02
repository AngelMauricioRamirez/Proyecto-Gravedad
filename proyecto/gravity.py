import gravity_functions as gf

finish = False

while not finish:

    selection = int(input("Selecciona que es lo que quieres obtener: \n(1)Obtener la gravedad del planeta \n(2)Obtener el tiempo en el que cae el objeto\n(3)Obtener la distancia de la caida del objeto\n(4)Terminar\n... "))

    if selection == 1:
        time = float(input("Proporciona el tiempo en el que cae el objeto: "))
        distance = float(input("Proporciona la altura a la que se encuentra el objeto: "))

        print(gf.grv_fun.get_similar(gf.grv_fun.get_planet_gravity(time, distance)))


    elif selection == 2:
        planet_gravity = float(input("Proporciona la gravedad del planeta: "))
        distance = float(input("Proporciona la altura a la que se encuentra el objeto: "))

        print(f"El objeto cae en {gf.grv_fun.get_time(planet_gravity, distance)} segundos")


    elif selection == 3:
        planet_gravity = float(input("Proporciona la gravedad del planeta: "))
        time = float(input("Proporciona el tiempo en el que cae el objeto: "))

        print(f"La distancia cayo desde una altura de {gf.grv_fun.get_distance(planet_gravity, time)}")

    elif selection == 4:
        finish = True
    
    else:
        print("No se encuentra la opcion")