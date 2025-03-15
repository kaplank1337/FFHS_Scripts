import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from PIL import Image

def apply_dct_to_image(image):
    """
    Wendet die diskrete Kosinustransformation (DCT) auf ein 2D-Bild an.

    Parameters:
        image (numpy.ndarray): Grauwertbild als 2D-Array.

    Returns:
        numpy.ndarray: Frequenzbereich des Bildes nach der DCT.
    """
    return dct(dct(image.T, type=2, norm='ortho').T, type=2, norm='ortho')

def apply_idct_to_image(transformed_image):
    """
    Führt die Rücktransformation (inverse DCT) eines transformierten Bildes aus.

    Parameters:
        transformed_image (numpy.ndarray): Frequenzbereich des Bildes als 2D-Array.

    Returns:
        numpy.ndarray: Rücktransformiertes Bild in der Raumdomäne.
    """
    return idct(idct(transformed_image.T, type=2, norm='ortho').T, type=2, norm='ortho')

def process_and_visualize(image_path, title):
    """
    Lädt ein Bild, wendet die DCT und die inverse DCT an, und zeigt die Ergebnisse.

    Parameters:
        image_path (str): Pfad zum Bild.
        title (str): Titel des Bildes für die Visualisierung.
    """
    # Bild laden und in Grauwertbild umwandeln
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)

    # Diskrete Kosinustransformation (DCT) anwenden
    dct_image = apply_dct_to_image(image_array)

    # Rücktransformation (IDCT) durchführen
    idct_image = apply_idct_to_image(dct_image)

    # Ergebnisse anzeigen
    plt.figure(figsize=(12, 8))

    plt.subplot(1, 3, 1)
    plt.title(f"Originalbild: {title}")
    plt.imshow(image_array, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("DCT des Bildes")
    plt.imshow(np.log(np.abs(dct_image) + 1), cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Rücktransformiertes Bild")
    plt.imshow(idct_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# Beispielbilder verarbeiten und visualisieren
process_and_visualize("C:\\Users\\u244205\\Downloads\\BeispielBilder\\Cat03.jpg", "Cat03")
process_and_visualize("C:\\Users\\u244205\\Downloads\\BeispielBilder\\PNG_transparency_demonstration_1.png", "PNG_transparency_demonstration_1")

