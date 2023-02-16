from pywinauto import Desktop

# Obtener todos los elementos de la ventana en el escritorio
windows = Desktop(backend="uia").windows()

# Buscar la ventana de LIBRA EDISA por título
libra_window = None
for window in windows:
    if window.window_text().startswith("LIBRA EDISA"):
        libra_window = window
        print(libra_window.window_text())
        break

# Si se encontró la ventana, imprimir sus elementos hijo
if libra_window:
    for child_window in libra_window.children():
        print(child_window.window_text())
else:
    print("No se encontró la ventana de LIBRA EDISA")