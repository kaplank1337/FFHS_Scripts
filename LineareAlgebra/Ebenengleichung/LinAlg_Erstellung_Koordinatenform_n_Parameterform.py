import numpy as np

def gerade_aus_punkten(punkt1, punkt2):
    """
    Berechnet die Parameterform und Koordinatengleichung einer Geraden
    durch zwei gegebene Punkte.

    Parameter:
        punkt1 (tuple): Erster Punkt (x1, y1, z1).
        punkt2 (tuple): Zweiter Punkt (x2, y2, z2).

    Gibt die Parameterform und die Koordinatengleichung der Geraden aus.
    """
    print("=== Berechnung der Geradengleichung ===")
    print(f"Punkt 1: {punkt1}")
    print(f"Punkt 2: {punkt2}")

    # Konvertiere die Punkte in NumPy-Arrays
    p1 = np.array(punkt1, dtype=float)
    p2 = np.array(punkt2, dtype=float)

    # Schritt 1: Richtungsvektor berechnen
    richtungsvektor = p2 - p1
    print("\nSchritt 1: Richtungsvektor der Geraden:")
    for elem in richtungsvektor:
        print(f"⎡{elem}⎤")
    print("")

    # Schritt 2: Parameterform Koordinaten Gleichung aufstellen
    print("\nSchritt 2: Parameterform Koordinaten Gleichung der Geraden:")
    t = "t"
    parameterform = [[f"{richtungsvektor[i]}*{t} + {p1[i]}" for i in range(len(p1))]]
    print(f"r(t) = {parameterform}")

    # Schritt 3: Koordinatengleichung (nur für 2D-Fall)
    if len(punkt1) == 2:  # Für Geraden in der Ebene (2D)
        print("\nSchritt 3: Koordinatengleichung der Geraden (2D):")
        x1, y1 = p1
        x2, y2 = p2
        if x2 - x1 != 0:  # Keine vertikale Gerade
            steigung = (y2 - y1) / (x2 - x1)
            y_achsenabschnitt = y1 - steigung * x1
            print(f"y - {y1:.2f} = ({steigung:.2f}) * (x - {x1:.2f})")
        else:
            print(f"Die Gerade ist vertikal: x = {x1}")
    else:
        print("\nDie Koordinatengleichung ist nur für 2D sinnvoll.")

    return richtungsvektor

# Beispiel:
punkt1 = (2, 3)
punkt2 = (8, 6)

richtungsvektor = gerade_aus_punkten(punkt1, punkt2)
