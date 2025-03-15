import numpy as np

def compute_corrected_matrix_bases(matrix):
    """
    Berechnet die Basen der Zeilenräume und Spaltenräume einer Matrix korrekt.

    Args:
        matrix (np.ndarray): Eingabematrix (beliebige Dimensionen).

    Returns:
        tuple: Zwei Listen mit den Basenvektoren für den Zeilen- und Spaltenraum.
    """
    # Konvertiere die Matrix in eine Zeilen-Reduced Row-Echelon-Form (RREF)
    def rref(mat):
        mat = mat.astype(float)
        rows, cols = mat.shape
        lead = 0
        for r in range(rows):
            if lead >= cols:
                return mat
            i = r
            while mat[i, lead] == 0:
                i += 1
                if i == rows:
                    i = r
                    lead += 1
                    if cols == lead:
                        return mat
            mat[[r, i]] = mat[[i, r]]
            lv = mat[r, lead]
            mat[r] = mat[r] / lv
            for i in range(rows):
                if i != r:
                    lv = mat[i, lead]
                    mat[i] = mat[i] - lv * mat[r]
            lead += 1
        return mat

    # RREF für Zeilenreduktion berechnen
    rref_matrix = rref(matrix)
    rank = np.linalg.matrix_rank(matrix)

    # Basis des Zeilenraums: Wähle alle Zeilen mit nicht-Null-Einträgen
    row_basis = [matrix[i] for i in range(rref_matrix.shape[0]) if not np.all(rref_matrix[i] == 0)]

    # Basis des Spaltenraums: Finde unabhängige Spalten basierend auf der Originalmatrix
    independent_columns = []
    for col_idx in range(matrix.shape[1]):
        col_vector = matrix[:, col_idx]
        if len(independent_columns) < rank:
            if np.linalg.matrix_rank(np.column_stack(independent_columns + [col_vector])) > len(independent_columns):
                independent_columns.append(col_vector)
    col_basis = np.column_stack(independent_columns)

    return np.array(row_basis), col_basis


# Eingabematrix definieren
A = np.array([
    [1, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0]
])

# Basen berechnen
row_basis, col_basis = compute_corrected_matrix_bases(A)

# Ergebnisse prüfen
print("Basis des Zeilenraums:")
print(row_basis)
print("Basis des Spaltenraums:")
print(col_basis)
