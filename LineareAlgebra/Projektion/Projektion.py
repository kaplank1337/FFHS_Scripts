import numpy as np

def compute_projection_matrix(r):
    """
    Berechnet die Abbildungsmatrix der Parallelprojektion
    auf die Ebene z=0 entlang der Richtung r.

    Args:
        r (numpy array): Richtungsvektor (3,).

    Returns:
        numpy array: Abbildungsmatrix (3, 3).
    """
    rx, ry, rz = r

    if rz == 0:
        raise ValueError("Die Projektion ist nicht definiert, da rz = 0 ist.")

    # Erstelle die Projektion-Matrix
    P = np.array([
        [1, 0, -rx / rz],
        [0, 1, -ry / rz],
        [0, 0, 0]
    ])
    return P

def project_point(point, P):
    """
    Projiziert einen Punkt mit der gegebenen Abbildungsmatrix.

    Args:
        point (numpy array): Punkt als (3,)-Array.
        P (numpy array): Abbildungsmatrix (3, 3).

    Returns:
        numpy array: Projizierter Punkt (3,).
    """
    return P @ point

if __name__ == "__main__":
    # Projektrichtung
    r = np.array([3, 2, 1])

    # Punkt, der projiziert werden soll
    point = np.array([4, 5, 6])

    # Berechnung der Abbildungsmatrix
    P = compute_projection_matrix(r)

    print("Abbildungsmatrix der Parallelprojektion:")
    print(P)

    # Projektion des Punktes
    projected_point = project_point(point, P)

    print("\nPunkt vor der Projektion:")
    print(point)

    print("\nPunkt nach der Projektion:")
    print(projected_point)
