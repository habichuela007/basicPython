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
    lbl_total.config(text="Peso total: " + str(pTotal))

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
    lbl_total.config(text="")
    lbl_Tara.config(text="")
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
    lbl_total.config(text="")
    lbl_Tara.config(text="")



# Crear la ventana
root = tk.Tk()
root.geometry("900x400")

# Crear el cuadro de entrada de peso
peso = tk.Entry(root, width=10, font=("Arial", 80))
peso.pack(pady=20)

# Crear los botones
btn_total = tk.Button(root, text="Peso total", font=("Arial", 25), command=peso_total)
btn_total.pack(side=tk.LEFT, padx=25)

btn_Tara = tk.Button(root, text="Peso Tara", font=("Arial", 25), command=peso_Tara)
btn_Tara.pack(side=tk.LEFT, padx=25)

btn_enviar = tk.Button(root, text="Enviar", font=("Arial", 25), command=enviar)
btn_enviar.pack(side=tk.RIGHT, padx=25)

btn_reiniciar = tk.Button(root, text="Reiniciar Pesada", font=("Arial", 25), command=reiniciar)
btn_re
