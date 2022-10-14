import math

#Esta constante sirve para guardar las gravedades de los planetas de nuestro sistema solar
#Solo sirve para comparar la gravedad de un planeta x con la gravedad de los planetas de nuestro sistema solar
PLANETS = {
    "Tierra": 9.807,
    "Marte": 3.721,
    "Jupiter": 24.79,
    "Saturno": 10.44,
    "Urano": 8.87,
    "Venus": 8.87,
    "Neptuno": 11.15,
    "Mercurio": 3.7
}

#Esta matriz solo sirve para almacenar los datos en (x,y) del tiro parabolico
Matrix_XY =[
    [0],
    [0]
]

#En esta clase se encuentran las funciones que se utilizan en gravity.py
class grv_fun():
    
    #Esta función obtiene el tiempo de caida libre de un objeto al proporcionar una gravedad y una distancia
    def get_time(planet_gravity, distance):
        time = math.sqrt((distance*2)/planet_gravity)
        return time

    #Esta función obtiene la distancia recorrida de un objeto en caida libre al proporcionar una gravedadd y el tiempo
    def get_distance(planet_gravity, time):
        distance = 0.5 * planet_gravity * math.pow(time, 2)
        return distance

    #Esta función obtiene la gravedad de un planeta x al calcular la caida libre de un objeto 
    def get_planet_gravity(time, distance):
        planet_gravity = (2*distance) / math.pow(time, 2)
        return planet_gravity

    #Esta función obtiene la similitud de la gravedad del planeta x con un planeta de nuestro sistema solar
    def get_similar(planet_gravity):
        message = f"La gravedad del planeta es {planet_gravity}, su gravedad se parece al la de"
        similarity = 0

        #Para obtener la similitud de los planetas primero se recorren los valores del diccionario PLANETS
        for x in PLANETS.values():
            #Se obtiene el porcentaje de similitud con la variable next
            next = planet_gravity * 100 / x

            #Si la similitud es mayor a 100 se borra el residuo
            if next > 100: next = 100 - (next - 100)
            
            #Si next es mayor a la variable similitud ahora similitud pasa a ser next
            if next > similarity and next <= 100:
                similarity = next
                gravity = x
                #Se obtiene el nombre del planeta que es similar
                planet = list(PLANETS.keys())[list(PLANETS.values()).index(gravity)]

        #Se declara un mensaje con el planeta con una mayor similitud 
        message = f"{message} {planet} con una similitud de {round(similarity, 2)}%"

        return message
    

    def parabolic_motion(gravity, velocity, angle, height):
        #Se convierte el angulo a radianes ya que python funciona en radianes
        angle = math.radians(angle)
        #Se obtiene la velocidad inicial en (x,y)
        velocity_y = velocity*math.sin(angle)
        velocity_x = velocity*math.cos(angle)
        #Se cambia el signo de la gravedad debido a que es una fuerza negativa
        gravity *= -1
        #dt es el intervalo de tiempo en donde se obtienen los datos
        dt = 0.5
        i = 0
        #Se declaran los vectores de (x,y)
        x = [0]
        y= [height]

        #Este vector sirve para obtener las nuevas velocidades en y, sirve para registrar las velocidades en cada tiempo
        new_velocity_y = [velocity_y]

        for i in range(400):
            #Si y es negativo quiere decir que el objeto cayó hace tiempo por lo que termina el ciclo
            if y[i] > 0:
                #Se agregan datos en las posiciones (x,y)
                x.append(x[i]+velocity_x*dt)
                y.append(y[i]+new_velocity_y[i]*dt)
                #Se obtiene una nueva velocidad en y
                new_velocity_y.append(new_velocity_y[i]+(gravity*dt))
            else:
                break

        matrix_xy =[x, y]
        print(matrix_xy)





