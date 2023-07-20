import webbrowser
import time
import pywinauto.keyboard as keyboard


def descargar_contador(t_ingreso,t_import_export,t_contador,t_salir):
    # Cambia a modo administrador
    time.sleep(4)
    for _ in range (t_ingreso):
        keyboard.send_keys("{TAB}")                      
    time.sleep(1)
    keyboard.send_keys("{DOWN}")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    # INGRESA CONTRASEÑA
    time.sleep(1)
    keyboard.send_keys("{TAB 4}")                       
    time.sleep(1)
    keyboard.send_keys("12345678")                       
    time.sleep(1)
    keyboard.send_keys("{ENTER}")                       
    # IR IMPORTAR/EXPORTAR
    time.sleep(15)
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


####TIPO 1###
t_ingreso = 4
t_import_export = 21
t_contador = 31
t_salir = 26

url = "10.70.10.50"
#webbrowser.open(url, new=2)
#descargar_contador(t_ingreso,t_import_export,t_contador,t_salir)

t_salir = 27
url = "10.70.10.51"
#webbrowser.open(url, new=2)
#descargar_contador(t_ingreso,t_import_export,t_contador,t_salir)
url = "10.70.10.56"
#webbrowser.open(url, new=2)
#descargar_contador(t_ingreso,t_import_export,t_contador,t_salir)

####TIPO ####
t_ingreso = 3
t_import_export = 14
t_contador = 31
t_salir = 26

url = "10.70.10.69"
#webbrowser.open(url, new=2)
#descargar_contador(t_ingreso,t_import_export,t_contador,t_salir)


t_contador = 26
t_salir = 21
url = "10.70.10.52"
#webbrowser.open(url, new=2)
#descargar_contador(t_ingreso,t_import_export,t_contador,t_salir)


#t_ingreso = 3
t_import_export = 16
t_contador = 30
t_salir = 25

url = "10.70.10.71"
#webbrowser.open(url, new=2)
#descargar_contador(t_ingreso,t_import_export,t_contador,t_salir)

t_contador = 28
t_salir = 23
url = "10.70.10.60"
webbrowser.open(url, new=2)
descargar_contador(t_ingreso,t_import_export,t_contador,t_salir)