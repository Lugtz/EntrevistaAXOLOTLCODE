# clasificador_yolo.py
# Clasificador en tiempo real con YOLOv8n (versión compacta)
# Detecta personas, objetos y fondo usando la cámara web

from ultralytics import YOLO
import cv2

# Inicialización del modelo YOLOv8 (versión 'nano' por su eficiencia en tiempo real)
modelo = YOLO('yolov8n.pt')
CLASES_DE_INTERES = ['person']

# Apertura del dispositivo de captura (cámara externa, si utiliza camara interna cambiar el 1 por 0)
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()
# Ciclo principal: detección y visualización
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el frame desde la cámara.")
        break
    resultados = modelo(frame)[0]
    etiqueta = "FONDO / INDEFINIDO"
    for deteccion in resultados.boxes.data:
        x1, y1, x2, y2, conf, clase_id = deteccion
        nombre_clase = modelo.names[int(clase_id)]

        if nombre_clase in CLASES_DE_INTERES:
            etiqueta = "PERSONA"
        else:
            etiqueta = "OBJETO"
        # Dibujar la caja delimitadora y la etiqueta correspondiente
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)#
        cv2.putText(frame, f"{etiqueta} ({conf:.2f})",
                    (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)#
    # Si no se detectó ningún objeto, mostrar etiqueta por defecto
    if len(resultados.boxes.data) == 0:
        cv2.putText(frame, etiqueta,
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Clasificador en Tiempo Real", frame)

    # Finalizar con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar recursos
cap.release()
cv2.destroyAllWindows()