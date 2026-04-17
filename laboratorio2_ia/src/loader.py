import cv2
import os

def cargar_imagen(nombre_archivo):
    ruta = os.path.join("data", nombre_archivo)
    imagen = cv2.imread(ruta)
    if imagen is None:
        print(f"Error: No se pudo encontrar la imagen en {ruta}")
        return None
    return imagen