import numpy as np

def berechne_basis(matrix):
    """
    Berechnet eine Basis des durch die Spaltenvektoren einer Matrix aufgespannten Vektorraums.

    Parameter:
        matrix (numpy.ndarray): Eine Matrix, deren Spalten die Vektoren darstellen.

    Rückgabe:
        basis (numpy.ndarray): Matrix mit den Basisvektoren als Spalten.
    """
    # Liste, um die Basisvektoren zu speichern
    basis_vectors = []

    # Basis durch Überprüfung linearer Abhängigkeit bestimmen
    for i in range(matrix.shape[1]):
        if len(basis_vectors) == 0:
            basis_vectors.append(matrix[:, i])
        else:
            # Temporäre Matrix mit den bisherigen Basisvektoren und dem neuen Vektor
            temp_matrix = np.column_stack(basis_vectors + [matrix[:, i]])
            if np.linalg.matrix_rank(temp_matrix) > len(basis_vectors):
                basis_vectors.append(matrix[:, i])

    return np.column_stack(basis_vectors)

if __name__ == "__main__":
    # Die Vektoren als Spalten in der Matrix definieren
    matrix = np.array([
        [1, 1, 3, 2],  # Erste Komponente der Vektoren
        [1, 2, 4, 3],  # Zweite Komponente der Vektoren
        [2, 3, 7, 5],  # Dritte Komponente der Vektoren
        [2, 4, 8, 6]   # Vierte Komponente der Vektoren
    ])

    print("Gegebene Matrix (Spalten sind Vektoren):")
    print(matrix)

    # Berechne die Basis
    basis = berechne_basis(matrix)

    print("\nBasis des Vektorraums:")
    print(basis)
