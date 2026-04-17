import cv2

def convertir_a_grises(imagen):
    return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

def ajustar_brillo(imagen, valor):
    # valor > 0 aumenta brillo, valor < 0 lo disminuye
    return cv2.convertScaleAbs(imagen, alpha=1, beta=valor)