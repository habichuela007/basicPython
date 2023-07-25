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

# Puerto de la base de datos (ajústalo al puerto correcto)
puerto_bd = 33060

def buscar_archivo(nombre_archivo):
    # Leer el archivo de texto desde la carpeta Descargas
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    # Buscar el archivo que comience con el nombre_archivo seguido de 8 números
    for archivo in os.listdir(carpeta_descargas):
        if archivo.startswith(nombre_archivo) and archivo[len(nombre_archivo):len(nombre_archivo) + 8].isdigit():
            return archivo

def obtener_fecha(archivo):
    try:
        with open(archivo, 'r') as file:
            # Leer las primeras tres líneas
            for _ in range(4):
                linea = file.readline()

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


def convertir_fecha_formato(fecha):
    try:
        fecha_objeto = pd.to_datetime(fecha, dayfirst=True)  # Convertir a objeto de fecha y hora
        fecha_formateada = fecha_objeto.strftime("%Y-%m-%d %H:%M")  # Formatear la fecha como "YYYY-MM-DD HH:MM"
        return fecha_formateada
    except ValueError:
        print(f"Error: La fecha '{fecha}' tiene un formato inválido.")
        return None
    

def cargar_datos_t1(nombre_archivo, nombre_tabla):
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    archivo = buscar_archivo(nombre_archivo)

    if archivo:
        # Ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

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
            #print("Datos insertados correctamente en la tabla MySQL.")
            
        except mysql.connector.Error as error:
            print(nombre_tabla)
            print(f"Error al conectarse a la base de datos: {error}")

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    else:
        print(f"No se encontró el archivo adecuado en la carpeta Descargas con el nombre: {nombre_archivo}.")
    
    if archivo:
        # Obtener la fecha desde el archivo
        fecha = obtener_fecha(os.path.join(carpeta_descargas, archivo))
        #print("Fecha leída desde el archivo:")
        #print(fecha)

        # Convertir la fecha al formato adecuado
        fecha_formateada = convertir_fecha_formato(fecha)
        if fecha_formateada:
            try:
                config["port"] = puerto_bd  # Actualizar el puerto en la configuración
                conexion = mysql.connector.connect(**config)
                cursor = conexion.cursor()

                # Crear la cadena de columnas para la actualización
                sql = f"UPDATE `{nombre_tabla}` SET fecha_contador = %s WHERE fecha_contador IS NULL"
                values = (fecha_formateada,)
                cursor.execute(sql, values)

                conexion.commit()
                #print("Fecha actualizada correctamente en la tabla MySQL.")

            except mysql.connector.Error as error:
                print(f"Error al conectarse a la base de datos: {error}")

            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()

    else:
        print(f"No se encontró el archivo adecuado en la carpeta Descargas con el nombre: {nombre_archivo}.")

def cargar_datos_t2(nombre_archivo, nombre_tabla):
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    archivo = buscar_archivo(nombre_archivo)

    if archivo:
        # Ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

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
            "user_name",
            "total_counter",
            "total_large_size_counter",
            "no_of_originals_counter",
            "no_of_prints_counter",
            "duplex_print_counter",
            "total_no_pages_output",
            "copy_total_total",
            "copy_total_full_color",
            "copy_total_black",
            "copy_total_2color",
            "copy_total_single_color",
            "copy_large_size_total",
            "copy_large_size_full_color",
            "copy_large_size_black",
            "copy_large_size_2color",
            "copy_large_size_single_color",
            "printer_total_total",
            "printer_total_full_color",
            "printer_total_black",
            "printer_total_2color",
            "printer_large_size_total",
            "printer_large_size_full_color",
            "printer_large_size_black",
            "printer_large_size_2color",
            "color_total_full_color",
            "color_total_black",
            "color_total_2color",
            "color_total_single_color",
            "color_large_size_full_color",
            "color_large_size_black",
            "color_large_size_2color",
            "color_large_size_single_color",
            "scan_total_print_full_color",
            "scan_total_print_black",
            "scan_total_scans",
            "scan_total_fax_tx",
            "scan_large_size_print_full_color",
            "scan_large_size_print_black",
            "scan_large_size_scans",
            "fecha_contador"
            ]
            columnas_str = ', '.join(columnas)

            # Insertar los datos en la tabla MySQL
            for _, fila in datos.iterrows():
                valores = tuple(fila)
                placeholders = ', '.join(['%s'] * len(valores))
                sql = f"INSERT INTO `{nombre_tabla}` ({columnas_str}) VALUES ({placeholders});"
                cursor.execute(sql, valores)
            conexion.commit()
            #print("Datos insertados correctamente en la tabla MySQL.")
            
        except mysql.connector.Error as error:
            print(nombre_tabla)
            print(f"Error al conectarse a la base de datos: {error}")

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    else:
        print(f"No se encontró el archivo adecuado en la carpeta Descargas con el nombre: {nombre_archivo}.")
    
    if archivo:
        # Obtener la fecha desde el archivo
        fecha = obtener_fecha(os.path.join(carpeta_descargas, archivo))
        #print("Fecha leída desde el archivo:")
        #print(fecha)

        # Convertir la fecha al formato adecuado
        fecha_formateada = convertir_fecha_formato(fecha)
        if fecha_formateada:
            try:
                config["port"] = puerto_bd  # Actualizar el puerto en la configuración
                conexion = mysql.connector.connect(**config)
                cursor = conexion.cursor()

                # Crear la cadena de columnas para la actualización
                sql = f"UPDATE `{nombre_tabla}` SET fecha_contador = %s WHERE fecha_contador IS NULL"
                values = (fecha_formateada,)
                cursor.execute(sql, values)

                conexion.commit()
                #print("Fecha actualizada correctamente en la tabla MySQL.")

            except mysql.connector.Error as error:
                print(f"Error al conectarse a la base de datos: {error}")

            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()

    else:
        print(f"No se encontró el archivo adecuado en la carpeta Descargas con el nombre: {nombre_archivo}.")

# Variable para el archivo y la tabla
nombre_archivo = "283_A1UF011003305_UC_"
nombre_tabla = "283_A1UF011003305"
cargar_datos_t1(nombre_archivo,nombre_tabla)

nombre_archivo = "223_A1UG011006937_UC_"
nombre_tabla = "223_A1UG011006937"
cargar_datos_t1(nombre_archivo,nombre_tabla)

nombre_archivo = "224e_A61H011006163_UC_"
nombre_tabla = "224e_A61H011006163"
cargar_datos_t2(nombre_archivo,nombre_tabla)

nombre_archivo = "363_A1UE011015445_UC_"
nombre_tabla = "363_A1UE011015445"
cargar_datos_t1(nombre_archivo,nombre_tabla)

nombre_archivo = "363_A1UE011016227_UC_"
nombre_tabla = "363_A1UE011016227"
cargar_datos_t1(nombre_archivo,nombre_tabla)

nombre_archivo = "363_A1UE011104367_UC_"
nombre_tabla = "363_A1UE011104367"
cargar_datos_t1(nombre_archivo,nombre_tabla)

nombre_archivo = "364e_A61F011024714_UC_"
nombre_tabla = "364e_A61F011024714"
cargar_datos_t2(nombre_archivo,nombre_tabla)

nombre_archivo = "552_A2WV011008573_UC_"
nombre_tabla = "552_A2WV011008573"
cargar_datos_t1(nombre_archivo,nombre_tabla)

nombre_archivo = "C227_A798011501042_UC_"
nombre_tabla = "C227_A798011501042"
cargar_datos_t2(nombre_archivo,nombre_tabla)

nombre_archivo = "C554e_A5AY011013622_UC_"
nombre_tabla = "C554e_A5AY011013622"
cargar_datos_t2(nombre_archivo,nombre_tabla)

