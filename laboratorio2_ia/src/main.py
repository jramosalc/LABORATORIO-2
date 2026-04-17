from loader import cargar_imagen
from transform import convertir_a_grises, ajustar_brillo
import cv2

def ejecutar_laboratorio():
    img = cargar_imagen("FRUTAS.PNG") 
    
    if img is not None:
        gris = convertir_a_grises(img)
        brillante = ajustar_brillo(img, 50)
        
        cv2.imshow("Original - Frutas", img)
        cv2.imshow("Grises - Frutas", gris)
        cv2.imshow("Brillo - Frutas", brillante)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    ejecutar_laboratorio()