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




child1 = parent.window(title="Sistema", auto_id="MenuBar", control_type="MenuBar")
child1 = parent.child_window(title="Sistema", auto_id="MenuBar", control_type="MenuBar")
print("******************CHILD1**********************")
child1.print_control_identifiers()

child2 = child1.window(title="Sistema", control_type="MenuItem")
child2 = child1.child_window(title="Sistema", control_type="MenuItem")
print("******************CHILD2**********************")
child2.print_control_identifiers()

#sistema1_control = child1.child_window(title="Sistema", auto_id="MenuBar", control_type="MenuItem")
#sistema1_control.click_input()

#minimizar_control = parent.child_window(title="Minimizar", control_type="Button")
#minimizar = minimizar_control.wrapper_object()
#minimizar.click()

controls = child2.children()

# iterar sobre los controles secundarios y encontrar los campos de entrada de texto
text_fields = []
for control in controls:
    if control.get_properties()['control_type'] == 'Edit':
        text_fields.append(control)

# imprimir los campos de entrada de texto encontrados
for field in text_fields:
    print(f"Nombre del campo: {field.get_properties()['friendly_class_name']}")


time.sleep(3)
parent.type_keys("gabriels{TAB}")
time.sleep(1)
parent.type_keys("1803998440")
time.sleep(1)
parent.type_keys("{ENTER}")

