from pywinauto.application import Application
import os

# Ruta de la aplicación de Bloc de notas
notepad_path = r"C:\Windows\System32\notepad.exe"

# Iniciar la aplicación de Bloc de notas
app = Application().start(notepad_path)

# Conectar con la ventana principal de Bloc de notas
notepad_window = app.top_window()

# Escribir "hola mundo"
notepad_window.type_keys("hola mundo")

# Guardar el archivo en la carpeta Descargas
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
filename = "hola_mundo.txt"

notepad_window.menu_select("Archivo -> Guardar como")
save_as_window = app.window(title="Guardar como")

# Escribir el nombre del archivo
save_as_window["Archivo &de nombre:"].type_keys(filename)

# Navegar a la carpeta Descargas
save_as_window["Explorador de archivos"].click_input()
file_name_box = save_as_window["Archivo &de nombre:"]
file_name_box.type_keys(downloads_path)
save_as_window["Guardar"].click_input()