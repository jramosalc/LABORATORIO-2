import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('imagen_prueba.jpg')
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

brillo = cv2.convertScaleAbs(gris, alpha=1.2, beta=60)

# Visualizacion
plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1); plt.imshow(imagen_rgb); plt.title("Original"); plt.axis("off")
plt.subplot(1, 3, 2); plt.imshow(gris, cmap='gray'); plt.title("Gris"); plt.axis("off")
plt.subplot(1, 3, 3); plt.imshow(brillo, cmap='gray'); plt.title("Brillo Ajustado"); plt.axis("off")
plt.show()