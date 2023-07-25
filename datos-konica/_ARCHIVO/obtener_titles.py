from pywinauto import Desktop

# Obtener todos los elementos de la ventana en el escritorio
windows = Desktop(backend="uia").windows()

# Imprimir los títulos de las ventanas
for window in windows:
    print(window.window_text())
    #print(window)