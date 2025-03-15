import numpy as np

def gauss_jordan_elimination_verbose(matrix):
    """
    Führt die Gauss-Jordan-Elimination an einer Matrix durch und erklärt jeden Schritt.

    Args:
        matrix (np.ndarray): Die Eingabematrix.

    Returns:
        np.ndarray: Die Matrix in RREF.
    """
    mat = matrix.astype(float)  # Arbeite mit Fließkommazahlen für präzise Berechnungen
    rows, cols = mat.shape
    lead = 0

    print("Initiale Matrix:")
    print(mat)
    print("-" * 40)

    for r in range(rows):
        if lead >= cols:  # Prüfe, ob wir am Ende der Spalten angekommen sind
            break
        i = r
        # Finde die Pivotzeile
        while mat[i, lead] == 0:
            i += 1
            if i == rows:  # Falls kein Pivot-Element in dieser Spalte existiert
                i = r
                lead += 1
                if lead == cols:  # Prüfe, ob `lead` aus den Spalten hinausgeht
                    break
        if lead == cols:  # Beende, falls alle Spalten verarbeitet wurden
            break

        # Tausche Zeilen, falls nötig
        if i != r:
            print(f"Tausche Zeile {r+1} mit Zeile {i+1} (für Pivot an Position {r}, {lead}):")
            mat[[r, i]] = mat[[i, r]]
            print(mat)
            print("-" * 40)

        # Normiere die Pivotzeile
        pivot = mat[r, lead]
        if pivot != 0:
            print(f"Normiere Zeile {r+1}, indem sie durch {pivot} geteilt wird (Pivot an {r}, {lead}):")
            mat[r] = mat[r] / pivot
            print(mat)
            print("-" * 40)

        # Eliminiere die anderen Zeilen
        for i in range(rows):
            if i != r:
                factor = mat[i, lead]
                print(f"Eliminiere Zeile {i+1}, indem {factor} * Zeile {r+1} subtrahiert wird:")
                mat[i] = mat[i] - factor * mat[r]
                print(mat)
                print("-" * 40)

        lead += 1

    print("Matrix in Reduced Row Echelon Form (RREF):")
    return mat

# Beispiel:
if __name__ == "__main__":
    # Eingabematrix definieren
    A = np.array([
        [1, 1, 1, 1],
        [1, -2, -3, 4],
        [-2, 1, 0, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ])

    # Gauss-Jordan-Elimination anwenden
    rref_matrix = gauss_jordan_elimination_verbose(A)

    print("\nErgebnis (RREF):")
    print(rref_matrix)
