import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    # Obtener las dimensiones del marco
    height = int(webcam.get(4))
    width = int(webcam.get(3))
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Parametro de color a detectar, en este caso el azul
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #Crear una mascara con los parametros de color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    #Aplicar la mascara al marco original para obtener solo las partes del color detectado
    result = cv2.bitwise_and(frame, frame, mask=mask)   


    if not ret:
        break  
    
    frame = cv2.flip(frame, 1)

    cv2.imshow('Webcam', frame)
    cv2.imshow('Webcam HSV', hsv)
    cv2.imshow('Mascara', mask)
    cv2.imshow('Color Detectado', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
webcam.release()
cv2.destroyAllWindows()
