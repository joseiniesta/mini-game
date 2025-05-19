import tkinter as tk
import sqlite3

# Creacion/conexion de la base de daatos 
conn = sqlite3.connect('Jugadores.db')

# Creo el cursor
cursor = conn.cursor()

#creo la tabla para almaacenar datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS jugadores (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               puntuacion INTEGER DEFAULT 0
               )
''')

# Confirmo esa creaacion de tabla
conn.commit()


preguntas = [
    "pregunta" : "¿Cual es la capital de Bélgica?",
    "opciones" :

]

# creamos la tercera ventana
def mostrar_pregunta3(nombre_jugador):
    #creo una nueva ventana
    ventana_pregunta3 = tk.Tk()
    ventana_pregunta3.title("Pregunta 3")
    ventana_pregunta3.geometry("500x300")
    # creo las preguntas y las espuestas en una variable
    pregunta = '¿Cual es la capital de Republica Checa?'
    opciones = {
        'A' : 'Praga', # esta es la corrrecta
        'B' : 'Asmara', 
        'C' : 'Atenas'
    }
    respuesta_correcta = 'A'

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 100 WHERE nombre ?', (nombre_jugador))
            conn.commit()

    # vamos a mostrar la pregunta con sus posibles respuestas
    tk.Label(ventana_pregunta3, text=pregunta, font=('Arial', 14)).pack(pady=10)

    #vamos a mostrar los botones
    for clave, valor in opciones.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana_pregunta3, text=valor).pack(pady=5)


# creamos la segunda ventana
def mostrar_pregunta2(nombre_jugador):
    #creo una nueva ventana
    ventana_pregunta2 = tk.Tk()
    ventana_pregunta2.title("Pregunta 2")
    ventana_pregunta2.geometry("500x300")
    # creo las preguntas y las espuestas en una variable
    pregunta = '¿Cual es la capital de Belgica?'
    opciones = {
        'A' : 'Bruselas', # esta es la corrrecta
        'B' : 'Copenhague', 
        'C' : 'Madrid' 
    }
    respuesta_correcta = 'A'

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre ?', (nombre_jugador))
            conn.commit()

    # vamos a mostrar la pregunta con sus posibles respuestas
    tk.Label(ventana_pregunta2, text=pregunta, font=('Arial', 14)).pack(pady=10)

    #vamos a mostrar los botones
    for clave, valor in opciones.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana_pregunta2, text=valor).pack(pady=5)


def mostrar_pregunta(nombre_jugador):
    #creo una nueva ventana
    ventana_pregunta = tk.Tk()
    ventana_pregunta.title("Pregunt1 1")
    ventana_pregunta.geometry("500x300")
    # creo las preguntas y las espuestas en una variable
    pregunta = '¿Cual es la capital de Argentina?'
    opciones = {
        'A' : 'Amsterdam',
        'B' : 'Lisboa', 
        'C' : 'Buenos Aires' # esta es la corrrecta
    }
    respuesta_correcta = 'C'

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre ?', (nombre_jugador))
            conn.commit()
            mostrar_pregunta.destroy()

    # vamos a mostrar la pregunta con sus posibles respuestas
    tk.Label(ventana_pregunta, text=pregunta, font=('Arial', 14)).pack(pady=10)

    #vamos a mostrar los botones
    for clave, valor in opciones.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana_pregunta, text=valor).pack(pady=5)
        tk.Button(vemtama_pregunta, tex=texto, width=20, command=lambda: responder(clave)).pack(pady=20)



# creo una funcion para almanezar el juego
def comenzar_juego():
    # almaceno el nombre del cuadro de entrada en una variable
    nombre = entrada_nombre.get().strip()
    # creo condicional para forzar la entrada del nombre
    if nombre:
        # si esite lo almaceno en la base de datos
        cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES( ?, ?)", (nombre, 0))
        # confirmo cambios
        conn.commit()
        # destruyo la ventana principal
        root.destroy()
        # llamo a otra funcion de preguntas
        mostrar_pregunta(nombre)

        # aqui iria la llamada a la siguiente ventana
    else:
        label_mensaje.config(text='Por favor, introduzca un nombre')



# creacion de la ventana principal
root = tk.Tk()
root.title('Login del juego')
root.geometry('300x300')

# Widgets
# Texto
label_titulo = tk.Label(root, text='Introduce tu nombre', font=("Consolas", 14))
label_titulo.pack(pady=10)

# Cuadro de entrada de texto
entrada_nombre = tk.Entry(root, font=("Consolas", 14))
entrada_nombre.pack(pady=10)

# boton para iniciar el juego
boton_comenzar = tk.Button(root, text= 'COMENZAR', font=("Consolas", 14), command=comenzar_juego)
boton_comenzar.pack(pady=10)

# creo un label para informar de que no se ha introducido un nombre
label_mensaje = tk.Label(root,text='', fg='red', font=("Consolas", 14))
label_mensaje.pack(pady=10)



# mantenemos ventana abierta
root.mainloop()

#cierro conexion de la base de datos
conn.close()
