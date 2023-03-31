import tkinter as tk
from tkinter import ttk
import mysql.connector

# Crea una instancia de Tkinter
root = tk.Tk()
root.geometry('300x200')

# Crea una conexión a la base de datos
cnx = mysql.connector.connect(
    host='10.20.10.92',
    port='3306',
    user='slamper',
    password='SLMPu$239_0d',
    database='prod_pesos'
)

# Crea un cursor para ejecutar las consultas
cursor = cnx.cursor()

# Consulta para obtener los registros de la columna articulo
query = "SELECT articulo, art_descripcion FROM slamper_articulos"

# Ejecuta la consulta
cursor.execute(query)

# Obtiene los resultados de la consulta
resultados = cursor.fetchall()

# Crea una lista con las opciones para el ComboBox
opciones = [articulo[0] for articulo in resultados]

# Crea un diccionario para mapear los artículos a sus descripciones
articulos_descripciones = {articulo[0]: articulo[1] for articulo in resultados}

# Crea una variable Tkinter para almacenar la opción seleccionada
selected_option = tk.StringVar()

# Crea el ComboBox y asígnale la variable y las opciones
combo_box = ttk.Combobox(root, textvariable=selected_option, values=opciones, state="readonly")
combo_box.pack(pady=10)

# Habilita la función de autocompletado del ComboBox
#combo_box['autocomplete'] = True

# Función para mostrar la descripción del artículo seleccionado
def mostrar_descripcion(event):
    articulo = selected_option.get()
    descripcion = articulos_descripciones.get(articulo)
    art_descripcion.set(descripcion)

# Crea una variable Tkinter para almacenar la descripción del artículo seleccionado
art_descripcion = tk.StringVar()

# Crea un campo de texto para mostrar la descripción del artículo seleccionado
label_descripcion = ttk.Label(root, textvariable=art_descripcion)
label_descripcion.pack(pady=10)

# Vincula la función mostrar_descripcion al evento <<ComboboxSelected>> del ComboBox
combo_box.bind("<<ComboboxSelected>>", mostrar_descripcion)

# Ejecuta el bucle principal de Tkinter
root.mainloop()
