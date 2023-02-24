#Destino libra
#Se quiere pasar el usuario y contraseña
#"C:\Program Files\Libra\Libra.exe" -url https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0
#"C:\Program Files\Libra\Libra.exe" -url https://pruebas.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0
from msilib import type_key
import subprocess
import pywinauto
from pywinauto import Application, Desktop, mouse
import time
# Especifica la ruta del archivo ejecutable y los argumentos a pasar
parent_name = "LIBRA EDISA"
main_window = "GRUPO BIOALIMENTAR - v6.0.6.6.4.1"
#main_window = "Sin título - Paint"
# Ruta del archivo .exe a abrir
exe_path = r"C:\Program Files\Libra\Libra.exe"
# Argumentos del comando
arguments = ['-url', 'https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa', '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']

# Abrir el archivo .exe con los argumentos dados
app = Application().connect(title = main_window)
window_main = app.window(title = main_window)
print("***************************ESPERA CARGA PROGRAMA********************************")
time.sleep(1)
print("***************************WINDOW MAIN********************************")
#window_main.print_control_identifiers()


import win32gui

print("***************************OBTENER COORDENADAS APLICACION********************************")
# Obtener el identificador de la ventana de la aplicación
handle = win32gui.FindWindow(None, main_window)
print("handle: ", handle)

# Obtener las coordenadas del rectángulo de la ventana
rect = win32gui.GetWindowRect(handle)
print("rect: ", rect)

# Obtener la posición x e y de la ventana
x = rect[0]
y = rect[1]
#print(f"La aplicación está ubicada en la posición ({x}, {y})")

x = rect[2]
y = rect[3]
#print(f"La aplicación está ubicada en la posición ({x}, {y})")

#Calcular la posición del clic de acuerdo a la cuadrícula
x = round(x-(x/6))
y = round(y/6)
print(f"La aplicación está ubicada en la posición ({x}, {y})")

print("***************************FIN OBTENER COORDENADAS********************************")

print("***************************HACER CLIC********************************")
mouse.click(button = "left", coords=(x,y))
time.sleep(2)
window_main.type_keys("menu{SPACE}por{SPACE}usuario")
time.sleep(2)
window_main.type_keys("{ENTER}")
print("***************************FIN HACER CLIC********************************")