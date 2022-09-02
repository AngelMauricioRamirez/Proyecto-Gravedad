import math

planets = {
    "Tierra": 9.807,
    "Marte": 3.721,
    "Jupiter": 24.79,
    "Saturno": 10.44,
    "Urano": 8.87,
    "Venus": 8.87,
    "Neptuno": 11.15,
    "Mercurio": 3.7
}


class grv_fun():
     
    def get_time(planet_gravity, distance):
        time = math.sqrt((distance*2)/planet_gravity)
        return time


    def get_distance(planet_gravity, time):
        distance = 0.5 * planet_gravity * math.pow(time, 2)
        return distance


    def get_planet_gravity(time, distance):
        planet_gravity = (2*distance) / math.pow(time, 2)
        return planet_gravity


    def get_similar(planet_gravity):
        message = f"La gravedad del planeta es {planet_gravity}, su gravedad se parece al la de"
        similarity = 0

        for x in planets.values():
            next = planet_gravity * 100 / x

            if next > 100: next = 100 - (next - 100)
            
            if next > similarity and next <= 100:
                similarity = next
                gravity = x
                planet = list(planets.keys())[list(planets.values()).index(gravity)]
        
        message = f"{message} {planet} con una similitud de {round(similarity, 2)}%"

        return message