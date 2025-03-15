import numpy as np

def kreuzprodukt(v1, v2):
    """
    Berechnet das Kreuzprodukt zweier Vektoren v1 und v2.

    Parameter:
        v1 (list or tuple): Erster Vektor (3D).
        v2 (list or tuple): Zweiter Vektor (3D).

    Rückgabe:
        list: Das Kreuzprodukt der beiden Vektoren.
    """
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Die Vektoren müssen genau 3 Dimensionen haben.")

    # Kreuzprodukt berechnen
    result = [
        v1[1] * v2[2] - v1[2] * v2[1],  # x-Komponente
        v1[2] * v2[0] - v1[0] * v2[2],  # y-Komponente
        v1[0] * v2[1] - v1[1] * v2[0]   # z-Komponente
    ]

    return result

# Beispiel
vektor1 = [1, 2, 3]
vektor2 = [3,2,-2]

kreuzprodukt_ergebnis = kreuzprodukt(vektor1, vektor2)
print(f"Kreuzprodukt von {vektor1} und {vektor2}: {kreuzprodukt_ergebnis}")

# Optional: Überprüfung mit numpy
kreuzprodukt_numpy = np.cross(vektor1, vektor2)
print(f"Überprüfung mit numpy: {kreuzprodukt_numpy}")
