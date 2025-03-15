def berechne_geometrie(stuetzvektor, richtungsvektor1, richtungsvektor2=None):
    """
    Berechnet die Parameterform und Koordinatenform für eine Gerade (2D/3D) oder eine Ebene (3D).
    Gibt die Schritte der Lösung aus.

    Parameter:
        stuetzvektor (list): Der Stützvektor der Geraden/Ebene (Punkt auf der Geraden/Ebene).
        richtungsvektor1 (list): Der erste Richtungsvektor.
        richtungsvektor2 (list, optional): Der zweite Richtungsvektor (nur für Ebenen in 3D).

    Rückgabe:
        dict: Ergebnisse mit Parameterform und Koordinatenform.
    """
    dimension = len(stuetzvektor)

    if richtungsvektor2 is None:
        # Berechnung für eine Gerade
        if dimension != len(richtungsvektor1):
            raise ValueError("Stützvektor und Richtungsvektor müssen die gleiche Dimension haben.")

        print("\n--- Schritt-für-Schritt-Lösung (Gerade) ---")

        # Parameterform
        print("\n1. Berechne die Parameterform:")
        if dimension == 2:
            print(f"Gegeben:\n  Stützvektor: {stuetzvektor}\n  Richtungsvektor: {richtungsvektor1}")
            parameterform = f"r(t) = ({stuetzvektor[0]}, {stuetzvektor[1]}) + t * ({richtungsvektor1[0]}, {richtungsvektor1[1]})"
            print(parameterform)
        elif dimension == 3:
            print(f"Gegeben:\n  Stützvektor: {stuetzvektor}\n  Richtungsvektor: {richtungsvektor1}")
            parameterform = f"r(t) = ({stuetzvektor[0]}, {stuetzvektor[1]}, {stuetzvektor[2]}) + t * ({richtungsvektor1[0]}, {richtungsvektor1[1]}, {richtungsvektor1[2]})"
            print(parameterform)
        else:
            raise ValueError("Nur 2D- oder 3D-Vektoren werden unterstützt.")

        # Koordinatenform
        print("\n2. Berechne die Koordinatenform:")
        if dimension == 2:
            # Bestimme den Normalenvektor
            normalenvektor = [-richtungsvektor1[1], richtungsvektor1[0]]
            print(f"Normalenvektor: ({normalenvektor[0]}, {normalenvektor[1]})")

            # Berechne c
            a, b = normalenvektor
            x0, y0 = stuetzvektor
            c = -(a * x0 + b * y0)
            print(f"c = -(a * x0 + b * y0) = -({a} * {x0} + {b} * {y0}) = {c}")

            koordinatenform = f"{a}x + {b}y + {c} = 0"
            print(f"Koordinatenform: {koordinatenform}")
        elif dimension == 3:
            print("Die Koordinatenform einer Gerade in 3D ist nicht definiert.")
            koordinatenform = "Nicht definiert"
        else:
            raise ValueError("Nur 2D- oder 3D-Vektoren werden unterstützt.")

        return {
            "Parameterform": parameterform,
            "Koordinatenform": koordinatenform
        }
    else:
        # Berechnung für eine Ebene
        if dimension != 3 or len(richtungsvektor1) != 3 or len(richtungsvektor2) != 3:
            raise ValueError("Für Ebenen müssen alle Vektoren 3D-Vektoren sein.")

        print("\n--- Schritt-für-Schritt-Lösung (Ebene) ---")

        # Parameterform
        print("\n1. Berechne die Parameterform:")
        print(f"Gegeben:\n  Stützvektor: {stuetzvektor}\n  Richtungsvektor 1: {richtungsvektor1}\n  Richtungsvektor 2: {richtungsvektor2}")
        parameterform = f"r(s, t) = ({stuetzvektor[0]}, {stuetzvektor[1]}, {stuetzvektor[2]}) + s * ({richtungsvektor1[0]}, {richtungsvektor1[1]}, {richtungsvektor1[2]}) + t * ({richtungsvektor2[0]}, {richtungsvektor2[1]}, {richtungsvektor2[2]})"
        print(parameterform)

        # Koordinatenform
        print("\n2. Berechne die Koordinatenform:")
        # Normalenvektor berechnen (Kreuzprodukt der Richtungsvektoren)
        normalenvektor = [
            richtungsvektor1[1] * richtungsvektor2[2] - richtungsvektor1[2] * richtungsvektor2[1],
            richtungsvektor1[2] * richtungsvektor2[0] - richtungsvektor1[0] * richtungsvektor2[2],
            richtungsvektor1[0] * richtungsvektor2[1] - richtungsvektor1[1] * richtungsvektor2[0],
            ]
        print(f"Normalenvektor: {normalenvektor}")

        # Berechne d
        a, b, c = normalenvektor
        x0, y0, z0 = stuetzvektor
        d = -(a * x0 + b * y0 + c * z0)
        print(f"d = -(a * x0 + b * y0 + c * z0) = -({a} * {x0} + {b} * {y0} + {c} * {z0}) = {d}")

        koordinatenform = f"{a}x + {b}y + {c}z + {d} = 0"
        print(f"Koordinatenform: {koordinatenform}")

        return {
            "Parameterform": parameterform,
            "Koordinatenform": koordinatenform
        }


# # Beispiel für eine Gerade in 2D
# stuetzvektor_2d = [2, 3]
# richtungsvektor_2d = [6, 3]
# print("\n--- 2D Beispiel (Gerade) ---")
# ergebnisse_2d = berechne_geometrie(stuetzvektor_2d, richtungsvektor_2d)

# Beispiel für eine Ebene in 3D
stuetzvektor_3d = [1, 3, 2]
richtungsvektor1_3d = [1, 0, -1]
richtungsvektor2_3d = [0, 2, -1]
print("\n--- 3D Beispiel (Ebene) ---")
ergebnisse_3d = berechne_geometrie(stuetzvektor_3d, richtungsvektor1_3d, richtungsvektor2_3d)
