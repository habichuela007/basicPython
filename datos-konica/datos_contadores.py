import webbrowser
import time
import pywinauto.keyboard as keyboard
from pywinauto import Desktop
import os
import subprocess
import re
import sys
import datetime


def ingresar(url,t_ingreso):
    webbrowser.open(url, new=2)
    # Cambia a modo administrador
    time.sleep(15)
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
    keyboard.send_keys("12345678")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    time.sleep(10)


def verificar_ingreso(url, t_import_export, t_contador, t_salir):
    # Obtener todos los elementos de la ventana en el escritorio
    time.sleep(1)
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
        mensaje_log = f"{url} No se pudo ingresar - {datetime.datetime.now()}"
        escribir_log(nombre_archivo_log,mensaje_log)
        time.sleep(2)        


def descargar_contador(t_import_export,t_contador,t_salir):
    # IR IMPORTAR/EXPORTAR
    time.sleep(4)
    for _ in range (t_import_export):
        keyboard.send_keys("{TAB}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")      
    # SELECCCIONAR CONTADOR DE USUARIO
    time.sleep(15)
    for _ in range (t_contador):
        keyboard.send_keys("{TAB}")  
    time.sleep(1)
    keyboard.send_keys("{DOWN}")                       
    time.sleep(1)
    keyboard.send_keys("{TAB}")
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       

    # EXPORTAR
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

    # INGRESA CONTRASEÑA
    time.sleep(10)
    keyboard.send_keys("{TAB}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       

    time.sleep(8)
    keyboard.send_keys("{TAB 4}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       

    time.sleep(4)
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
        print(f"El archivo {archivo_descargado} se descargó exitosamente.")
    else:
        mensaje_log = f"{url} Archivo No encontrado - {datetime.datetime.now()}"
        escribir_log(nombre_archivo_log,mensaje_log)


def escribir_log(nombre_archivo_log,mensaje_log):
    # Obtener la ruta completa del archivo de log
    ruta_archivo_log = os.path.join(os.path.expanduser("~"), "Downloads", nombre_archivo_log)

    # Abre el archivo de log en modo de apendizaje (si no existe, se creará)
    with open(ruta_archivo_log, "a") as archivo_log:
        # Redirige la salida estándar al archivo de log
        sys.stdout = archivo_log
        print(mensaje_log)
        sys.stdout = sys.__stdout__  # Restaura la salida estándar original


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