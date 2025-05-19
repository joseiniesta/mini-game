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
    {
        "pregunta" : "¿Cual es la capital de Bélgica?",
        "opciones" : {"A": "Bruselas", "B": "Copenhague","C": "Madrid"}
        "respuesta" : "A"
    },
    {
        "pregunta" : "¿Cual es la capital de Argentina?",
        "opciones" : {
            "A": "Amsterdan",
            "B": "Lisboa",
            "C": "Buenos Aires"}
        "respuesta" : "C"
    },
    {
        "pregunta" : "¿Cual es la capital de Repunlica Checa?",
        "opciones" : {
            "A": "Praga",
            "B": "Asmara",
            "C": "Atenas"}
        "respuesta" : "A"
    }
]

def mostrar_pregunta(nombre_jugador, indice):
    if indice >= len(preguntas):
        print("Juego terminado")
        return
    
    datos = preguntas[indice]
    ventana = tk.Tk()
    ventana.title(f"Pregunta {indice + 1}")
    ventana.geometry("400x250")

    #accion al respopnder
    def responder(eleccion):
        if eleccion == datos["respuesta"]:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?", (nombre_jugador,))
            conn.commit()
        ventana.destroy()
        mostrar_pregunta(nombre_jugador, indice + 1)

    #mosstrar contenido 
    tk.Label(ventana, text=datos["pregunta"], font=("Arial", 14), wraplength=350).pack(pady=20)
    for clave, valor in datos["opciones"].items():
        texto = f"{clave} {valor}"
        tk.Button(ventana, text=texto, command=lambda :responder(clave),)



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
