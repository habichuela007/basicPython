import mysql.connector
import tkinter as tk

# Crear la conexión a la base de datos
conexion = mysql.connector.connect(
    host='10.20.10.93',
    port='33060',
    user='root',
    password='Bio.1234',
    database='prb_analitica'
)
cursor = conexion.cursor()

# Funciones para los botones
def peso_total():
    global pTotal
    pTotal = float(peso.get())
    lbl_total.config(text="Peso Total: " + str(pTotal))

def peso_Tara():
    global pTara
    pTara = float(peso.get())
    lbl_Tara.config(text="Peso Tara: " + str(pTara))

def enviar():  
    global pNeto
    pNeto = pTotal - pTara
    sql = "INSERT INTO peso_slamper (peso_total, peso_Tara, peso_neto) VALUES (%s, %s, %s)"
    values = (pTotal, pTara, pNeto)
    cursor.execute(sql, values)
    conexion.commit()
    peso.delete(0, 'end')
    lbl_total.config(text="Peso Total: ")
    lbl_Tara.config(text="Peso Tara: ")
    update_pesada_id()

def update_pesada_id():
    # Obtener el último pesada_id
    sql = "SELECT pesada_id FROM peso_slamper ORDER BY pesada_id DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    last_id = result[0] if result else 0
    # Actualizar el Label con el pesada_id + 1
    lbl_pesada_id.config(text="Pesada ID: " + str(last_id + 1))

def reiniciar():
    global pTotal, pTara, pNeto
    pTotal = 0
    pTara = 0
    pNeto = 0
    peso.delete(0, 'end')
    lbl_total.config(text="Peso Total: ")
    lbl_Tara.config(text="Peso Tara: ")

# Crear la ventana
root = tk.Tk()
root.geometry("900x400")

# Crear el cuadro de entrada de peso
peso = tk.Entry(root, width=10, font=("Arial", 80))
peso.pack(pady=20)

# Crear los contenedores para cada fila de indicadores
row1 = tk.Frame(root)
row2 = tk.Frame(root)
row3 = tk.Frame(root)

# Ordenar los contenedores utilizando el método pack()
row1.pack()
row2.pack()
row3.pack()

# Crear los botones
btn_total = tk.Button(row2, text="Peso total", font=("Arial", 25), command=peso_total)
btn_total.pack(side=tk.LEFT, padx=25, fill=tk.X, expand=True)

btn_Tara = tk.Button(row3, text="Peso Tara", font=("Arial", 25), command=peso_Tara)
btn_Tara.pack(side=tk.LEFT, padx=25, fill=tk.X, expand=True)

btn_enviar = tk.Button(row2, text="Enviar", font=("Arial", 25), command=enviar)
btn_enviar.pack(side=tk.LEFT, padx=25, fill=tk.X, expand=True)

btn_reiniciar = tk.Button(row3, text="Reiniciar", font=("Arial", 15), command=reiniciar)
btn_reiniciar.pack(side=tk.LEFT, padx=25, fill=tk.X, expand=True)

# Crear los visualizadores de peso total y peso Tara
lbl_total = tk.Label(row2, font=("Arial", 25))
lbl_total.pack(side=tk.RIGHT, pady=10)

lbl_Tara = tk.Label(row3, font=("Arial", 25))
lbl_Tara.pack(side=tk.RIGHT, pady=10)

# Crear el visualizador de pesada_id
lbl_pesada_id = tk.Label(row1, font=("Arial", 25))
lbl_pesada_id.pack(side=tk.TOP, pady=10)

# Actualizar el Label de pesada_id
update_pesada_id()

# Iniciar el bucle principal de la ventana
root.mainloop()