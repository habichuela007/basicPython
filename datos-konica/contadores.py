import webbrowser
import time
import pywinauto.keyboard as keyboard
from pywinauto import Desktop
import os
import subprocess
import re
import sys
import datetime
import shutil
import pandas as pd
import mysql.connector
import pyautogui

pyautogui.FAILSAFE = False


# Variables para la conexión a la base de datos
config = {
    "user": "rpa_konica",
    "password": "Bio$1984.",
    "host": "10.20.10.94",
    "port": 3306,  # Puerto predeterminado de MySQL
    "database": "prb_impresiones",
}

# Puerto de la base de datos (ajústalo al puerto correcto)
puerto_bd = 3306

def ingresar(url,t_ingreso):
    webbrowser.open(url, new=2)
    # Cambia a modo administrador
    time.sleep(25)
    for _ in range (t_ingreso):
        keyboard.send_keys("{TAB}")                      
    time.sleep(1)
    keyboard.send_keys("{DOWN}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    # INGRESA CONTRASEÑA
    time.sleep(2)
    keyboard.send_keys("{TAB 4}")                       
    time.sleep(1)
    for numero in range(1, 9):
        #keyboard.send_keys(str(numero))
        pyautogui.write(str(numero))
        #print(numero)
        time.sleep(0.1)
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    time.sleep(8)  


def verificar_ingreso(url, t_import_export, t_contador, t_salir):
    # Obtener todos los elementos de la ventana en el escritorio
    time.sleep(2)
    windows = Desktop(backend="uia").windows()
    # Buscar la ventana de KONICA por título
    konica_window = None
    for window in windows:
        if window.window_text().startswith("Mantenimiento") or window.window_text().startswith("Contador"):
            konica_window = window
            break
    # Si se encontró la ventana, Descargar
    if konica_window:
        descargar_contador(t_import_export, t_contador, t_salir)
        time.sleep(2)
    else:
        mensaje_log = f"{datetime.datetime.now()} - {url} No se pudo ingresar"
        escribir_log(nombre_archivo_log,mensaje_log)
        time.sleep(2)        


def descargar_contador(t_import_export,t_contador,t_salir):
    # IR IMPORTAR/EXPORTAR
    time.sleep(6)
    for _ in range (t_import_export):
        keyboard.send_keys("{TAB}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")      
    
    # SELECCCIONAR RADIUS CONTADOR
    time.sleep(8)
    for _ in range (t_contador):
        keyboard.send_keys("{TAB}")  
    time.sleep(1)
    keyboard.send_keys("{DOWN}")                       
    time.sleep(1)
    keyboard.send_keys("{TAB}")
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       

    # IR A CONTADOR DE USUARIO
    time.sleep(1)
    keyboard.send_keys("{TAB}")                       
    time.sleep(1)
    keyboard.send_keys("{DOWN}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    # DESCARGAR
    time.sleep(8)
    keyboard.send_keys("{TAB}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       

    #REGRESAR
    time.sleep(10)
    keyboard.send_keys("{TAB}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       

    # SELECCIONAR CERRAR SESIÓN
    time.sleep(8)
    keyboard.send_keys("{TAB 4}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       

    time.sleep(5)
    for _ in range (t_salir):
        keyboard.send_keys("{TAB}")                         
    time.sleep(1)
    keyboard.send_keys("{ENTER}")   
    time.sleep(1)


def verificar_descarga(patron_fecha,carpeta_descargas):
    # Busca el archivo en la carpeta de descargas que cumpla con el patrón de la fecha.
    archivo_descargado = None
    for nombre_archivo in os.listdir(carpeta_descargas):
        if re.search(patron_fecha, nombre_archivo):
            archivo_descargado = os.path.join(carpeta_descargas, nombre_archivo)
            break

    if archivo_descargado:

        # Enviar el atajo Ctrl+Alt+Delete
        pyautogui.hotkey('alt','f4')
        #print(f"El archivo {archivo_descargado} se descargó exitosamente.")
    else:
        mensaje_log = f"{datetime.datetime.now()} - {url} Archivo No encontrado"
        escribir_log(nombre_archivo_log,mensaje_log)


def escribir_log(nombre_archivo_log,mensaje_log):
    # Obtener la ruta completa del archivo de log
    ruta_archivo_log = os.path.join(os.path.expanduser("~"), "Documents\log\contadores", nombre_archivo_log)

    # Abre el archivo de log en modo de apendizaje (si no existe, se creará)
    with open(ruta_archivo_log, "a") as archivo_log:
        # Redirige la salida estándar al archivo de log
        sys.stdout = archivo_log
        print(mensaje_log)
        sys.stdout = sys.__stdout__  # Restaura la salida estándar original


def buscar_archivo(nombre_archivo):
    # Leer el archivo de texto desde la carpeta Descargas
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    # Buscar el archivo que comience con el nombre_archivo seguido de 8 números
    for archivo in os.listdir(carpeta_descargas):
        if archivo.startswith(nombre_archivo) and archivo[len(nombre_archivo):len(nombre_archivo) + 8].isdigit():
            return archivo


def buscar_archivo_path(nombre_archivo):
    # Leer el archivo de texto desde la carpeta Descargas
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    # Buscar el archivo que comience con el nombre_archivo seguido de 8 números
    for archivo in os.listdir(carpeta_descargas):
        if archivo.startswith(nombre_archivo) and archivo[len(nombre_archivo):len(nombre_archivo) + 8].isdigit():
            return os.path.join(carpeta_descargas, archivo)


def mover_archivo(archivo):
    archivo_encontrado = buscar_archivo_path(archivo)
    if archivo_encontrado:
        # Ruta destino donde se moverá el archivo
        ruta_destino = r"\\10.20.10.15\flux\impresora\DATA"

        # Mover el archivo encontrado a la ubicación especificada
        try:
            shutil.move(archivo_encontrado, os.path.join(ruta_destino, os.path.basename(archivo_encontrado)))
            #print(f"Archivo movido correctamente a {ruta_destino}")
        except shutil.Error as e:
            mensaje_log = f"{datetime.datetime.now()} - {archivo} Archivo No encontrado"
            escribir_log(nombre_archivo_log,mensaje_log)
            #print(f"Error al mover el archivo: {e}")


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

        # Llenar los valores NaN con ceros
        datos.fillna("NULL", inplace=True)

        # Obtener la fecha desde el archivo
        fecha = obtener_fecha(os.path.join(carpeta_descargas, archivo))
        #print("Fecha leída desde el archivo:")
        #print(fecha)

        # Convertir la fecha al formato adecuado
        fecha_formateada = convertir_fecha_formato(fecha)

        try:
            config["port"] = puerto_bd  # Actualizar el puerto en la configuración
            conexion = mysql.connector.connect(**config)
            cursor = conexion.cursor()

            # Crear la cadena de columnas para la inserción
            columnas = list(datos.columns)
            columnas = [
                "user_name", "total_counter", "total_large_size_counter", "no_of_originals_counter","no_of_prints_counter", "copy_total_total", "copy_large_size_total","printer_total_total", "printer_large_size_total", "scan_total_print","scan_scans", "scan_fax_tx", "scan_large_size_print", "scan_large_size_scans", "fecha_contador"
            ]

            columnas_str = ', '.join(columnas)

            # Insertar los datos en la tabla MySQL
            for _, fila in datos.iterrows():
                valores = tuple(fila)
                placeholders = ', '.join(['%s'] * len(valores))
                sql = f"INSERT INTO `{nombre_tabla}` ({columnas_str}) VALUES ({placeholders});"
                cursor.execute(sql, valores)

            # Actualizar la fecha en la tabla MySQL si es válida
            if fecha_formateada:
                sql = f"UPDATE `{nombre_tabla}` SET fecha_contador = %s WHERE fecha_contador = 'NULL'"
                values = (fecha_formateada,)
                cursor.execute(sql, values)

            conexion.commit()

            mover_archivo(nombre_archivo)


        except mysql.connector.Error as error:
            mensaje_log = f"{datetime.datetime.now()} - {nombre_archivo} Error mysql {error}"
            escribir_log(nombre_archivo_log, mensaje_log)

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
       
    else:
        mensaje_log = f"{datetime.datetime.now()} - {archivo} No se encontró el archivo en Descargas {nombre_archivo}"
        escribir_log(nombre_archivo_log, mensaje_log)


def cargar_datos_t2(nombre_archivo, nombre_tabla):
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    archivo = buscar_archivo(nombre_archivo)

    if archivo:
        # Ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

        # Leer los datos desde el archivo y saltar las primeras 7 líneas
        datos = pd.read_csv(ruta_archivo, sep="\t", skiprows=6, encoding="utf-16")

        # Llenar los valores NaN con ceros
        datos.fillna("NULL", inplace=True)

        # Obtener la fecha desde el archivo
        fecha = obtener_fecha(os.path.join(carpeta_descargas, archivo))
        #print("Fecha leída desde el archivo:")
        #print(fecha)

        # Convertir la fecha al formato adecuado
        fecha_formateada = convertir_fecha_formato(fecha)

        try:
            config["port"] = puerto_bd  # Actualizar el puerto en la configuración
            conexion = mysql.connector.connect(**config)
            cursor = conexion.cursor()

            # Crear la cadena de columnas para la inserción
            columnas = list(datos.columns)
            columnas = [
            "user_name", "total_counter", "total_large_size_counter", "no_of_originals_counter", "no_of_prints_counter", "duplex_print_counter", "total_no_pages_output", "copy_total_total", "copy_total_full_color", "copy_total_black", "copy_total_2color", "copy_total_single_color", "copy_large_size_total", "copy_large_size_full_color", "copy_large_size_black", "copy_large_size_2color", "copy_large_size_single_color", "printer_total_total","printer_total_full_color","printer_total_black","printer_total_2color","printer_large_size_total","printer_large_size_full_color","printer_large_size_black","printer_large_size_2color","color_total_full_color","color_total_black","color_total_2color","color_total_single_color","color_large_size_full_color","color_large_size_black","color_large_size_2color","color_large_size_single_color","scan_total_print_full_color","scan_total_print_black","scan_total_scans","scan_total_fax_tx","scan_large_size_print_full_color","scan_large_size_print_black","scan_large_size_scans","fecha_contador"
            ]

            columnas_str = ', '.join(columnas)

            # Insertar los datos en la tabla MySQL
            for _, fila in datos.iterrows():
                valores = tuple(fila)
                placeholders = ', '.join(['%s'] * len(valores))
                sql = f"INSERT INTO `{nombre_tabla}` ({columnas_str}) VALUES ({placeholders});"
                cursor.execute(sql, valores)

            # Actualizar la fecha en la tabla MySQL si es válida
            if fecha_formateada:
                sql = f"UPDATE `{nombre_tabla}` SET fecha_contador = %s WHERE fecha_contador = 'NULL'"
                values = (fecha_formateada,)
                cursor.execute(sql, values)

            conexion.commit()
            mover_archivo(nombre_archivo)


        except mysql.connector.Error as error:
            mensaje_log = f"{datetime.datetime.now()} - {nombre_archivo} Error mysql {error}"
            escribir_log(nombre_archivo_log, mensaje_log)

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()


    else:
        mensaje_log = f"{datetime.datetime.now()} - {archivo} No se encontró el archivo en Descargas {nombre_archivo}"
        escribir_log(nombre_archivo_log, mensaje_log)


def cargar_datos_t3(nombre_archivo, nombre_tabla):
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    archivo = buscar_archivo(nombre_archivo)

    if archivo:
        # Ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

        # Leer los datos desde el archivo y saltar las primeras 7 líneas
        datos = pd.read_csv(ruta_archivo, sep="\t", skiprows=6, encoding="utf-16")

        # Llenar los valores NaN con ceros
        datos.fillna("NULL", inplace=True)
        # Obtener la fecha desde el archivo
        fecha = obtener_fecha(os.path.join(carpeta_descargas, archivo))
        #print("Fecha leída desde el archivo:")
        #print(fecha)

        # Convertir la fecha al formato adecuado
        fecha_formateada = convertir_fecha_formato(fecha)

        try:
            config["port"] = puerto_bd  # Actualizar el puerto en la configuración
            conexion = mysql.connector.connect(**config)
            cursor = conexion.cursor()

            # Crear la cadena de columnas para la inserción
            columnas = list(datos.columns)
            columnas = ["user_name","total_counter ","total_large_size_counter ","no_of_originals_counter ","no_of_prints_counter ","duplex_print_counter ","total_no_pages_output ","duplex_print_rate","psc_a3 ","psc_a4 ","psc_b4 ","psc_b5 ","psc_55x85 ","psc_85x11 ","psc_85x14 ","psc_11x17 ","psc_long ","psc_other ","nin1_2in1 ","nin1_4in1 ","nin1_other ","nin1_nin1printrate ","copy_total_total ","copy_total_full_color ","copy_total_black ","copy_total_2color ","copy_total_single_color ","copy_large_size_total ","copy_large_size_full_color ","copy_large_size_black ","copy_large_size_2color ","copy_large_size_single_color ","copy_copypaper_allcolor ","copy_copypaper_full_color ","copy_copypaper_black ","copy_copypaper_monobicolor ","printer_total_total ","printer_total_full_color ","printer_total_black ","printer_total_2color ","printer_large_size_total ","printer_large_size_full_color ","printer_large_size_black ","printer_large_size_2color ","printer_printpaper_allcolor ","printer_printpaper_full_color ","printer_printpaper_black ","printer_printpaper_monobicolor ","color_total_full_color ","color_total_black ","color_total_2color ","color_total_single_color ","color_large_size_full_color ","color_large_size_black ","color_large_size_2color ","color_large_size_single_color ","scan_total_print_full_color ","scan_total_print_black ","scan_total_scans ","scan_total_fax_tx ","scan_large_size_print_full_color ","scan_large_size_print_black ","scan_large_size_scans ","scan_printpaper_allcolor ","scan_printpaper_full_color ","scan_printpaper_black ","no_of_prints_counter_fullcolor ","no_of_prints_counter_black ","no_of_prints_counter_monobiocolor ","fecha_contador"
            ]

            columnas_str = ', '.join(columnas)

            # Insertar los datos en la tabla MySQL
            for _, fila in datos.iterrows():
                valores = tuple(fila)
                placeholders = ', '.join(['%s'] * len(valores))
                sql = f"INSERT INTO `{nombre_tabla}` ({columnas_str}) VALUES ({placeholders});"
                cursor.execute(sql, valores)

            # Actualizar la fecha en la tabla MySQL si es válida
            if fecha_formateada:
                sql = f"UPDATE `{nombre_tabla}` SET fecha_contador = %s WHERE fecha_contador = 'NULL'"
                values = (fecha_formateada,)
                cursor.execute(sql, values)

            conexion.commit()
            mover_archivo(nombre_archivo)
            
        except mysql.connector.Error as error:
            mensaje_log = f"{datetime.datetime.now()} - {nombre_archivo} Error mysql {error}"
            escribir_log(nombre_archivo_log, mensaje_log)

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()


    else:
        mensaje_log = f"{datetime.datetime.now()} - {archivo} No se encontró el archivo en Descargas {nombre_archivo}"
        escribir_log(nombre_archivo_log, mensaje_log)


# Guarda la referencia al stdout original
stdout_original = sys.stdout

# Nombre del archivo de log con la fecha en el nombre
#nombre_archivo_log = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
nombre_archivo_log = "log.txt"

patron_fecha = r"\d{8}"  # Busca 8 dígitos numéricos consecutivos.
carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")


url = "10.70.10.50"
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
patron_fecha = r"363_A1UE011016227_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.51"
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
patron_fecha = r"363_A1UE011104367_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.52"
t_ingreso = 3
t_import_export = 16
t_contador = 28
t_salir = 23
patron_fecha = r"364e_A61F011024714_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.54"
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 26
patron_fecha = r"CAMBIAR\d{8}"  # Busca 8 dígitos numéricos consecutivos.
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.55"
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
patron_fecha = r"552_A2WV011008573_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.56"
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
patron_fecha = r"223_A1UG011006937_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.60"
t_ingreso = 3
t_import_export = 16
t_contador = 28
t_salir = 23
patron_fecha = r"C554e_A5AY011013622_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.69"
t_ingreso = 3
t_import_export = 14
t_contador = 31
t_salir = 26
patron_fecha = r"363_A1UE011015445_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.70"
t_ingreso = 4
t_import_export = 22
t_contador = 32
t_salir = 28
ingresar(url,t_ingreso)
verificar_ingreso(url, t_import_export, t_contador, t_salir)

url = "10.70.10.71"
t_ingreso = 3
t_import_export = 14
t_contador = 28
t_salir = 23
ingresar(url,t_ingreso)

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
cargar_datos_t3(nombre_archivo,nombre_tabla)

nombre_archivo = "C554e_A5AY011013622_UC_"
nombre_tabla = "C554e_A5AY011013622"
cargar_datos_t2(nombre_archivo,nombre_tabla)

mensaje_log = f"{datetime.datetime.now()} - EXPORTACION TERMINADA ***************************"
escribir_log(nombre_archivo_log,mensaje_log)