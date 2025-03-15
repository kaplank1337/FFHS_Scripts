import numpy as np

def determine_basis(vectors):
    """
    Bestimmt die Basis für einen Vektorraum, der durch die gegebenen Vektoren aufgespannt wird.

    Args:
        vectors (list of lists): Liste der Vektoren.

    Returns:
        numpy array: Basisvektoren.
    """
    # Erstelle die Matrix aus den Vektoren
    matrix = np.array(vectors).T  # Spaltenweise Anordnung

    # Berechne den Rang und bringe die Matrix in reduzierte Zeilenstufenform
    _, _, pivot_columns = np.linalg.svd(matrix, full_matrices=False)

    # Bestimme die unabhängigen Spalten (Pivot-Spalten)
    rref_matrix = np.linalg.matrix_rank(matrix)

    # Extrahiere die Basisvektoren
    basis_vectors = matrix[:, :rref_matrix]

    return basis_vectors

if __name__ == "__main__":
    # Gegebene Vektoren
    a = [1, 1, 2, 2]
    b = [1, 2, 3, 4]
    c = [3, 4, 7, 8]
    d = [2, 3, 5, 6]

    # Bestimme die Basis
    basis = determine_basis([a, b, c, d])

    print("Basisvektoren:")
    print(basis)
