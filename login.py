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

# creo una funcion para almanezar el juego
def comenzar_juego():
    # almaceno el nombre del cuadro de entrada en una variavle
    nombre = entrada_nombre.get().strip()
    # creo condicional para forzar  la entradad del nombre
    if nombre:
        # si esite lo almaceno en la base de datos
        cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES( ?, ?)", (nombre,0))
        # confirmo cambios
        conn.commit()
        # aqui iria la llamada a la siguiente ventana
    else:
        label_mensaje.config(text='Por favor, introduzca un nombre')

# creacion de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title('Login del juego')
ventana_principal.geometry('300x300')

# Widgets
# Texto
label_titulo = tk.Label(ventana_principal, text='Introduce tu nombre', font=("Consolas", 14))
label_titulo.pack(pady=10)

# Cuadro de entrada de texto
entrada_nombre = tk.Entry(ventana_principal, font=("Consolas", 14) )
entrada_nombre.pack(pady=10)

# boton para iniciar el juego
boton_comenzar = tk.Button(ventana_principal, text= 'COMENZAR', font=("Consolas", 14), command=comenzar_juego)
boton_comenzar.pack(pady=10)

# creo un label para informar de que no se ha introducido un nombre
label_mensaje = tk.Label(ventana_principal,text='', fg='red', font=("Consolas", 14))
label_mensaje.pack(pady=10)



# mantenemos ventana abierta
ventana_principal.mainloop()

#cierro conexion de la base de datos
conn.close()
