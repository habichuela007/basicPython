import tkinter as tk

# Funciones para los botones
def peso_total():
    print("Peso total")

def peso_neto():
    print("Peso neto")

# Crear la ventana
root = tk.Tk()
root.geometry("200x100")

# Crear los botones
btn_total = tk.Button(root, text="Peso total", command=peso_total)
btn_total.pack(side=tk.LEFT, padx=10, pady=10)

btn_neto = tk.Button(root, text="Peso neto", command=peso_neto)
btn_neto.pack(side=tk.RIGHT, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()