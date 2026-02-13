# Introducción a la Inteligencia Artificial.
La Inteligencia Artificial (IA) es, en esencia, el intento de crear máquinas que puedan realizar tareas que normalmente requieren de la inteligencia humana 🧠. Esto incluye cosas como aprender de la experiencia, reconocer patrones en imágenes o entender el lenguaje natural.

## Los 3 Pilares del Funcionamiento
Entrada de Datos (Inputs) 📥: La IA necesita ejemplos. Para que aprenda a reconocer un gato, necesita ver miles de fotos de gatos y de cosas que no son gatos.

Algoritmos y Modelos ⚙️: Es el "cerebro" matemático. El algoritmo analiza los datos buscando características comunes (como la forma de las orejas o los bigotes). Al final de este entrenamiento, se crea un modelo.

Predicción o Decisión (Outputs) 📤: Una vez entrenado, si le muestras una foto nueva, el modelo calcula la probabilidad de que sea un gato basándose en lo que aprendió antes.

## Concepto Clave: Redes Neuronales 🧠
Una de las formas más avanzadas de IA se inspira en la biología: las Redes Neuronales Artificiales. Son capas de nodos (neuronas matemáticas) que procesan la información. Cada capa identifica detalles más complejos: la primera puede ver líneas, la segunda formas geométricas y la última el objeto completo.

### Link de visualizador de modelos: 
https://bbycroft.net/llm

### Simulador de red neuronal
https://playground.tensorflow.org/#activation=tanh&batchSize=9&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=5&networkShape=3,4,4,6,2&seed=0.54269&showTestData=false&discretize=false&percTrainData=70&x=true&y=true&xTimesY=false&xSquared=true&ySquared=true&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false


### El entrenamiento 
Es el proceso mediante el cual una IA pasa de ser un conjunto de fórmulas vacías a un sistema capaz de reconocer patrones. Es muy parecido a cómo un estudiante practica con ejercicios antes de un examen. 📝

Para entenderlo, imaginemos que queremos entrenar a una IA para que distinga entre fotos de perros 🐶 y gatos 🐱. El proceso sigue estos pasos:

### El Ciclo de Aprendizaje 🔄
La Predicción Inicial: Al principio, la IA no sabe nada. Si le muestras una foto, lanzará una "moneda al aire" y dirá "es un perro" al azar. 🎲

La Función de Pérdida (El Error) 📉: Aquí es donde ocurre la magia. El sistema compara su respuesta con la etiqueta real de la foto. Si falló, calcula qué tan lejos estuvo de la respuesta correcta. A este error lo llamamos "pérdida".

### El Optimizador (La Corrección) 🛠️: 
Una vez que la IA sabe que se equivocó, el algoritmo de optimización ajusta las conexiones internas (llamadas pesos) del modelo. Es como si la IA se dijera a sí misma: "Ah, las orejas puntiagudas suelen ser de gato, le daré más importancia a ese detalle la próxima vez".

### Repetición: 
Este ciclo se repite miles o millones de veces con diferentes ejemplos hasta que el error es mínimo.

# Conceptos Clave
Reinforcement Learning with Human Feedback
