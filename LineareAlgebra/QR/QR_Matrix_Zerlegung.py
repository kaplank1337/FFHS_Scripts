import numpy as np

def gram_schmidt_qr_decomposition(A):
    """
    QR-Zerlegung mit Gram-Schmidt-Verfahren.
    Gibt jeden Schritt aus.

    Parameters:
        A (numpy.ndarray): Eingabematrix (m x n).

    Returns:
        Q (numpy.ndarray): Orthonormale Matrix (m x n).
        R (numpy.ndarray): Obere Dreiecksmatrix (n x n).
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    print("Schritt 1: Starte Gram-Schmidt-Verfahren")

    for i in range(n):
        print(f"\nVerarbeite Spalte {i + 1} von A:")
        # Kopiere die i-te Spalte von A
        v = A[:, i]
        print(f"  Ursprünglicher Vektor v_{i+1}: {v}")

        # Orthogonalisiere bezüglich der bisherigen Basisvektoren
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], v)  # Projektion von v auf q_j
            print(f"  Projektion von v_{i+1} auf q_{j+1}: R[{j}, {i}] = {R[j, i]}")
            v = v - R[j, i] * Q[:, j]     # Subtrahiere Projektion
            print(f"  Aktualisierter Vektor v_{i+1} nach Abzug der Projektion: {v}")

        # Berechne die Norm des resultierenden Vektors
        R[i, i] = np.linalg.norm(v)
        print(f"  Norm von v_{i+1}: R[{i}, {i}] = {R[i, i]}")

        # Normalisiere den Vektor, um q_i zu erhalten
        Q[:, i] = v / R[i, i]
        print(f"  Normalisierter Vektor q_{i+1}: {Q[:, i]}")

    print("\nSchritt 2: Ergebnis")
    print("Orthonormale Matrix Q:")
    print(Q)
    print("\nObere Dreiecksmatrix R:")
    print(R)

    return Q, R

# Beispielmatrix
A = np.array([[-1, 2, 2],
              [0, 4, 5],
              [4, -3, 2]], dtype=float)

print("Eingabematrix A:")
print(A)

# Berechnung der QR-Zerlegung
Q, R = gram_schmidt_qr_decomposition(A)
