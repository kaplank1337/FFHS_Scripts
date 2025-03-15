import numpy as np

def multiply_three_matrices(A, B, C):
    """
    Multipliziert drei Matrizen A, B und C.

    Args:
        A (np.ndarray): Erste Matrix.
        B (np.ndarray): Zweite Matrix.
        C (np.ndarray): Dritte Matrix.

    Returns:
        np.ndarray: Ergebnis der Matrixmultiplikation A * B * C.
    """
    # Prüfen, ob die Dimensionen für die Multiplikation kompatibel sind
    if A.shape[1] != B.shape[0] or B.shape[1] != C.shape[0]:
        raise ValueError("Die Dimensionen der Matrizen sind nicht kompatibel für die Multiplikation.")

    # Multiplikation von A, B und C
    result = A @ B @ C
    return result

# Beispiel
if __name__ == "__main__":
    # Beispielmatrizen definieren
    A = np.array([[1, 0, 3], [0, 1, 2], [0, 0, 1]])
    B = np.array([[1, 0, 4], [1, 2, 5], [0, 0, 1]])
    C = np.array([[0, 1, 1], [2, 3, 1], [0, 0, 1]])

    # Matrizen multiplizieren
    try:
        result = multiply_three_matrices(A, B, C)
        print("Matrix A:")
        print(A)
        print("\nMatrix B:")
        print(B)
        print("\nMatrix C:")
        print(C)
        print("\nErgebnis der Multiplikation (A * B * C):")
        print(result)
    except ValueError as e:
        print(f"Fehler: {e}")
