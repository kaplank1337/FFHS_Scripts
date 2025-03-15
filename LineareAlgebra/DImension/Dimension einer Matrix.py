import numpy as np

def calculate_matrix_dimension(matrix):
    """
    Berechnet die Dimension einer Matrix, definiert durch ihren Rang.

    Args:
        matrix (np.ndarray): Eingabematrix.

    Returns:
        int: Die Dimension der Matrix (Rang).
    """
    # Berechne den Rang der Matrix
    rank = np.linalg.matrix_rank(matrix)
    return rank

# Beispiel
if __name__ == "__main__":
    # Eingabematrix definieren
    A = np.array([
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 3]
    ])

    print("Matrix:")
    print(A)

    # Dimension der Matrix berechnen
    dimension = calculate_matrix_dimension(A)

    print(f"\nDie Dimension der Matrix ist: {dimension}")
