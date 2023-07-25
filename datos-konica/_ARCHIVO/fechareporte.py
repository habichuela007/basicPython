import os

def leer_fecha_desde_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            # Leer las primeras tres líneas
            for _ in range(4): #con el valor 2, lee la serie
                linea = file.readline()
                #print(linea)

            # Leer la tercera línea y obtener la fecha
            tercera_linea = file.readline().rstrip('\n')
            elementos_tercera_linea = tercera_linea.split('\t')
            if len(elementos_tercera_linea) > 4:
                fecha = elementos_tercera_linea[4]
                return fecha
            else:
                print("Error: No se encontró la fecha en la tercera línea.")
                return None

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")
        return None

# Variable para el archivo
nombre_archivo = "552_A2WV011008573_UC_"

# Ruta completa del archivo a procesar (en la carpeta Descargas del usuario)
carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

# Buscar el archivo que comience con el nombre_archivo seguido de 8 números
for archivo in os.listdir(carpeta_descargas):
    if archivo.startswith(nombre_archivo) and archivo[len(nombre_archivo):len(nombre_archivo) + 8].isdigit():
        nombre_archivo = archivo
        break

archivo = os.path.join(carpeta_descargas, nombre_archivo)
fecha_leida = leer_fecha_desde_archivo(archivo)

if fecha_leida is not None:
    print("Fecha leída desde el archivo:")
    print(fecha_leida)
