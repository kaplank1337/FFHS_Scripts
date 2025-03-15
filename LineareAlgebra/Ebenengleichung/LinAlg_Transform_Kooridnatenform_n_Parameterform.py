import numpy as np

def parameterform_to_koordinatenform(a, b, c):
    """
    Wandelt eine Ebenengleichung von Parameterform in Koordinatenform um.

    Parameter:
        a (list): Ortsvektor (Punkt auf der Ebene).
        b (list): Erster Richtungsvektor.
        c (list): Zweiter Richtungsvektor.
    """
    print("=== Umwandlung von Parameterform in Koordinatenform ===")
    print(f"Gegebene Punkte:")
    print(f"Ortsvektor a: {a}")
    print(f"Richtungsvektor b: {b}")
    print(f"Richtungsvektor c: {c}")

    # Vektoren in NumPy-Arrays umwandeln
    a_vec = np.array(a, dtype=float)
    b_vec = np.array(b, dtype=float)
    c_vec = np.array(c, dtype=float)

    # Schritt 1: Kreuzprodukt von b und c berechnen, um den Normalenvektor zu erhalten
    n_vec = np.cross(b_vec, c_vec)
    print("\nSchritt 1: Kreuzprodukt von b und c (Normalenvektor):")
    print(f"Normalenvektor: {n_vec}")

    # Schritt 2: Ebenengleichung aufstellen: n_vec . (x - a) = 0
    # Die symbolischen Variablen werden hier als Strings dargestellt
    x, y, z = "x", "y", "z"
    r_vec = np.array([f"({x} - {a_vec[0]})",
                      f"({y} - {a_vec[1]})",
                      f"({z} - {a_vec[2]})"], dtype=object)

    ebene_terms = [f"{n_vec[i]} * {r_vec[i]}" for i in range(3)]
    ebene = " + ".join(ebene_terms) + " = 0"

    print("\nSchritt 2: Ebenengleichung aufstellen (Skalarprodukt mit (x - a)):")
    print(f"Ebenengleichung: {ebene}")

    # Schritt 3: Koordinatenform der Ebene (vereinfachen)
    koord_terms = [f"{n_vec[i]} * {var}" for i, var in enumerate([x, y, z])]
    ebene_koordinatenform = " + ".join(koord_terms) + f" = {np.dot(n_vec, a_vec)}"

    print("\nSchritt 3: Koordinatenform der Ebene:")
    print(ebene_koordinatenform)

    return ebene_koordinatenform


def koordinatenform_to_parameterform(normal, d):
    """
    Wandelt eine Ebenengleichung von Koordinatenform in Parameterform um.

    Parameter:
        normal (list): Normalenvektor der Ebene.
        d (int): Der konstante Term der Ebenengleichung.
    """
    print("\n=== Umwandlung von Koordinatenform in Parameterform ===")
    print(f"Gegebener Normalenvektor: {normal}")
    print(f"Konstanter Term d: {d}")

    # Normalenvektor als NumPy-Array
    n_vec = np.array(normal, dtype=float)

    # Einen Punkt auf der Ebene finden: Setze zwei Variablen auf 0
    punkt = None
    if n_vec[0] != 0:
        punkt = [-d / n_vec[0], 0, 0]
    elif n_vec[1] != 0:
        punkt = [0, -d / n_vec[1], 0]
    else:
        punkt = [0, 0, -d / n_vec[2]]

    print("\nSchritt 1: Einen Punkt auf der Ebene finden:")
    print(f"Punkt: {punkt}")

    # Zwei Richtungsvektoren finden (beliebig, aber linear unabhängig vom Normalenvektor)
    if n_vec[0] != 0:
        richtungsvektor_1 = np.array([0, 1, 0], dtype=float)
    else:
        richtungsvektor_1 = np.array([1, 0, 0], dtype=float)

    richtungsvektor_2 = np.cross(n_vec, richtungsvektor_1)

    print("\nSchritt 2: Zwei Richtungsvektoren finden:")
    print(f"Richtungsvektor 1: {richtungsvektor_1}")
    print(f"Richtungsvektor 2: {richtungsvektor_2}")

    # Schritt 3: Parameterform der Ebene
    parameterform = f"r(u, v) = {punkt} + u * {richtungsvektor_1} + v * {richtungsvektor_2}"
    print("\nSchritt 3: Parameterform der Ebene:")
    print(parameterform)

    return punkt, richtungsvektor_1, richtungsvektor_2


if __name__ == "__main__":
    # Beispiel 1: Parameterform -> Koordinatenform
    a = [1, 2, 5]
    b = [2, 3, 4]
    c = [1, -1, 6]
    print("\nBeispiel 1: Parameterform -> Koordinatenform")
    parameterform_to_koordinatenform(a, b, c)

    # Beispiel 2: Koordinatenform -> Parameterform
    normal = [2, 3, 4]
    d = 12
    print("\nBeispiel 2: Koordinatenform -> Parameterform")
    koordinatenform_to_parameterform(normal, d)
