import numpy as np

def koordinatenform_to_parameterform(a, b, c, d, dimension=2):
    """
    Wandelt eine Koordinatenform in die Parameterform um.

    Parameter:
        a, b, c, d (float): Koeffizienten der Koordinatengleichung (ax + by + cz + d = 0).
        dimension (int): Dimension der Ebene (2 oder 3).

    Rückgabe:
        dict: Parameterform mit Stützvektor und Richtungsvektoren.
    """
    if dimension == 2:
        # Überprüfen, ob der Fall 2D ist
        if c != 0:
            raise ValueError("Die dritte Komponente c sollte 0 für eine 2D-Ebene sein.")

        # Stützvektor bestimmen (wähle x = 0, berechne y)
        if b != 0:
            stuetzvektor = np.array([0, -d / b])
        elif a != 0:
            stuetzvektor = np.array([-d / a, 0])
        else:
            raise ValueError("Die Gleichung ist ungültig für 2D.")

        # Richtungsvektor bestimmen
        richtungsvektor = np.array([b, -a])  # Senkrecht zur Normalen

        return {
            "Stützvektor": stuetzvektor,
            "Richtungsvektor": richtungsvektor
        }

    elif dimension == 3:
        # Überprüfen, ob der Fall 3D ist
        if a == 0 and b == 0 and c == 0:
            raise ValueError("Ungültige Koordinatenform für 3D.")

        # Wähle x = 0 und y = 0, berechne z
        if c != 0:
            stuetzvektor = np.array([0, 0, -d / c])
        elif b != 0:
            stuetzvektor = np.array([0, -d / b, 0])
        elif a != 0:
            stuetzvektor = np.array([-d / a, 0, 0])
        else:
            raise ValueError("Ungültige Koordinatenform für 3D.")

        # Zwei unabhängige Richtungsvektoren finden
        if c != 0:
            richtungsvektor1 = np.array([1, 0, -a / c]) if c != 0 else np.array([1, 0, 0])
            richtungsvektor2 = np.array([0, 1, -b / c]) if c != 0 else np.array([0, 1, 0])
        elif b != 0:
            richtungsvektor1 = np.array([1, 0, 0])
            richtungsvektor2 = np.array([0, 0, 1])
        else:
            richtungsvektor1 = np.array([0, 1, 0])
            richtungsvektor2 = np.array([0, 0, 1])

        return {
            "Stützvektor": stuetzvektor,
            "Richtungsvektor1": richtungsvektor1,
            "Richtungsvektor2": richtungsvektor2
        }

    else:
        raise ValueError("Nur 2D- und 3D-Vektoren werden unterstützt.")

# Beispiele

# Beispiel 1: 2D
print("\n--- Beispiel: 2D-Ebene ---")
parameterform_2d = koordinatenform_to_parameterform(a=2, b=-3, c=0, d=6, dimension=2)
print("Stützvektor:", parameterform_2d["Stützvektor"])
print("Richtungsvektor:", parameterform_2d["Richtungsvektor"])

# Beispiel 2: 3D
print("\n--- Beispiel: 3D-Ebene ---")
parameterform_3d = koordinatenform_to_parameterform(a=2, b=3, c=4, d=5, dimension=3)
print("Stützvektor:", parameterform_3d["Stützvektor"])
print("Richtungsvektor 1:", parameterform_3d["Richtungsvektor1"])
print("Richtungsvektor 2:", parameterform_3d["Richtungsvektor2"])
