import numpy as np

def gauss_jordan_elimination(matrix):
    """
    Führt den Gauß-Jordan-Algorithmus auf einer gegebenen Matrix aus.
    Gibt die transformierte Matrix und die Basiswechselmatrix zurück.
    """
    rows, cols = matrix.shape
    identity = np.eye(rows)  # Einheitsmatrix zur Verfolgung der Transformationen
    augmented_matrix = np.hstack((matrix, identity))  # Augmentierte Matrix

    for i in range(rows):
        # Pivot-Element auswählen
        pivot = augmented_matrix[i, i]
        if abs(pivot) < 1e-10:  # Überprüfen auf numerische Stabilität
            # Falls Pivot 0 ist, tausche mit einer anderen Zeile
            for j in range(i + 1, rows):
                if abs(augmented_matrix[j, i]) > 1e-10:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
            pivot = augmented_matrix[i, i]
            if abs(pivot) < 1e-10:
                raise ValueError("Matrix ist singulär und kann nicht umgeformt werden.")

        # Normieren der Pivot-Zeile
        augmented_matrix[i] = augmented_matrix[i] / pivot

        # Nullstellen in der Pivot-Spalte erzeugen
        for j in range(rows):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    # Die Basiswechselmatrix ist jetzt in der rechten Hälfte
    transformed_matrix = augmented_matrix[:, :cols]
    basis_change_matrix = augmented_matrix[:, cols:]

    return transformed_matrix, basis_change_matrix

# Beispielmatrix
input_matrix = np.array([
    [1, 3, 2, -1],
    [2, 1, 1, 2]
], dtype=float)

# Gauß-Jordan-Algorithmus anwenden
try:
    transformed_matrix, basis_change_matrix = gauss_jordan_elimination(input_matrix)

    # Ergebnisse anzeigen
    print("Eingabematrix:")
    print(input_matrix)
    print("\nTransformierte Matrix (Linke Seite -> Einheitsmatrix) && (Rechte Seite --> Basiswechsel Matrix):")
    print(transformed_matrix)
    # print("\nBasiswechselmatrix:")
    # print(basis_change_matrix)
except ValueError as e:
    print(f"Fehler: {e}")
