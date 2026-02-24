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
    lower = np.array([90, 50, 50])
    upper = np.array([130, 255, 255])

    # rojo “bajo” (cerca de 0º)
    lower1 = np.array([  0, 100, 100])
    upper1 = np.array([ 10, 255, 255])
    # rojo “alto” (cerca de 180º)
    lower2 = np.array([160, 100, 100])
    upper2 = np.array([179, 255, 255])
    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    #mask  = cv2.bitwise_or(mask1, mask2)

    # rango aproximado para amarillo y verde
    #lower_A = np.array([20, 100, 100])
    #upper_A = np.array([30, 255, 255])
    lower_A = np.array([40, 50, 50])
    upper_A = np.array([90, 255, 255])

    #Crear una mascara con los parametros de color en azul
    #mask = cv2.inRange(hsv, lower, upper)
    

    #Crear una mascara con los parametros de color en amarillo
    mask_A = cv2.inRange(hsv, lower_A, upper_A)
    
    
    #Aplicar la mascara al marco original para obtener solo las partes del color detectado
    result = cv2.bitwise_and(frame, frame, mask=mask_A)   


    if not ret:
        break  
    
    frame = cv2.flip(frame, 1)

    cv2.imshow('Webcam', frame)
    cv2.imshow('Webcam HSV', hsv)
    cv2.imshow('Mascara', mask_A)
    cv2.imshow('Color Detectado', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
webcam.release()
cv2.destroyAllWindows()
