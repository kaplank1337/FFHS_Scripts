import numpy as np

def berechne_winkel(vektor1, vektor2):
    """
    Berechnet den Winkel zwischen zwei Vektoren (2D oder 3D).

    Parameter:
        vektor1 (list or numpy array): Der erste Vektor.
        vektor2 (list or numpy array): Der zweite Vektor.

    Rückgabe:
        float: Der Winkel in Grad.
    """
    # Konvertiere die Vektoren in numpy-Arrays
    vektor1 = np.array(vektor1)
    vektor2 = np.array(vektor2)

    # Überprüfen, ob die Dimensionen der Vektoren übereinstimmen
    if len(vektor1) != len(vektor2):
        raise ValueError("Die Vektoren müssen die gleiche Dimension haben (2D oder 3D).")

    # Berechne das Skalarprodukt
    skalarprodukt = np.dot(vektor1, vektor2)

    # Berechne die Beträge der Vektoren
    betrag_a = np.linalg.norm(vektor1)
    betrag_b = np.linalg.norm(vektor2)

    # Berechne den Cosinus des Winkels
    cos_theta = skalarprodukt / (betrag_a * betrag_b)

    # Begrenze cos_theta auf den Bereich [-1, 1] (Numerische Stabilität)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Berechne den Winkel in Radiant
    theta_rad = np.arccos(cos_theta)

    # Konvertiere den Winkel in Grad
    theta_deg = np.degrees(theta_rad)

    # Ausgabe der Schritte
    print(f"Skalarprodukt: {skalarprodukt}")
    print(f"Betrag von Vektor 1: {betrag_a}")
    print(f"Betrag von Vektor 2: {betrag_b}")
    print(f"cos(theta): {cos_theta}")
    print(f"Winkel (Radiant): {theta_rad}")
    print(f"Winkel (Grad): {theta_deg}")

    return theta_deg

# Beispiele für 2D- und 3D-Vektoren

# Beispiel 1: 2D-Vektoren
vektor1_2d = [1, 2]
vektor2_2d = [3, 4]
print("\n--- 2D-Beispiel ---")
winkel_2d = berechne_winkel(vektor1_2d, vektor2_2d)
print(f"\nDer Winkel zwischen den 2D-Vektoren beträgt: {winkel_2d:.2f} Grad")

# Beispiel 2: 3D-Vektoren
vektor1_3d = [3, 4, 5]
vektor2_3d = [5, 4, 3]
print("\n--- 3D-Beispiel ---")
winkel_3d = berechne_winkel(vektor1_3d, vektor2_3d)
print(f"\nDer Winkel zwischen den 3D-Vektoren beträgt: {winkel_3d:.2f} Grad")
