import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1) # Espejo para que sea más natural
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --- DEFINICIÓN DE RANGOS ---

    # Azul
    lower_azul = np.array([90, 50, 50])
    upper_azul = np.array([130, 255, 255])
    
    # Rojo (usa dos rangos porque el rojo está al inicio y al final del espectro HSV)
    lower_rojo1 = np.array([0, 100, 100]); upper_rojo1 = np.array([10, 255, 255])
    lower_rojo2 = np.array([160, 100, 100]); upper_rojo2 = np.array([179, 255, 255])
    
    # Amarillo
    lower_amarillo = np.array([20, 100, 100])
    upper_amarillo = np.array([30, 255, 255])
    
    # Verde
    lower_verde = np.array([40, 40, 40])
    upper_verde = np.array([80, 255, 255])

    # --- CREACIÓN DE MÁSCARAS ---
    mask_azul = cv2.inRange(hsv, lower_azul, upper_azul)
    mask_amarillo = cv2.inRange(hsv, lower_amarillo, upper_amarillo)
    mask_verde = cv2.inRange(hsv, lower_verde, upper_verde)
    # El rojo suma sus dos máscaras
    mask_rojo = cv2.add(cv2.inRange(hsv, lower_rojo1, upper_rojo1), 
                       cv2.inRange(hsv, lower_rojo2, upper_rojo2))

    # --- APLICAR MÁSCARAS (RESULTADOS) ---
    res_azul = cv2.bitwise_and(frame, frame, mask=mask_azul)
    res_rojo = cv2.bitwise_and(frame, frame, mask=mask_rojo)
    res_amarillo = cv2.bitwise_and(frame, frame, mask=mask_amarillo)
    res_verde = cv2.bitwise_and(frame, frame, mask=mask_verde)

    # --- MOSTRAR VENTANAS ---
    cv2.imshow('Original', frame)
    cv2.imshow('Deteccion ROJO', res_rojo)
    cv2.imshow('Deteccion AMARILLO', res_amarillo)
    cv2.imshow('Deteccion AZUL', res_azul)
    cv2.imshow('Deteccion VERDE', res_verde)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
webcam.release()
cv2.destroyAllWindows()