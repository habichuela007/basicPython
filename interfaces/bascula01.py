import tkinter as tk
import serial
import mysql.connector

# Configuración de la conexión serial
serial_port = 'COM3'
baud_rate = 9600
#ser = serial.Serial(serial_port, baud_rate)

# Configuración de la conexión a la base de datos MySQL
db_host = '10.20.10.93'
db_user = 'root'
db_pass = 'Bio.1234'
db_name = 'prb_analitica'
db_table = 'peso2_slamper'
db_connection = mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
db_cursor = db_connection.cursor()

# Funciones para los botones
def peso_total():
#    peso = ser.readline().decode().strip()
    lbl_peso_total.config(text=peso)
    sql = f"UPDATE {db_table} SET peso_total = {peso} WHERE id = 1"
    db_cursor.execute(sql)
    db_connection.commit()

def peso_neto():
#    peso = ser.readline().decode().strip()
    lbl_peso_neto.config(text=peso)
    sql = f"UPDATE {db_table} SET peso_neto = {peso} WHERE id = 1"
    db_cursor.execute(sql)
    db_connection.commit()

# Crear la ventana
root = tk.Tk()
root.geometry("400x200")

# Crear los botones
btn_total = tk.Button(root, text="Peso total", command=peso_total)
btn_total.pack(side=tk.LEFT, padx=10, pady=10)

btn_neto = tk.Button(root, text="Peso neto", command=peso_neto)
btn_neto.pack(side=tk.RIGHT, padx=10, pady=10)

# Crear el indicador de peso total
lbl_total = tk.Label(root, text="Peso total:", font=("Arial Bold", 20))
lbl_total.pack(padx=10, pady=10)
lbl_peso_total = tk.Label(root, text="0", font=("Arial Bold", 20))
lbl_peso_total.pack(padx=10, pady=10)

# Crear el indicador de peso neto
lbl_neto = tk.Label(root, text="Peso neto:", font=("Arial Bold", 20))
lbl_neto.pack(padx=10, pady=10)
lbl_peso_neto = tk.Label(root, text="0", font=("Arial Bold", 20))
lbl_peso_neto.pack(padx=10, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
