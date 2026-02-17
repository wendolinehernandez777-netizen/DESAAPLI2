import cv2
import numpy as np

# Función auxiliar para dibujar líneas discontinuas
def draw_dashed_line(img, p1, p2, color, thickness=2, dash_len=15, gap_len=10):
    x1, y1 = p1
    x2, y2 = p2
    
    # Calcular la distancia total y el vector de dirección
    dist = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if dist == 0: return
    
    dx = (x2 - x1) / dist
    dy = (y2 - y1) / dist
    
    current_dist = 0
    while current_dist < dist:
        # Calcular inicio y fin del segmento actual
        start_x = int(x1 + current_dist * dx)
        start_y = int(y1 + current_dist * dy)
        
        end_dist = min(current_dist + dash_len, dist)
        end_x = int(x1 + end_dist * dx)
        end_y = int(y1 + end_dist * dy)
        
        # Dibujar el segmento
        cv2.line(img, (start_x, start_y), (end_x, end_y), color, thickness)
        
        # Avanzar la distancia del segmento + el espacio
        current_dist += dash_len + gap_len

def dibujar_guias_estilo_nuevo(frame):
    alto, ancho = frame.shape[:2]
    centro_x = ancho // 2
    
    # --- Definición de la Perspectiva y Zonas ---
    punto_fuga_y = int(alto * 0.35) # Punto más alto (verde)
    base_y = int(alto * 0.95)       # Punto más bajo (rojo)
    
    ancho_base = int(ancho * 0.9)
    ancho_top = int(ancho * 0.25)
    
    # Definir límites verticales para los cambios de color
    y_limite_rojo = int(alto * 0.75)    # Fin de la zona roja
    y_limite_amarillo = int(alto * 0.55) # Fin de la zona amarilla
    
    # Puntos principales (inicio y fin de las líneas laterales)
    p_base_izq = np.array([centro_x - ancho_base // 2, base_y])
    p_top_izq = np.array([centro_x - ancho_top // 2, punto_fuga_y])
    p_base_der = np.array([centro_x + ancho_base // 2, base_y])
    p_top_der = np.array([centro_x + ancho_top // 2, punto_fuga_y])
    
    # Colores (B, G, R)
    verde = (0, 255, 0)
    amarillo = (0, 255, 255)
    rojo = (0, 0, 255)
    grosor = 4
    
    # Función para encontrar puntos intermedios en las líneas laterales
    def get_interp_point(p_start, p_end, target_y):
        t = (target_y - p_start[1]) / (p_end[1] - p_start[1])
        x = int(p_start[0] + (p_end[0] - p_start[0]) * t)
        return np.array([x, target_y])

    # Calcular puntos de transición de color
    p_rojo_izq = get_interp_point(p_base_izq, p_top_izq, y_limite_rojo)
    p_amarillo_izq = get_interp_point(p_base_izq, p_top_izq, y_limite_amarillo)
    
    p_rojo_der = get_interp_point(p_base_der, p_top_der, y_limite_rojo)
    p_amarillo_der = get_interp_point(p_base_der, p_top_der, y_limite_amarillo)
    
    # --- Dibujado de las Guías ---
    
    # 1. Líneas Laterales (segmentadas por color)
    # Izquierda
    draw_dashed_line(frame, tuple(p_base_izq), tuple(p_rojo_izq), rojo, grosor)
    draw_dashed_line(frame, tuple(p_rojo_izq), tuple(p_amarillo_izq), amarillo, grosor)
    draw_dashed_line(frame, tuple(p_amarillo_izq), tuple(p_top_izq), verde, grosor)
    # Derecha
    draw_dashed_line(frame, tuple(p_base_der), tuple(p_rojo_der), rojo, grosor)
    draw_dashed_line(frame, tuple(p_rojo_der), tuple(p_amarillo_der), amarillo, grosor)
    draw_dashed_line(frame, tuple(p_amarillo_der), tuple(p_top_der), verde, grosor)

    # 2. Líneas Horizontales (en los puntos de transición)
    # Base Roja
    draw_dashed_line(frame, tuple(p_base_izq), tuple(p_base_der), rojo, grosor)
    # Límite Rojo/Amarillo
    draw_dashed_line(frame, tuple(p_rojo_izq), tuple(p_rojo_der), rojo, grosor)
    # Límite Amarillo/Verde
    draw_dashed_line(frame, tuple(p_amarillo_izq), tuple(p_amarillo_der), amarillo, grosor)
    # Tope Verde (un poco más abajo del punto de fuga para que se vea)
    p_top_final_izq = get_interp_point(p_base_izq, p_top_izq, punto_fuga_y + 15)
    p_top_final_der = get_interp_point(p_base_der, p_top_der, punto_fuga_y + 15)
    draw_dashed_line(frame, tuple(p_top_final_izq), tuple(p_top_final_der), verde, grosor)

    # Texto de seguridad (siempre es bueno mantenerlo)
    texto = "Verificar seguridad del entorno"
    fuente = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, texto, (ancho//2 - 180, 50), fuente, 0.7, (255,255,255), 2)

def main():
    # Iniciar captura de video
    cap = cv2.VideoCapture(0) # Usa 0 para webcam, o ruta de archivo de video
    
    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara.")
        return

    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # Efecto espejo
        frame = cv2.flip(frame, 1)
        
        # Dibujar las nuevas guías
        dibujar_guias_estilo_nuevo(frame)
        
        cv2.imshow('Camara de Reversa - Estilo Nuevo', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
