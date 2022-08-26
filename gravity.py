import math

EARTH = 9.807
MARS = 3.721
JUPITER = 24.79
SATURN = 10.44
URANUS = 8.87
VENUS = 8.87
NEPTUNE = 11.15
MERCURY = 3.7


def get_time(planet_gravity, distance):
    time = math.sqrt((distance*2)/planet_gravity)
    return time


def get_distance(planet_gravity, time):
    distance = 0.5 * planet_gravity * math.pow(time, 2)
    return distance


def get_planet_gravity(time, distance):
    planet_gravity = (2*distance) / math.pow(time, 2)
    return planet_gravity


def get_simlar_gravity(planet_gravity):
    message = f"La gravedad del planeta es {planet_gravity}, su gravedad se parece al la de"
    if planet_gravity <= MERCURY:
        similarity = planet_gravity * 100 / MERCURY
        message = f"{message} Mercurio con una similitud de {round(similarity, 2)}"
    elif planet_gravity <= MARS and planet_gravity > MERCURY:
        similarity = planet_gravity * 100 / MARS
        message = f"{message} Marte con una similitud de {round(similarity, 2)}"
    elif planet_gravity <= URANUS and planet_gravity > MARS:
        similarity = planet_gravity * 100 / URANUS
        message = f"{message} Urano y Venus con una similitud de {round(similarity, 2)}"
    elif planet_gravity <= EARTH and planet_gravity > URANUS:
        similarity = planet_gravity * 100 / EARTH
        message = f"{message} la Tierra con una similitud de {round(similarity, 2)}"
    elif planet_gravity <= SATURN and planet_gravity > EARTH:
        similarity = planet_gravity * 100 / SATURN
        message = f"{message} Saturno con una similitud de {round(similarity, 2)}"
    elif planet_gravity <= NEPTUNE and planet_gravity > SATURN:
        similarity = planet_gravity * 100 / NEPTUNE
        message = f"{message} Neptuno con una similitud de {round(similarity, 2)}"
    elif planet_gravity <= JUPITER and planet_gravity > NEPTUNE:
        similarity = planet_gravity * 100 / JUPITER
        message = f"{message} Jupiter con una similitud de {round(similarity, 2)}"
    return message


selection = int(input("Selecciona que es lo que quieres obtener: \n(1)Obtener la gravedad del planeta \n(2)Obtener el tiempo en el que cae el objeto\n(3)Obtener la distancia de la caida del objeto\n... "))


if selection == 1:
    time = float(input("Proporciona el tiempo en el que cae el objeto: "))
    distance = float(input("Proporciona la altura a la que se encuentra el objeto: "))

    print(get_simlar_gravity(get_planet_gravity(time, distance)))


elif selection == 2:
    planet_gravity = float(input("Proporciona la gravedad del planeta: "))
    distance = float(input("Proporciona la altura a la que se encuentra el objeto: "))

    print(f"El objeto cae en {get_time(planet_gravity, distance)} segundos")


elif selection == 3:
    planet_gravity = float(input("Proporciona la gravedad del planeta: "))
    time = float(input("Proporciona el tiempo en el que cae el objeto: "))

    print(f"La distancia cayo desde una altura de {get_distance(planet_gravity, time)}")
    