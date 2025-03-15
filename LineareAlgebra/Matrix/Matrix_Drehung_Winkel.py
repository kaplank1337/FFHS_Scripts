import numpy as np

def rotation_matrix(angle, point):
    """
    Erstellt die Darstellungs-Matrix für eine Drehung um einen Punkt.

    Args:
        angle (float): Der Drehwinkel in Radiant.
        point (tuple): Der Drehmittelpunkt (px, py).

    Returns:
        np.ndarray: Die 3x3-Transformationsmatrix.
    """
    px, py = point

    # Translationsmatrix, um den Punkt zum Ursprung zu verschieben
    T_hin = np.array([
        [1, 0, -px],
        [0, 1, -py],
        [0, 0, 1]
    ])

    # Rotationsmatrix um den Ursprung
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    R = np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])

    # Translationsmatrix, um den Punkt zurückzuschieben
    T_zurück = np.array([
        [1, 0, px],
        [0, 1, py],
        [0, 0, 1]
    ])

    # Gesamtdarstellungs-Matrix: Rücktransformation * Rotation * Hintransformation
    M = T_zurück @ R @ T_hin
    return M

def transform_point(matrix, point):
    """
    Transformiert einen Punkt mit der gegebenen Transformationsmatrix.

    Args:
        matrix (np.ndarray): Die 3x3-Transformationsmatrix.
        point (tuple): Der zu transformierende Punkt (x, y).

    Returns:
        tuple: Der transformierte Punkt (x', y').
    """
    x, y = point
    point_homogeneous = np.array([x, y, 1])  # Homogene Koordinaten
    transformed_point = matrix @ point_homogeneous
    return transformed_point[0], transformed_point[1]

# Beispiel
if __name__ == "__main__":
    # Drehwinkel (in Radiant, z. B. 270° = 3π/2)
    angle = 3 * np.pi / 2  # 270 Grad im Gegenuhrzeigersinn

    # Drehmittelpunkt
    point = (4, 1)

    # Transformationsmatrix berechnen
    M = rotation_matrix(angle, point)
    print("Transformationsmatrix:")
    print(M)

    # # Einen Punkt transformieren
    # original_point = (6, 3)
    # transformed_point = transform_point(M, original_point)
    # print("\nOriginalpunkt:", original_point)
    # print("Transformierter Punkt:", transformed_point)
