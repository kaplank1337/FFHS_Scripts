import numpy as np

def invertiere_matrix(matrix):
    """
    Invertiert eine Matrix, falls sie invertierbar ist.

    Parameter:
        matrix (list of lists or numpy array): Die quadratische Matrix.

    Rückgabe:
        numpy array: Die inverse Matrix, falls die Matrix invertierbar ist.
        str: Fehlermeldung, falls die Matrix nicht invertierbar ist.
    """
    # Konvertiere die Matrix in ein numpy-Array
    matrix = np.array(matrix)

    # Überprüfen, ob die Matrix quadratisch ist
    if matrix.shape[0] != matrix.shape[1]:
        return "Die Matrix muss quadratisch sein, um invertierbar zu sein."

    # Berechne die Determinante
    det = np.linalg.det(matrix)
    print(f"Determinante der Matrix: {det}")

    # Überprüfen, ob die Determinante ungleich null ist
    if det == 0:
        return "Die Matrix ist nicht invertierbar (singulär)."

    # Berechne die Inverse der Matrix
    inverse = np.linalg.inv(matrix)
    return inverse

# Beispiel-Matrizen
matrix1 = [[0, 1, 0], [0, 0, 1],[1, 0, 0]]  # Invertierbar


print("Matrix:")
result1 = invertiere_matrix(matrix1)
print(result1)

