# EntrevistaAXOLOTLCODE
Visión por computadora en tiempo real con YOLOv8n para la clasificacion de: Objetos, Personas y Fondo

````markdown
 Clasificador de Objetos en Tiempo Real con YOLOv8n

Este proyecto fue desarrollado como una prueba técnica para la empresa **AXOLOTLCODE**, con el objetivo de demostrar habilidades en visión por computadora en tiempo real utilizando modelos de detección optimizados. El sistema identifica si frente a la cámara hay una persona, un objeto o si no hay ninguna detección (fondo).

Se utilizó el modelo **YOLOv8n** (versión nano) por su eficiencia en tareas en tiempo real, balanceando velocidad y precisión. Todo el código está implementado en un único script para mantenerlo compacto, entendible y portátil.

---

##**Código Fuente**

Archivo principal:  
**VisionArtificial.py**

Repositorio:  
[https://github.com/Lugtz/AXOLOTLCODE](https://github.com/Lugtz/AXOLOTLCODE)

---

##** Requisitos**

- **Python 3.12**
- Sistema operativo: Windows (probado en Windows 10)
- Cámara conectada y operativa

---

## **Instalación**

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Lugtz/AXOLOTLCODE.git
   cd VisionArtificial.py
````

2. (Opcional) Crear y activar entorno virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución

Para ejecutar el clasificador:

```bash
python VisionArtificial.py
```

Presiona la tecla `q` para cerrar la aplicación.

---

## Dependencias

* `ultralytics >= 8.0.0`
* `opencv-python`
* `numpy`

Estas dependencias están especificadas en el archivo `requirements.txt`.

---

## Funcionamiento

* Se accede a la cámara y se procesa cada frame en tiempo real.
* El modelo **YOLOv8n** detecta los objetos presentes.
* Si la clase detectada es `'person'`, se etiqueta como **PERSONA**.
* Si se detecta cualquier otra clase, se etiqueta como **OBJETO**.
* Si no hay detecciones visibles, se muestra **FONDO / INDEFINIDO**.

---

## Capturas del Funcionamiento

Se encuentran en la carpeta:

```
"EntrevistaP\media"
```


## Documentación Técnica

### Arquitectura del Sistema

1. Captura de video mediante OpenCV
2. Detección en tiempo real usando YOLOv8n
3. Clasificación del objeto detectado
4. Visualización con etiquetas personalizadas sobre el video

### Algoritmos

* Modelo preentrenado YOLOv8n (`yolov8n.pt`)
* Uso de clases del dataset COCO:

  * `person` = Persona
  * Cualquier otra = Objeto
  * Sin detección = Fondo / Indefinido

---

## Decisiones de Diseño

* Se usó YOLOv8n por su velocidad de inferencia en entornos sin GPU.
* Toda la lógica fue encapsulada en un solo script (`VisionArtificial.py`).
* Se usó la cámara externa (índice 1). Si se requiere usar cámara interna, se puede modificar por `0`.
* Se utilizó `cv2.CAP_DSHOW` para asegurar compatibilidad con Windows.

---

## Posibles Errores y Soluciones

Error: No se pudo acceder a la cámara.
Posible causa: el índice de la cámara es incorrecto o está en uso por otra aplicación.
Solución: Cambiar cv2.VideoCapture(1) por cv2.VideoCapture(0) para utilizar la cámara interna o probar otro índice disponible.

ModuleNotFoundError: No module named 'ultralytics'
Posible causa: la dependencia ultralytics no está instalada en el entorno actual.
Solución: Ejecutar pip install -r requirements.txt para instalar todas las dependencias necesarias.

La ventana de video se congela o no se ve la imagen.
Posible causa: la cámara está bloqueada por otra aplicación o hay un problema con el backend de OpenCV.
Solución: Asegúrate de usar cv2.CAP_DSHOW en la línea cv2.VideoCapture() si estás trabajando en Windows.

Error de compatibilidad con Python.
Posible causa: se está usando una versión de Python no compatible.
Solución: Este proyecto fue desarrollado con Python 3.12, por lo tanto, se recomienda utilizar esa misma versión para evitar errores.


## Recomendaciones Finales

* Confirmar que la cámara funciona antes de ejecutar el script.
* Verificar el entorno virtual y dependencias antes de la entrevista.
* Asegurar iluminación suficiente para que YOLOv8 realice detecciones precisas.
* Capturar screenshots reales para incluir en el repositorio como evidencia visual.
* Se sugiere probar en distintos entornos para comprobar robustez.

---

Este proyecto refleja mi enfoque técnico y práctico para resolver problemas reales con inteligencia artificial, específicamente en visión por computadora. Fue desarrollado como parte de una entrevista técnica y demuestra habilidades en integración de modelos, análisis visual y optimización para tiempo real.

````
