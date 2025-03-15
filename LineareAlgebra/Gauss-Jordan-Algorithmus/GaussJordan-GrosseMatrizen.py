def gauss_jordan_fix(matrix):
    """
    Bringt die Generatormatrix G in die Form [I | P], falls möglich.
    """
    matrix = matrix.copy()  # Vermeidung der Veränderung der Originalmatrix
    rows, cols = matrix.shape
    rank = 0  # Zählt die Anzahl der unabhängigen Zeilen (Rang der Matrix)

    for col in range(cols):
        if rank >= rows:
            break

        # Suche eine Zeile mit einer 1 in der aktuellen Spalte
        pivot_row = -1
        for row in range(rank, rows):
            if matrix[row, col] == 1:
                pivot_row = row
                break

        if pivot_row == -1:
            # Kein Pivot-Element in dieser Spalte, weiter zur nächsten Spalte
            continue

        # Tausche die aktuelle Zeile mit der Pivot-Zeile
        if pivot_row != rank:
            matrix[[rank, pivot_row]] = matrix[[pivot_row, rank]]

        # Setze alle anderen Werte in der Spalte auf 0
        for row in range(rows):
            if row != rank and matrix[row, col] == 1:
                matrix[row] = (matrix[row] + matrix[rank]) % 2

        # Erhöhe den Rang
        rank += 1

    # Überprüfen, ob der linke obere Block eine Einheitsmatrix bilden kann
    k = rank  # Anzahl der Informationsbits
    identity_part = matrix[:k, :k]
    if not np.array_equal(identity_part, np.eye(k, dtype=int)):
        print("Warnung: Matrix konnte nicht vollständig in die Form [I | P] gebracht werden.")

    return matrix

# Teste die Funktion erneut
try:
    G_reduced_fixed = gauss_jordan_fix(G)
    print("\nReduzierte Generatormatrix [I | P] (oder bestmöglich):")
    print(G_reduced_fixed)
except ValueError as e:
    print("\nFehler:", e)
