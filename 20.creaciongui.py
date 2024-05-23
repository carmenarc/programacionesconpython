import tkinter as tk
from tkinter import messagebox

# Función para manejar el evento del botón
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Hola, mundo!")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de GUI con Tkinter")

# Crear un marco
marco = tk.Frame(ventana)
marco.pack(padx=20, pady=20)

# Crear una etiqueta
etiqueta = tk.Label(marco, text="¡Hola, mundo!")
etiqueta.pack(padx=10, pady=10)

# Crear un botón
boton = tk.Button(marco, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack(padx=10, pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
