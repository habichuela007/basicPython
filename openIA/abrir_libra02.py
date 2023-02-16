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
archivo_ejecutable = r"C:\Program Files\Libra\Libra.exe"
direccion_destino = "https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa"
argumentos = ['-url', direccion_destino, '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']
nombre_ventana = "LIBRA EDISA"

# Construye la lista con el comando y los argumentos
comando = [archivo_ejecutable] + argumentos

# Ejecuta el comando y espera a que termine
subprocess.run(comando)



# Obtener todas las ventanas abiertas en el escritorio
desktop = pywinauto.Desktop(backend="uia")

#Esperar a que la ventana responda
time.sleep(10)

# Buscar la ventana con título "Mi Ventana"
window_spec = desktop.window(title=nombre_ventana)

###COMPROBADO####
#print(window_spec)

#window = window_spec.window(title = nombre_ventana)
time.sleep(10)

# Esperar a que aparezca la ventana
#window = window_spec.wait('Exists')

# Conectar con la aplicación
#app = Application(backend = 'uia').connect(title=nombre_ventana)
#ventana = app.window(title_re=nombre_ventana)

# Acceder a la ventana real a través de wrapper_object()
#real_window = window_spec.wrapper_object()

# Conectar con la ventana principal de Bloc de notas
#window = comando.windows().top_window()

# Escribir "hola mundo"
#window_spec.type_keys("hola mundo")

#time.sleep(5)
# Obtener el control del campo de texto
#text_box = ventana.window(title_re=nombre_ventana).child_window(title="usuario", control_type="Edit")

# Escribir en el campo de texto
#text_box.type_keys("Texto a escribir")


# Obtener el control de la ventana de la aplicación
#app = pywinauto.application.Application()
#ventana = app.connect(title = nombre_ventana, backend = 'uia').window()
#ventana = app.window(title = nombre_ventana)
#ventana.wait('visible')

# Conectar con la aplicación

# Ahora se puede interactuar con la aplicación utilizando la referencia de la ventana

# Identificar los elementos de la interfaz de usuario para usuario y contraseña
#usuario = ventana.child_window(title='usuario', control_type='Edit')
#contrasena = ventana.child_window(title='password', control_type='Edit')

# Escribir el usuario y contraseña en los campos correspondientes
#usuario.set_text('GABRIELS')
#contrasena.set_text('Gab$1984')

# Hacer clic en el botón de "Iniciar sesión"
#boton = ventana.child_window(title='Acceder', control_type='Button')
#boton.click()