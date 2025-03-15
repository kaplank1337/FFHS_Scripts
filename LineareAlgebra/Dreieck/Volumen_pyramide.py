import numpy as np

def pyramiden_volumen(v1, v2, v3):
    """
    Berechnet das Volumen einer Pyramide, gegeben durch drei Vektoren.

    Parameter:
        v1, v2, v3 (list oder numpy.ndarray):
            Die drei Vektoren, die die Basisfläche der Pyramide und die Höhe definieren.

    Rückgabe:
        float: Das Volumen der Pyramide.
    """
    # Konvertiere die Vektoren in numpy-Arrays
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)
    v3 = np.array(v3, dtype=float)

    # Berechne das Spatprodukt (Vektorprodukt von v1 und v2, dann Skalarprodukt mit v3)
    spatprodukt = np.dot(v3, np.cross(v1, v2))

    # Das Volumen der Pyramide ist 1/6 des Betrags des Spatprodukts
    volumen = abs(spatprodukt) / 6

    return volumen

# Beispiel: Eingabe der Vektoren
v1 = [1, 0, 0]
v2 = [0, 1, 0]
v3 = [0, 0, 1]

volumen = pyramiden_volumen(v1, v2, v3)
print(f"Das Volumen der Pyramide beträgt: {volumen}")
