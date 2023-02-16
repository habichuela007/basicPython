import cv2

# Cargar la cascada frontal de Haar para la detección de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Iniciar la captura de video desde la cámara frontal de la computadora
cap = cv2.VideoCapture(0)

while True:
    # Leer un cuadro de video
    ret, frame = cap.read()

    # Convertir el cuadro a escala de grises para un mejor rendimiento
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el cuadro utilizando la cascada frontal de Haar
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Dibujar un rectángulo alrededor de cada rostro detectado en el cuadro
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Mostrar el cuadro resultante con los rostros detectados
    cv2.imshow('Reconocimiento facial',frame)

    # Esperar a que el usuario presione la tecla 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar la ventana
cap.release()
cv2.destroyAllWindows()