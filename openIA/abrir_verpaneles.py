#Destino libra
#Se quiere pasar el usuario y contraseña
#"C:\Program Files\Libra\Libra.exe" -url https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0
#"C:\Program Files\Libra\Libra.exe" -url https://pruebas.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0

from msilib import type_key
import subprocess
import pywinauto
from pywinauto import Application, Desktop
from pywinauto.findwindows import find_window
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

# Definir los nombres de las ventanas, paneles y controles necesarios
app_name = "LIBRA EDISA"
window_name = "LIBRA EDISA"
panel_name = "LIBRA - Chromium"
control_type = "edit"
control_id = 50004

# Encontrar la aplicación "LIBRA EDISA"
app = Application().connect(title=app_name)

# Obtener la ventana "LIBRA EDISA"
time.sleep(10)
win = app.window(title=window_name)
print("************************WIN********************")
win.print_control_identifiers(depth=10)

# Establecer la ventana como activa
win.set_focus()

# Encontrar el panel "LIBRA - Chromium"
panel = win[panel_name]
print("************************PANEL********************")
panel.print_control_identifiers()

# Encontrar el control "edit(50004)" dentro del panel
control = panel.child_window(control_type=control_type, control_id=control_id)
print("************************CONTROL********************")
control.print_control_identifiers()

# Escribir el texto "GABRIELS" en el control
control.set_text("GABRIELS")
