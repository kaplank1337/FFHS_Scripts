import numpy as np

def linearkombination(basis_vectors, target_vector):
    """
    Berechnet die Koeffizienten der Linearkombination eines Zielvektors aus gegebenen Basisvektoren.

    Parameter:
    basis_vectors : list of lists or numpy.ndarray
        Die Basisvektoren.
    target_vector : list or numpy.ndarray
        Der Vektor, der als Linearkombination dargestellt werden soll.

    Rückgabe:
    coefficients : numpy.ndarray
        Die Koeffizienten der Linearkombination.
    """
    # Erstelle die Basis-Matrix
    B = np.array(basis_vectors, dtype=float).T  # Basisvektoren als Spaltenmatrix
    v = np.array(target_vector, dtype=float)    # Zielvektor

    # Löse das Gleichungssystem B * c = v
    if np.linalg.matrix_rank(B) < len(B[0]):
        raise ValueError("Die Basisvektoren sind nicht linear unabhängig.")

    coefficients = np.linalg.lstsq(B, v, rcond=None)[0]  # Genaue Lösung oder Approximation
    return coefficients

# Beispiel
basis_vectors = [
    [-1,  1,  1,  1,],
    [ 1, -1,  1,  1,],
    [ 0,  0, -1,  1,],
    [ 1,  1,  0,  0,]   # Basisvektor 3
]

target_vector = [2, 4, 6, 8]  # Zielvektor

# Berechne die Linearkombination
coefficients = linearkombination(basis_vectors, target_vector)
print("Koeffizienten der Linearkombination:", coefficients)
