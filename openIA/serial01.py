import serial

# Configurar el puerto serial
ser = serial.Serial('COM3', 2400, timeout=1)

# Esperar a que se abra el puerto serial
ser.isOpen()

# Enviar comandos seriales
ser.write(b'AT\r\n')  # Envía el comando "AT"
response = ser.readline()  # Espera la respuesta del dispositivo
print(response)

ser.write(b'AT+MODE=1\r\n')  # Envía el comando "AT+MODE=1"
response = ser.readline()  # Espera la respuesta del dispositivo
print(response)

# Cerrar el puerto serial
ser.close()