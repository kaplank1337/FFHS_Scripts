import numpy as np

def affine_transformation(A, x, b):
    """
    Führt eine affine Transformation mit homogenen Koordinaten durch.

    Args:
        A (np.ndarray): Die lineare Transformationsmatrix (n x n).
        x (np.ndarray): Der Vektor im n-dimensionalen Raum (n x 1).
        b (np.ndarray): Der Translationsvektor (n x 1).

    Returns:
        np.ndarray: Der transformierte Vektor im homogenen Koordinatensystem.
    """
    # Dimension prüfen
    n = A.shape[0]
    if A.shape[1] != n or x.shape[0] != n or b.shape[0] != n:
        raise ValueError("Die Dimensionen von A, x und b müssen übereinstimmen.")

    # Homogene Koordinaten erstellen
    x_h = np.append(x, 1)  # Homogene Erweiterung von x (n -> n+1)
    A_h = np.vstack([np.hstack([A, b.reshape(-1, 1)]), [0] * n + [1]])  # Homogene Matrix (n+1 x n+1)

    # Transformation durchführen
    result_h = A_h @ x_h  # Matrixmultiplikation

    return result_h

# Beispiel
if __name__ == "__main__":
    # Beispielwerte
    A = np.array([[1, 0], [0, 1]])  # Transformationsmatrix (Skalierung)
    x = np.array([21, 9])  # Ursprünglicher Punkt
    b = np.array([-6, 7])  # Translationsvektor

    # Affine Transformation
    result = affine_transformation(A, x, b)

    print("Homogene Transformationsmatrix:")
    print(np.vstack([np.hstack([A, b.reshape(-1, 1)]), [0, 0, 1]]))  # Zeigt die vollständige Matrix
    print("\nTransformierter Punkt in homogenen Koordinaten:")
    print(result)
    print("\nTransformierter Punkt in normalen Koordinaten:")
    print(result[:-1])  # Ohne homogene Komponente
