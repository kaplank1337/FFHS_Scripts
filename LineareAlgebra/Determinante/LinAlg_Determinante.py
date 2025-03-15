import numpy as np

def calculate_determinant(matrix):
    """
    Berechnet die Determinante einer quadratischen Matrix mit numpy.

    Parameter:
        matrix (list of lists): Die Eingabematrix (quadratisch, 2x2 bis 5x5).

    Rückgabe:
        Keiner. Gibt die Schritte der Berechnung aus.
    """
    # Konvertiere die Matrix in ein numpy-Array
    np_matrix = np.array(matrix, dtype=float)
    n = np_matrix.shape[0]

    if n < 2 or n > 5:
        print("Nur Matrizen von 2x2 bis 5x5 sind erlaubt.")
        return

    print("Gegebene Matrix:")
    print(np_matrix)
    print("\nBerechnung der Determinante:")

    # Berechne die Determinante mit numpy
    determinant = np.linalg.det(np_matrix)

    print("\nEndergebnis (Determinante):")
    print(f"{determinant:.2f}")


if __name__ == "__main__":
    # # Beispiel für eine 2x2 Matrix
    # matrix_2x2 = [[2, 4],
    #               [6, 5]]
    # print("=== 2x2 Matrix ===")
    # calculate_determinant(matrix_2x2)

    # Beispiel für eine 3x3 Matrix
    matrix_3x3 = [[1, 4, 7],
                  [2, 5, 8],
                  [3, 7, 11]]
    print("\n=== 3x3 Matrix ===")
    calculate_determinant(matrix_3x3)

    # # Beispiel für eine 4x4 Matrix
    # matrix_4x4 = [[1, 0, 0, 1],
    #               [0, 1, 0, 1],
    #               [0, 0, 1, 1],
    #               [1, 1, 1, 3]]
    # print("\n=== 4x4 Matrix ===")
    # calculate_determinant(matrix_4x4)
    #
    # # Beispiel für eine 5x5 Matrix
    # matrix_5x5 = [[1, 0, 2, -1, 3],
    #               [3, 0, 0, 5, 0],
    #               [2, 1, 4, 0, -1],
    #               [0, 6, 0, -2, 0],
    #               [5, 0, 3, 0, 1]]
    # print("\n=== 5x5 Matrix ===")
    # calculate_determinant(matrix_5x5)
