from pywinauto import Application
from pywinauto.timings import TimeoutError
import time

# Especifica la ruta del archivo ejecutable y los argumentos a pasar
parent_name = "LIBRA EDISA"
#child1_name = "GRUPO BIOALIMENTAR - v6.0.6.6.4.1"
child1_name = "####GRUPO BIOALIMENTAR#### - v6.0.6.6.4.2"
# Ruta del archivo .exe a abrir
exe_path = r"C:\Program Files\Libra\Libra.exe"
# Argumentos del comando

# Argumentos del comando
arguments = ['-url', 'https://pruebas.bioalimentar.com:443/forms/frmservlet?config=libra_saa', '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']

# Abre la aplicación
try:
    print(f"***************************LLAMANDO CON ARGUMENTOS A {parent_name}********************************")
    timeout_seconds = 60
    app = Application(backend='uia').start(exe_path + " " + " ".join(arguments), timeout=timeout_seconds)
except TimeoutError:
    print(f"Error: La aplicación no pudo abrirse dentro de {timeout_seconds} segundos.")
    exit()

#Espera a que aparezca la ventana de inicio de sesión
try:
    print(f"***************************ESPERANDO A {parent_name}********************************")
    app.window(title_re=parent_name).wait('ready', timeout=30)
except TimeoutError:
    print("Error: La ventana 'LIBRA EDISA' no apareció dentro del tiempo de espera.")
    app.kill()
    exit()

# Acceder a la ventana principal
print(f"***************************ACCEDIENDO A {parent_name}********************************")
main_window = app.window(title=parent_name)

# Realizar acciones en la ventana principal
main_window.type_keys("usuario{TAB}")
main_window.type_keys("password")
main_window.type_keys("{ENTER}")

# Esperar a que aparezca la ventana hija
child_window = app.window(title="####GRUPO BIOALIMENTAR#### - v6.0.6.6.4.2")
child_window.wait('ready')

# Realizar acciones en la ventana hija
child_window.type_keys("menu{SPACE}por{SPACE}usuario")
child_window.type_keys("{ENTER}")

# Continuar con las interacciones...

# Cerrar la aplicación al final
#app.kill()
