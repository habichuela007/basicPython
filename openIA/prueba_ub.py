#Destino libra
#Se quiere pasar el usuario y contraseña
#"C:\Program Files\Libra\Libra.exe" -url https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0
#"C:\Program Files\Libra\Libra.exe" -url https://pruebas.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0
from msilib import type_key
import subprocess
import pywinauto
from pywinauto import Application, Desktop, mouse
import win32gui
import time
# Especifica la ruta del archivo ejecutable y los argumentos a pasar
parent_name = "LIBRA EDISA"
#child1_name = "GRUPO BIOALIMENTAR - v6.0.6.6.4.1"
child1_name = "####GRUPO BIOALIMENTAR#### - v6.0.6.6.4.2"
#child1_name = "Sin título - Paint"
# Ruta del archivo .exe a abrir
exe_path = r"C:\Program Files\Libra\Libra.exe"
# Argumentos del comando
arguments = ['-url', 'https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa', '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']

# Abrir el archivo .exe con los argumentos dados
app = Application().connect(title = child1_name)
# Esperar a que aparezca la ventana de inicio de sesión
parent = app.window()

child1 = app.window(title = child1_name)
print(f"***************************ESPERANDO A {child1_name}********************************")
time.sleep(1)
print(f"***************************CONTROLES {child1_name}********************************")
child1.print_control_identifiers()
print(f"***************************FIN CONTROLES {child1_name}********************************")

print("***************************OBTENER COORDENADAS APLICACION********************************")
# Obtener el identificador de la ventana de la aplicación
handle = win32gui.FindWindow(None, child1_name)
#print("handle: ", handle)

# Obtener las coordenadas del rectángulo de la ventana
rect = win32gui.GetWindowRect(handle)
#print("rect: ", rect)

# Obtener la posición x e y de la ventana en el punto superior izquierdo
#x = rect[0]
#y = rect[1]
#print(f"El punto superior izquierdo de {child1} está ubicado en la posición ({x}, {y})")

# Obtener la posición x e y de la ventana en el punto inferior derecho
x = rect[2]
y = rect[3]
#print(f"El punto inferior derecho de {child1_name} está ubicado en la posición ({x}, {y})")

sleep_type = 1
time.sleep(sleep_type)
child1.type_keys("{F7}")
time.sleep(sleep_type)
child1.type_keys("{TAB}")
time.sleep(sleep_type)
child1.type_keys("{%}GABRIEL{SPACE}ED{%}")
time.sleep(sleep_type)
child1.type_keys("{F8}")

time.sleep(sleep_type)
child1.type_keys("{TAB}")
time.sleep(sleep_type)
child1.type_keys("{TAB}")
time.sleep(sleep_type)
child1.type_keys("{TAB}")
time.sleep(sleep_type)
child1.type_keys("1803998440")
time.sleep(sleep_type)
child1.type_keys("{F10}")
time.sleep(sleep_type)
child1.type_keys("{ENTER}")
time.sleep(sleep_type)
child1.type_keys("{ESC}")
