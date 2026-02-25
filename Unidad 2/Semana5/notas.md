# Documentación: Detector de Colores en Tiempo Real

## 📋 Índice
1. [¿Qué hace el programa?](#qué-hace-el-programa)
2. [Cómo se hizo](#cómo-se-hizo)
3. [Librerías utilizadas](#librerías-utilizadas)
4. [Funciones principales](#funciones-principales)
5. [Parámetros HSV explicados](#parámetros-hsv-explicados)
6. [Flujo del programa](#flujo-del-programa)
7. [Cátedra: Conceptos clave](#cátedra-conceptos-clave)

---

## 🎯 ¿Qué hace el programa?

Este programa captura video en tiempo real desde la cámara web del dispositivo y detecta **4 colores específicos** (rojo, azul, verde y amarillo). Para cada color detectado:

- Crea una **máscara binaria** que identifica píxeles del color objetivo
- Aplica la máscara al frame original para aislar solo aquellos píxeles
- Muestra el resultado en una ventana separada

**Resultado final:** 5 ventanas simultáneas mostrando:
1. Frame original sin procesar
2. Píxeles rojos detectados (fondo negro, píxeles rojos visibles)
3. Píxeles azules detectados
4. Píxeles verdes detectados
5. Píxeles amarillos detectados

---

## 🔨 Cómo se hizo

### Paso 1: Importación de librerías
```python
import cv2
import numpy as np
```

### Paso 2: Inicializar captura de video
```python
webcam = cv2.VideoCapture(0)
```
Abre la cámara predeterminada (índice 0).

### Paso 3: Bucle principal
```python
while True:
    ret, frame = webcam.read()
```
Lee frame por frame de la cámara en un bucle infinito.

### Paso 4: Conversión del espacio de color
```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```
Convierte el frame de BGR a HSV (explicado en detalle más adelante).

### Paso 5: Detección de cada color
Para cada color, se realizan 3 pasos:
- **Definir rango HSV**: Establecer los valores `lower` y `upper` para el color
- **Crear máscara**: Usar `cv2.inRange()` para identificar píxeles dentro del rango
- **Aplicar máscara**: Usar `cv2.bitwise_and()` para aplicarla al frame original

### Paso 6: Mostrar resultados
```python
cv2.imshow('nombre_ventana', imagen)
```
Muestra cada resultado en una ventana separada.

### Paso 7: Control de salida
```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```
Presionar 'q' cierra el programa.

### Paso 8: Liberar recursos
```python
webcam.release()
cv2.destroyAllWindows()
```

---

## 📚 Librerías utilizadas

### **OpenCV (cv2)**
Es una librería de visión por computadora muy potente.

| Función | Parámetros | Qué hace |
|---------|-----------|----------|
| `VideoCapture(índice)` | `0` = cámara predeterminada | Abre un dispositivo de video |
| `read()` | Ninguno | Lee un frame. Retorna `(ret, frame)` |
| `cvtColor(src, código)` | `frame`, `COLOR_BGR2HSV` | Convierte entre espacios de color |
| `inRange(src, lower, upper)` | `hsv`, valores mín/máx | Crea máscara binaria |
| `bitwise_and(src1, src2, mask)` | `frame`, `frame`, `mask` | Aplica máscara lógicamente |
| `imshow(nombre, imagen)` | `'Nombre'`, imagen | Muestra ventana |
| `waitKey(ms)` | `1` = 1 milisegundo | Espera tecla presionada |
| `release()` | Ninguno | Libera cámara |
| `destroyAllWindows()` | Ninguno | Cierra todas las ventanas |

### **NumPy (np)**
Librería para operaciones con arrays numéricos.

```python
np.array([H, S, V])
```
Crea un array con los valores de Hue, Saturation y Value para definir un color en HSV.

---

## 🔧 Funciones principales

### 1. `cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`

**¿Por qué convertir a HSV?**
- BGR es cómo captura OpenCV (Azul, Verde, Rojo)
- HSV es más intuitivo para detectar colores (Hue, Saturation, Value)
- HSV es **menos sensible a cambios de iluminación**

**Retorna:** El mismo frame pero en espacio HSV

---

### 2. `cv2.inRange(hsv, lower, upper)`

**Parámetros:**
- `hsv`: El frame convertido a HSV
- `lower`: Array [H_min, S_min, V_min]
- `upper`: Array [H_max, S_max, V_max]

**¿Qué hace?**
Crea una imagen binaria (blanco y negro) donde:
- **255 (blanco)**: píxeles dentro del rango
- **0 (negro)**: píxeles fuera del rango

**Retorna:** Una máscara binaria

---

### 3. `cv2.bitwise_and(src1, src2, mask=mask)`

**Parámetros:**
- `src1`: Imagen 1 (en este caso, frame)
- `src2`: Imagen 2 (en este caso, frame nuevamente)
- `mask`: La máscara a aplicar

**¿Qué hace?**
Aplica la máscara al frame, dejando visible solo donde la máscara es 255.

**Retorna:** El frame con solo los píxeles del color detectado

---

### 4. `cv2.bitwise_or(mask1, mask2)`

Se usa **solo para el rojo** porque:
- El rojo está en AMBOS extremos del rango HSV (0 y 179)
- Se crean 2 máscaras separadas y se unen con OR lógico

```python
mask_red1 = cv2.inRange(hsv, [0, 100, 100], [10, 255, 255])    # Rojo bajo (cerca de 0)
mask_red2 = cv2.inRange(hsv, [160, 100, 100], [179, 255, 255]) # Rojo alto (cerca de 179)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)                 # Combina ambas
```

---

## 🎨 Parámetros HSV explicados

### ¿Qué es HSV?

| Componente | Rango | Significado |
|-----------|-------|------------|
| **H (Hue)** | 0-179 | El **color puro**: 0=Rojo, 30=Amarillo, 60=Verde, 90=Cian, 120=Azul, 150=Magenta |
| **S (Saturation)** | 0-255 | **Intensidad del color**: 0=Gris puro, 255=Color saturado |
| **V (Value)** | 0-255 | **Brillo**: 0=Negro, 255=Máximo brillo |

### Rango para cada color

#### 🔴 ROJO
```python
# Rojo bajo (cercano a 0°)
lower1 = np.array([0, 100, 100])
upper1 = np.array([10, 255, 255])

# Rojo alto (cercano a 180°)
lower2 = np.array([160, 100, 100])
upper2 = np.array([179, 255, 255])

mask_red = cv2.bitwise_or(
    cv2.inRange(hsv, lower1, upper1),
    cv2.inRange(hsv, lower2, upper2)
)
```
**¿Por qué dos rangos?** Porque en la rueda HSV, el rojo está "dividido" entre 0 y 179.

---

#### 🔵 AZUL
```python
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
```
**H:** 90-130 (el rango del azul)
**S:** 50+ (necesita saturación)
**V:** 50+ (necesita brillo mínimo)

---

#### 💚 VERDE
```python
lower_green = np.array([40, 50, 50])
upper_green = np.array([90, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)
```
**H:** 40-90 (desde amarillo-verde hasta verde-cian)
**S:** 50+ (saturación mínima)
**V:** 50+ (brillo mínimo)

---

#### 💛 AMARILLO
```python
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
```
**H:** 20-30 (entre rojo y verde)
**S:** 100+ (debe ser muy saturado)
**V:** 100+ (debe ser bastante brillante)

---

## 📊 Flujo del programa

```
START
  ↓
Abrir cámara (VideoCapture)
  ↓
┌─ BUCLE INFINITO ─────────────────────────┐
│                                          │
│ 1. Leer frame de cámara                 │
│                                          │
│ 2. Convertir BGR → HSV                  │
│                                          │
│ 3. Para cada color (R, A, V, Am):      │
│    ├─ Crear máscara con inRange        │
│    └─ Aplicar máscara con bitwise_and  │
│                                          │
│ 4. Mostrar 5 ventanas:                 │
│    ├─ Frame Original                   │
│    ├─ Rojo Detectado                   │
│    ├─ Azul Detectado                   │
│    ├─ Verde Detectado                  │
│    └─ Amarillo Detectado               │
│                                          │
│ 5. ¿Presionó 'q'?                      │
│    ├─ SÍ → Salir del bucle             │
│    └─ NO → Continuar                   │
│                                          │
└──────────────────────────────────────────┘
  ↓
Liberar cámara
  ↓
Cerrar ventanas
  ↓
END
```

---

## 🎓 Cátedra: Conceptos clave

### 1. **¿Por qué OpenCV es mejor que capturar directamente de PIL o matplotlib?**

OpenCV está optimizado para **procesamiento de video en tiempo real**. Puede:
- Leer frames a alta velocidad
- Manejar múltiples operaciones simultáneamente
- Procesar miles de píxeles sin lag

### 2. **¿Por qué HSV y no RGB/BGR?**

Imagina que quieres detectar un objeto rojo en diferentes luces:

| Espacio | Con luz brillante | Con luz débil | Problema |
|---------|------------------|---------------|----------|
| BGR | (255, 0, 0) | (100, 0, 0) | **Valores diferentes** |
| HSV | (0, 255, 255) | (0, 255, 100) | **Hue igual, solo cambia Value** |

En HSV, el **Hue nunca cambia** con la iluminación. Solo cambia Saturation y Value.

---

### 3. **¿Cómo elegir los valores lower y upper correctamente?**

**Método manual (prueba y error):**
```python
# Probar con valores más amplios primero
lower = np.array([0, 50, 50])          # Menos restricción
upper = np.array([10, 255, 255])       # Más permisivo

# Si detecta demasiado ruido, restringir:
lower = np.array([0, 150, 100])        # Más restricción
upper = np.array([10, 255, 255])
```

**Método profesional:** Usar trackbars interactivos
```python
cv2.createTrackbar('H_min', 'window', 0, 179, lambda x: None)
# ... esto permite ajustar en tiempo real
```

---

### 4. **El concepto de la máscara binaria**

Una máscara es como un **molde transparente**:

```
Frame Original:     Máscara:           Resultado:
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ RGB RGB RGB │    │ 255 0 255   │    │ RGB 0 RGB   │
│ RGB RGB RGB │ ×  │ 0 255 0     │  = │ 0 RGB 0     │
│ RGB RGB RGB │    │ 255 0 255   │    │ RGB 0 RGB   │
└─────────────┘    └─────────────┘    └─────────────┘
                   (255=visible)      (0=invisible)
                   (0=invisible)
```

---

### 5. **¿Por qué se usa bitwise_and en lugar de multiplicación simple?**

Porque `bitwise_and` **a nivel de hardware** es mucho más rápido:

```python
# Lento (elemento por elemento)
resultado = frame * (mask / 255.0)

# Rápido (operación lógica a nivel de bits)
resultado = cv2.bitwise_and(frame, frame, mask=mask)
```

Para video en tiempo real, esa diferencia importa mucho.

---

### 6. **Casos de uso en el mundo real**

Este programa es la base para:

- **Robótica**: Detectar objetos por color (balón en un robot futbolista)
- **Visión médica**: Identificar áreas inflamadas en imágenes térmicas
- **Manufactura**: Control de calidad (detectar componentes de color específico)
- **Videovigilancia**: Tracking de personas con ropa de color particular
- **Realidad aumentada**: Detección de marcadores de color

---

### 7. **Mejoras posibles**

Para hacer el programa más robusto:

```python
# 1. Usar blur para reducir ruido
frame_blur = cv2.GaussianBlur(hsv, (5, 5), 0)

# 2. Aplicar erosión y dilatación para limpiar la máscara
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask_clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# 3. Encontrar contornos de objetos detectados
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 4. Dibujar rectángulos alrededor de objetos
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if cv2.contourArea(contour) > 500:  # Filtrar por área mínima
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
```

---

## 📝 Resumen

| Concepto | Función OpenCV | Parámetro clave | Propósito |
|----------|----------------|-----------------|-----------|
| Captura | `VideoCapture()` | Índice cámara | Obtener video |
| Conversión | `cvtColor()` | `COLOR_BGR2HSV` | Cambiar espacio de color |
| Detección | `inRange()` | `lower`, `upper` | Crear máscara |
| Aplicación | `bitwise_and()` | `mask` | Aislar píxeles |
| Visualización | `imshow()` | Nombre ventana | Mostrar resultado |

---

**Fecha de elaboración:** Febrero 2026
**Nivel:** Introducción a Inteligencia Artificial - Procesamiento de Imágenes
**Objetivo:** Comprender detección de colores en tiempo real usando HSV
