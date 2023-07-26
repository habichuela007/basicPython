import os
import shutil

def buscar_archivo(nombre_archivo):
    # Leer el archivo de texto desde la carpeta Descargas
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    # Buscar el archivo que comience con el nombre_archivo seguido de 8 números
    for archivo in os.listdir(carpeta_descargas):
        if archivo.startswith(nombre_archivo) and archivo[len(nombre_archivo):len(nombre_archivo) + 8].isdigit():
            return os.path.join(carpeta_descargas, archivo)

def mover_archivo(archivo):
    archivo_encontrado = buscar_archivo(archivo)
    if archivo_encontrado:
        # Ruta destino donde se moverá el archivo
        ruta_destino = r"\\10.20.10.15\flux\impresora\DATA"

        # Mover el archivo encontrado a la ubicación especificada
        try:
            shutil.move(archivo_encontrado, os.path.join(ruta_destino, os.path.basename(archivo_encontrado)))
            print(f"Archivo movido correctamente a {ruta_destino}")
        except shutil.Error as e:
            print(f"Error al mover el archivo: {e}")

nombre_archivo = "223_A1UG011006937_UC_"
mover_archivo(nombre_archivo)
