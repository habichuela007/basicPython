#Destino libra
#Se quiere pasar el usuario y contraseña
#"C:\Program Files\Libra\Libra.exe" -url https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0
#"C:\Program Files\Libra\Libra.exe" -url https://pruebas.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0

from msilib import type_key
import subprocess
import pywinauto
from pywinauto import Application, Desktop
import time
# Especifica la ruta del archivo ejecutable y los argumentos a pasar
nombre_ventana = "LIBRA EDISA"
# Ruta del archivo .exe a abrir
exe_path = r"C:\Program Files\Libra\Libra.exe"
# Argumentos del comando
arguments = ['-url', 'https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa', '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']

# Abrir el archivo .exe con los argumentos dados
app = Application(backend='uia').start(exe_path + " " + " ".join(arguments))


# Crea una instancia de Application
app2 = pywinauto.Application(backend='uia')

time.sleep(10)
# Conecta a una ventana por su título
window = app2.connect(title=nombre_ventana)
print("window: ", window)

time.sleep(10)
login = window.menu()

time.sleep(10)

# Obtener el objeto del control de texto
control = login.window_control(title=nombre_ventana)
print("control ", control)

# Obtener el texto del control
texto = control.window_text()
print("texto: ", texto)