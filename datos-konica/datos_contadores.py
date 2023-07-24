import webbrowser
import time
import pywinauto.keyboard as keyboard
from pywinauto import Desktop
import os
import subprocess
import re

def ingresar(t_ingreso):
    # Cambia a modo administrador
    time.sleep(15)
    for _ in range (t_ingreso):
        keyboard.send_keys("{TAB}")                      
    time.sleep(1)
    keyboard.send_keys("{DOWN}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    # INGRESA CONTRASEÑA
    time.sleep(4)
    keyboard.send_keys("{TAB 4}")                       
    time.sleep(1)
    keyboard.send_keys("12345678")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    time.sleep(15)


def verificar_ingreso(t_import_export,t_contador,t_salir):
    # Obtener todos los elementos de la ventana en el escritorio
    time.sleep(2)
    windows = Desktop(backend="uia").windows()
    # Buscar la ventana de KONICA por título
    konica_window = None
    for window in windows:
        if window.window_text().startswith("Mantenimiento") or window.window_text().startswith("Contador"):
            konica_window = window
            #print(konica_window.window_text())
            break
    # Si se encontró la ventana, Descargar
    if konica_window:
        descargar_contador(t_import_export,t_contador,t_salir)
        time.sleep(1)
    else:
        print(url,"No se pudo ingresar")
        time.sleep(1)


def descargar_contador(t_import_export,t_contador,t_salir):
    # IR IMPORTAR/EXPORTAR
    time.sleep(2)
    for _ in range (t_import_export):
        keyboard.send_keys("{TAB}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")      
    # SELECCCIONAR CONTADOR DE USUARIO
    time.sleep(12)
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
        print("No se pudo encontrar el archivo descargado.")


patron_fecha = r"\d{8}"  # Busca 8 dígitos numéricos consecutivos.
carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

url = "10.70.10.50"
webbrowser.open(url, new=2)
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.51"
webbrowser.open(url, new=2)
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.52"
webbrowser.open(url, new=2)
t_ingreso = 3
t_import_export = 16
t_contador = 28
t_salir = 23
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.54"
webbrowser.open(url, new=2)
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 26
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.55"
webbrowser.open(url, new=2)
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)
patron_fecha = r"552_A2WV011008573_UC_\d{8}"  # Busca 8 dígitos numéricos consecutivos.
verificar_descarga(patron_fecha,carpeta_descargas)

url = "10.70.10.56"
webbrowser.open(url, new=2)
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 27
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.60"
webbrowser.open(url, new=2)
t_ingreso = 3
t_import_export = 16
t_contador = 28
t_salir = 23
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.69"
webbrowser.open(url, new=2)
t_ingreso = 3
t_import_export = 14
t_contador = 31
t_salir = 26
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.70"
webbrowser.open(url, new=2)
t_ingreso = 4
t_import_export = 22
t_contador = 32
t_salir = 28
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)

url = "10.70.10.71"
webbrowser.open(url, new=2)
t_ingreso = 3
t_import_export = 14
t_contador = 28
t_salir = 23
ingresar(t_ingreso)
verificar_ingreso(t_import_export,t_contador,t_salir)