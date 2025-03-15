import numpy as np

def vektor_multiplikation(vektor1, vektor2, methode="skalar"):
    """
    Multipliziert zwei Vektoren nach der angegebenen Methode.

    Parameter:
        vektor1 (list or numpy array): Der erste Vektor.
        vektor2 (list or numpy array): Der zweite Vektor.
        methode (str): "skalar" für Skalarprodukt, "kreuz" für Kreuzprodukt.

    Rückgabe:
        float oder numpy array: Ergebnis der Multiplikation.
    """
    vektor1 = np.array(vektor1)
    vektor2 = np.array(vektor2)

    if methode == "skalar":
        if len(vektor1) != len(vektor2):
            raise ValueError("Die Vektoren müssen die gleiche Dimension für das Skalarprodukt haben.")
        skalarprodukt = np.dot(vektor1, vektor2)
        print(f"Formel für das Skalarprodukt: a · b = Σ(a_i * b_i)")
        print(f"Berechnung: {vektor1} · {vektor2} = {skalarprodukt}")
        return skalarprodukt

    elif methode == "kreuz":
        if len(vektor1) != 3 or len(vektor2) != 3:
            raise ValueError("Das Kreuzprodukt ist nur für 3D-Vektoren definiert.")
        kreuzprodukt = np.cross(vektor1, vektor2)
        print("Formel für das Kreuzprodukt:")
        print("a × b = (a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)")
        print(f"Berechnung: {vektor1} × {vektor2} = {kreuzprodukt}")
        return kreuzprodukt

    else:
        raise ValueError("Unbekannte Methode. Bitte 'skalar' oder 'kreuz' angeben.")

# Beispiele

# Skalarprodukt
vektor_a = [-1, 1, 1, 1]
vektor_b = [-1, 1, -1, 1]
print("\nSkalarprodukt:")
skalar_resultat = vektor_multiplikation(vektor_a, vektor_b, methode="skalar")

# # Kreuzprodukt
# vektor_c = [1, 2, 3]
# vektor_d = [4, 5, 6]
# print("\nKreuzprodukt:")
# kreuz_resultat = vektor_multiplikation(vektor_c, vektor_d, methode="kreuz")
