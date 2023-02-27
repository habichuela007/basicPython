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
# Ruta del archivo .exe a abrir
exe_path = r"C:\Program Files\Libra\Libra.exe"
# Argumentos del comando
arguments = ['-url', 'https://pruebas.bioalimentar.com:443/forms/frmservlet?config=libra_saa', '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']
# Abrir el archivo .exe con los argumentos dados
app = Application(backend='uia').start(exe_path + " " + " ".join(arguments))

# Esperar a que aparezca la ventana de inicio de sesión
print(f"***************************ESPERANDO A {parent_name}********************************")
time.sleep(15)
parent = app.window(title=parent_name)

print(f"***************************CONTROLES {parent_name}********************************")
parent.print_control_identifiers()
print(f"***************************FIN CONTROLES {parent_name}********************************")

print(f"***************************EMPIEZA INICIO DE SESION********************************")
time.sleep(4)
parent.type_keys("gabriels{TAB}")
time.sleep(1)
parent.type_keys("Gab$1984")
time.sleep(1)
parent.type_keys("{ENTER}")
print("***************************TERMINA INICIO DE SESION********************************")

child1 = app.window(title = child1_name)
print(f"***************************ESPERANDO A {child1_name}********************************")
time.sleep(15)
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

print("***************************BUSCANDO CAMPO 'BUSCAR' ********************************")
#Calcular la posición del clic de acuerdo a la cuadrícula
x = round(x-(x/6))
y = round(y/6)
print(f"El campo 'BUSCAR' está ubicado en la posición ({x}, {y})")

print("***************************FIN OBTENER COORDENADAS CAMPO 'BUSCAR'********************************")

print("***************************ABRIR 'MENU POR USUARIO'********************************")
mouse.click(button = "left", coords=(x,y))
time.sleep(2)
child1.type_keys("menu{SPACE}por{SPACE}usuario")
time.sleep(2)
child1.type_keys("{ENTER}")
print("***************************FIN ABRIR 'MENU POR USUARIO'********************************")

# Obtener la posición x e y de la ventana en el punto inferior derecho
x = rect[2]
y = rect[3]
#print(f"El punto inferior derecho de {child1_name} está ubicado en la posición ({x}, {y})")
time.sleep(2)

print("***************************BUSCANDO CAMPO 'CARGOS COLABORADORES'********************************")
#Calcular la posición del clic de acuerdo a la cuadrícula
x = round(x/8)
y = round(y/4.5)
print(f"El campo Cargos Colaboradores está ubicado en la posición ({x}, {y})")
time.sleep(2)
mouse.double_click(button = "left", coords=(x,y))
print("***************************FIN BUSCANDO CAMPO 'CARGOS COLABORADORES'********************************")

#Volver a cargar x e y#
x = rect[2]
y = rect[3]
print(f"El punto inferior derecho de {child1_name} está ubicado en la posición ({x}, {y})")

print("***************************BUSCANDO CAMPO 'BOTON EXPORTAR EXCEL'********************************")
#Calcular la posición del botón EXCEL de acuerdo a la cuadrícula
x = round(x/5.5)
y = round(y-(y/1.085))
print(f"El campo EXCEL está ubicado en la posición ({x}, {y})")
mouse.click(button = "left", coords=(x,y))
print("***************************FIN BUSCANDO CAMPO 'BOTON EXPORTAR EXCEL'********************************")

print("***************************OK A GUARDAR********************************")
child1 = app.window(title = child1_name)
child1.print_control_identifiers()
time.sleep(15)
child1.type_keys("{ENTER}")
print("***************************FIN OK A GUARDAR********************************")

print("***************************WINDOW MAIN********************************")