from tkinter import *
import gravity_functions as gf
from matplotlib import pyplot as plt

root = Tk()
root.title('GRAVITY PROJECT')
root.geometry('1050x650+300+200')
root.configure(bg="black")
root.resizable(False,False)

img = PhotoImage(file='images/universe.png')
Label(root, image=img, bg='black').place(x=0,y=0)

Label(root, text='GRAVITY PROJECT', font=('Arial', 40, 'bold'), fg='#00ABB3').place(x=30, y=250)

copy = Button(root, text='Angel Mauricio Ramirez Herrera', font=('Arial', 12, 'bold'))
copy.place(x=10, y=600)

def option_1():

    #La funcion go_back sirve para ir al menu principal al borrar el frame optionFrame
    def go_back():
        optionFrame.destroy()

    #La funcion send_variables sirve para mandar datos proporcionados por el usuario y obtener una respuesta
    def send_variables():
        try:
            time = float(input1.get())
            distance = float(input2.get())
            ans = gf.grv_fun.get_similar(gf.grv_fun.get_planet_gravity(time, distance))
            msg = 'Respuesta: ' + str(ans)
            answer = Label(optionFrame, text=msg, fg='red', bg='white', font=('Arial', 6, 'bold'))
            answer.place(y=300)
        except:
            answer = Label(optionFrame, text='Ha ocurrido un error', fg='red', bg='white', font=('Arial', 6, 'bold'))
            answer.place(y=300)
    
    #OptionFrame almacena solo los elementos de la opcion seleccionada
    optionFrame = Frame(root, width=400, height=400, bg='white')
    optionFrame.place(x=600, y=200)

    #heading sirve para informar al usuario en donde se encuentra
    heading = Label(optionFrame, text='Obtener la gravedad del planeta', fg='#00ABB3', bg='white', font=('Arial', 15, 'bold'))
    heading.place(x=10, y=10)

    #inputs_frame almacena los elementos de los inputs proporcionados por el usuario
    inputs_frame = Frame(optionFrame, width=300, height=300, bg='white' )
    inputs_frame.place(x=50, y=45)

    label1 = Label(inputs_frame, text='Proporciona el tiempo en el que cae el objeto: ', bg='white', font=('Arial', 9, 'bold'))
    label1.place(x=10, y=5)

    input1 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input1.place(x=10, y=35)
    
    label2 = Label(inputs_frame, text='Proporciona la altura del objeto: ', bg='white', font=('Arial', 9, 'bold'))
    label2.place(x=10, y=65)

    input2 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input2.place(x=10, y=95)

    #send sirve para mandar los datos proporcionados por el usuario a la funcion send_variables
    send = Button(inputs_frame, text='Enviar', bg='white', font=('Arial', 9, 'bold'), border=0, command=send_variables)
    send.place(x=10, y=125)

    #goBack sirve para ir al menu principal al llamar a la funcion go_back
    goBack =  Button(inputs_frame, text='Ir atras', bg='white', font=('Arial', 9, 'bold'), border=0, command=go_back)
    goBack.place(x=100, y=125)

def option_2():

    #La funcion go_back sirve para ir al menu principal al borrar el frame optionFrame
    def go_back():
        optionFrame.destroy()

    #La funcion send_variables sirve para mandar datos proporcionados por el usuario y obtener una respuesta
    def send_variables():
        try:
            planet_gravity = float(input1.get())
            distance = float(input2.get())
            ans = gf.grv_fun.get_time(planet_gravity, distance)
            msg = 'Respuesta: El objeto cae en ' + str(ans) + ' segundos'
            answer = Label(optionFrame, text=msg, fg='red', bg='white', font=('Arial', 6, 'bold'))
            answer.place(y=300)
        except:
            answer = Label(optionFrame, text='Ha ocurrido un error', fg='red', bg='white', font=('Arial', 6, 'bold'))
            answer.place(y=300)
    
    #OptionFrame almacena solo los elementos de la opcion seleccionada
    optionFrame = Frame(root, width=400, height=400, bg='white')
    optionFrame.place(x=600, y=200)

    #heading sirve para informar al usuario en donde se encuentra
    heading = Label(optionFrame, text='Obtener el tiempo en el que cae el objeto', fg='#00ABB3', bg='white', font=('Arial', 15, 'bold'))
    heading.place(x=10, y=10)

    #inputs_frame almacena los elementos de los inputs proporcionados por el usuario
    inputs_frame = Frame(optionFrame, width=300, height=300, bg='white' )
    inputs_frame.place(x=50, y=45)

    label1 = Label(inputs_frame, text='Proporciona la gravedad del planeta: ', bg='white', font=('Arial', 9, 'bold'))
    label1.place(x=10, y=5)

    input1 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input1.place(x=10, y=35)
    
    label2 = Label(inputs_frame, text='Proporciona la altura del objeto: ', bg='white', font=('Arial', 9, 'bold'))
    label2.place(x=10, y=65)

    input2 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input2.place(x=10, y=95)

    #send sirve para mandar los datos proporcionados por el usuario a la funcion send_variables
    send = Button(inputs_frame, text='Enviar', bg='white', font=('Arial', 9, 'bold'), border=0, command=send_variables)
    send.place(x=10, y=125)

    #goBack sirve para ir al menu principal al llamar a la funcion go_back
    goBack =  Button(inputs_frame, text='Ir atras', bg='white', font=('Arial', 9, 'bold'), border=0, command=go_back)
    goBack.place(x=100, y=125)

def option_3():

    #La funcion go_back sirve para ir al menu principal al borrar el frame optionFrame
    def go_back():
        optionFrame.destroy()

    #La funcion send_variables sirve para mandar datos proporcionados por el usuario y obtener una respuesta
    def send_variables():
        try:
            planet_gravity = float(input1.get())
            time = float(input2.get())
            ans = gf.grv_fun.get_distance(planet_gravity, time)
            msg = 'Respuesta: El objeto cayo desde ' + str(ans) + ' metros'
            answer = Label(optionFrame, text=msg, fg='red', bg='white', font=('Arial', 6, 'bold'))
            answer.place(y=300)
        except:
            answer = Label(optionFrame, text='Ha ocurrido un error', fg='red', bg='white', font=('Arial', 6, 'bold'))
            answer.place(y=300)
    
    #OptionFrame almacena solo los elementos de la opcion seleccionada
    optionFrame = Frame(root, width=400, height=400, bg='white')
    optionFrame.place(x=600, y=200)

    #heading sirve para informar al usuario en donde se encuentra
    heading = Label(optionFrame, text='Obtener la distancia de la caida del objeto', fg='#00ABB3', bg='white', font=('Arial', 15, 'bold'))
    heading.place(x=10, y=10)

    #inputs_frame almacena los elementos de los inputs proporcionados por el usuario
    inputs_frame = Frame(optionFrame, width=300, height=300, bg='white' )
    inputs_frame.place(x=50, y=45)

    label1 = Label(inputs_frame, text='Proporciona la gravedad del planeta: ', bg='white', font=('Arial', 9, 'bold'))
    label1.place(x=10, y=5)

    input1 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input1.place(x=10, y=35)
    
    label2 = Label(inputs_frame, text='Proporciona el tiempo en el que cae el objeto: ', bg='white', font=('Arial', 9, 'bold'))
    label2.place(x=10, y=65)

    input2 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input2.place(x=10, y=95)

    #send sirve para mandar los datos proporcionados por el usuario a la funcion send_variables
    send = Button(inputs_frame, text='Enviar', bg='white', font=('Arial', 9, 'bold'), border=0, command=send_variables)
    send.place(x=10, y=125)

    #goBack sirve para ir al menu principal al llamar a la funcion go_back
    goBack =  Button(inputs_frame, text='Ir atras', bg='white', font=('Arial', 9, 'bold'), border=0, command=go_back)
    goBack.place(x=100, y=125)

def option_4():

    #La funcion go_back sirve para ir al menu principal al borrar el frame optionFrame
    def go_back():
        optionFrame.destroy()

    #La funcion send_variables sirve para mandar datos proporcionados por el usuario y obtener una respuesta
    def send_variables():
        try:
            gravity = float(input1.get())
            velocity = float(input2.get())
            angle = float(input3.get())
            height = float(input4.get())
            ans = gf.grv_fun.parabolic_motion(gravity, velocity, angle, height)
            x = ans[0]
            y = ans[1]
            plt.plot(x,y)
            plt.show()
        except:
            answer = Label(optionFrame, text='Ha ocurrido un error', fg='red', bg='white', font=('Arial', 6, 'bold'))
            answer.place(x=150, y=350)
    
    #OptionFrame almacena solo los elementos de la opcion seleccionada
    optionFrame = Frame(root, width=400, height=400, bg='white')
    optionFrame.place(x=600, y=200)

    #heading sirve para informar al usuario en donde se encuentra
    heading = Label(optionFrame, text='Obtener tiro parabólico', fg='#00ABB3', bg='white', font=('Arial', 15, 'bold'))
    heading.place(x=10, y=10)

    #inputs_frame almacena los elementos de los inputs proporcionados por el usuario
    inputs_frame = Frame(optionFrame, width=300, height=300, bg='white' )
    inputs_frame.place(x=50, y=45)

    label1 = Label(inputs_frame, text='Proporciona la gravedad: ', bg='white', font=('Arial', 9, 'bold'))
    label1.place(x=10, y=5)

    input1 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input1.place(x=10, y=35)
    
    label2 = Label(inputs_frame, text='Proporciona la velocidad inicial: ', bg='white', font=('Arial', 9, 'bold'))
    label2.place(x=10, y=65)

    input2 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input2.place(x=10, y=95)

    label3 = Label(inputs_frame, text='Proporciona el ángulo de salida: ', bg='white', font=('Arial', 9, 'bold'))
    label3.place(x=10, y=125)

    input3 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input3.place(x=10, y=155)

    label4 = Label(inputs_frame, text='Proporciona la altura inicial: ', bg='white', font=('Arial', 9, 'bold'))
    label4.place(x=10, y=185)

    input4 = Entry(inputs_frame, width=40, fg='white', border=0, bg='#B2B2B2', font=('Arial', 9))
    input4.place(x=10, y=215)

    #send sirve para mandar los datos proporcionados por el usuario a la funcion send_variables
    send = Button(inputs_frame, text='Enviar', bg='white', font=('Arial', 9, 'bold'), border=0, command=send_variables)
    send.place(x=10, y=245)

    #goBack sirve para ir al menu principal al llamar a la funcion go_back
    goBack =  Button(inputs_frame, text='Ir atras', bg='white', font=('Arial', 9, 'bold'), border=0, command=go_back)
    goBack.place(x=100, y=245)

def draw_menu():

    #Se crea un frame de 400x400px en donde se va a mostrar la informacion de el codigo
    frame = Frame(root, width=400, height=400, bg='white')
    frame.place(x=600, y=100)

    #heading sirve para informar al usuario en donde se encuentra
    heading = Label(frame, text='Menu principal', fg='#00ABB3', bg='white', font=('Arial', 15, 'bold'))
    heading.place(x=100, y=10)

    #Se crea un frame donde se van a mostrar solo los botones
    buttons_frame = Frame(frame, width=300, height=300, bg='white' )
    buttons_frame.place(x=50, y=120)

    #Los botones son opciones a realizar en el codigo, cada boton manda a llamar un funcion relacionada con la opcion seleccionada

    option1 = Button(buttons_frame, text='(1)Obtener la gravedad del planeta', bg='white', font=('Arial', 9, 'bold'), border=0, command=option_1)
    option1.place(x=10, y=5)

    option2 = Button(buttons_frame, text='(2)Obtener el tiempo en el que cae el objeto', bg='white', font=('Arial', 9, 'bold'), border=0, command=option_2)
    option2.place(x=10, y=35)

    option3 = Button(buttons_frame, text='(3)Obtener la distancia de la caida del objeto', bg='white', font=('Arial', 9, 'bold'), border=0, command=option_3)
    option3.place(x=10, y=65)

    option4 = Button(buttons_frame, text='(4)Obtener tiro parabólico', bg='white', font=('Arial', 9, 'bold'), border=0, command=option_4)
    option4.place(x=10, y=95)

draw_menu()

root.mainloop()