#Destino libra
#"C:\Program Files\Libra\Libra.exe" -url https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0
#"C:\Program Files\Libra\Libra.exe" -url https://pruebas.bioalimentar.com:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.1.0 -fs S -ww 0 -wh 0 -dpi 0

import subprocess

# Especifica la ruta del archivo ejecutable y los argumentos a pasar
archivo_ejecutable = r"C:\Program Files\Libra\Libra.exe"
argumentos = ['-url', 'https://libra.bioalimentar.com:443/forms/frmservlet?config=libra_saa', '-t', '60000', '-wlv', '12.2.1.1.0', '-fs', 'S', '-ww', '0', '-wh', '0', '-dpi', '0']

# Construye la lista con el comando y los argumentos
comando = [archivo_ejecutable] + argumentos

# Ejecuta el comando y espera a que termine
subprocess.run(comando)
