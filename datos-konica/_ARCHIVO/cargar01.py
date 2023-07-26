import os
import pandas as pd
import mysql.connector

# Variables para la conexión a la base de datos
config = {
    "user": "rpa_konica",
    "password": "Bio$1984.",
    "host": "10.20.10.93",
    "port": 33060,  # Puerto predeterminado de MySQL
    "database": "prb_impresiones",
}

# Variable para el archivo y la tabla
nombre_archivo = "552_A2WV011008573_UC_"
nombre_tabla = "552_A2WV011008573"

# Puerto de la base de datos (ajústalo al puerto correcto)
puerto_bd = 33060

# Leer el archivo de texto desde la carpeta Descargas
carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

# Buscar el archivo que comience con el nombre_archivo seguido de 8 números
for archivo in os.listdir(carpeta_descargas):
    if archivo.startswith(nombre_archivo) and archivo[len(nombre_archivo):len(nombre_archivo) + 8].isdigit():
        nombre_archivo = archivo
        break

if nombre_archivo:
    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_descargas, nombre_archivo)

    # Leer los datos desde el archivo y saltar las primeras 7 líneas
    datos = pd.read_csv(ruta_archivo, sep="\t", skiprows=6, encoding="utf-16")

    # Establecer la conexión a la base de datos MySQL
    try:
        config["port"] = puerto_bd  # Actualizar el puerto en la configuración
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        # Crear la cadena de columnas para la inserción
        columnas = list(datos.columns)
        columnas = [
            "user_name", "total_counter", "total_large_size_counter", "no_of_originals_counter",
            "no_of_prints_counter", "copy_total_total", "copy_large_size_total",
            "printer_total_total", "printer_large_size_total", "scan_total_print",
            "scan_scans", "scan_fax_tx", "scan_large_size_print", "scan_large_size_scans", "fecha_contador"
        ]

        columnas_str = ', '.join(columnas)


        # Insertar los datos en la tabla MySQL
        for _, fila in datos.iterrows():
            valores = tuple(fila)
            placeholders = ', '.join(['%s'] * len(valores))
            sql = f"INSERT INTO `{nombre_tabla}` ({columnas_str}) VALUES ({placeholders});"
            cursor.execute(sql, valores)

        conexion.commit()
        print("Datos insertados correctamente en la tabla MySQL.")

    except mysql.connector.Error as error:
        print(f"Error al conectarse a la base de datos: {error}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

else:
    print(f"No se encontró el archivo adecuado en la carpeta Descargas con el nombre: {nombre_archivo}.")