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
parent_name = "LIBRA EDISA"
# Ruta del archivo .exe a abrir
exe_path = r"C:\Program Files\Libra\Libra.exe"
# Argumentos del comando
arguments = ['-url', 'https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa', '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']

# Abrir el archivo .exe con los argumentos dados
app = Application(backend='uia').start(exe_path + " " + " ".join(arguments))

time.sleep(10)
# Esperar a que aparezca la ventana de inicio de sesión
parent = app.window(title=parent_name)

print("***********************LIBRA EDISA****************************")
parent.print_control_identifiers()
time.sleep(1)

dialog = parent.Dialog()
dialog.window(title="Menu").select()