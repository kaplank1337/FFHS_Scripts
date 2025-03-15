import sympy as sp

def solve_matrix(matrix):
    """
    Berechnet das charakteristische Polynom, Eigenwerte, Eigenvektoren und Diagonalisierung,
    normierte Eigenvektoren und Diagonalisierung, algebraische und geometrische Vielfachheiten
    einer Matrix und überprüft, ob die Matrix diagonalisierbar ist.

    Parameter:
        matrix (list of lists or numpy array): Die Eingabematrix (2D, quadratisch).

    Rückgabe:
        Keiner. Gibt die Schritte und Ergebnisse aus.
    """
    # Konvertiere die Matrix in eine sympy-Matrix
    sym_matrix = sp.Matrix(matrix)
    n = sym_matrix.shape[0]

    print("Gegebene Matrix:")
    sp.pprint(sym_matrix)

    # Schritt 1: Charakteristisches Polynom berechnen
    lambda_var = sp.symbols('lambda')
    char_poly = sym_matrix.charpoly(lambda_var)
    print("\nCharakteristisches Polynom:")
    sp.pprint(char_poly.as_expr())

    # Schritt 2: Eigenwerte berechnen
    eigenvalues = sp.solve(char_poly.as_expr(), lambda_var)
    eigenvalue_counts = {value: eigenvalues.count(value) for value in set(eigenvalues)}
    print("\nEigenwerte (mit algebraischer Vielfachheit):")
    for eigenvalue, count in eigenvalue_counts.items():
        print(f"Eigenwert: {eigenvalue}, Algebraische Vielfachheit: {count}")

    # Variable zur Überprüfung der Diagonalisierbarkeit
    diagonalisierbar = True

    # Schritt 3: Geometrische Vielfachheit und Eigenvektoren und Diagonalisierung
    for eigenvalue in eigenvalue_counts:
        print(f"\nBerechnungen für Eigenwert λ = {eigenvalue}:")
        eigen_space_matrix = sym_matrix - eigenvalue * sp.eye(n)
        print("\nMatrix (A - λI):")
        sp.pprint(eigen_space_matrix)

        # Geometrische Vielfachheit = Dimension des Eigenraums
        eigen_space_dim = len(eigen_space_matrix.nullspace())
        print(f"Geometrische Vielfachheit: {eigen_space_dim}")

        # Überprüfung der Diagonalisierbarkeit
        if eigen_space_dim < eigenvalue_counts[eigenvalue]:
            diagonalisierbar = False

        # Eigenvektoren und Diagonalisierung berechnen
        print("\nEigenvektoren und Diagonalisierung:")
        for vec in eigen_space_matrix.nullspace():
            sp.pprint(vec)

        # Normierte Eigenvektoren und Diagonalisierung
        print("\nNormierte Eigenvektoren und Diagonalisierung:")
        for vec in eigen_space_matrix.nullspace():
            norm = sp.sqrt(sum([v**2 for v in vec]))
            normalized_vec = vec / norm
            sp.pprint(normalized_vec)

    # Überprüfung: Ist die Matrix diagonalisierbar?
    if diagonalisierbar:
        print("\nDie Matrix ist diagonalisierbar.")
    else:
        print("\nDie Matrix ist NICHT diagonalisierbar.")


if __name__ == "__main__":
    # Beispiel für eine 2x2 Matrix
    matrix_2x2 = [[3, 4],
                  [4, -3]]
    print("=== Ergebnisse für die 2x2 Matrix ===")
    solve_matrix(matrix_2x2)

    # #Beispiel für eine 3x3 Matrix (optional)
    # matrix_3x3 = [[2, 1, 2],
    #               [1, 2, 2],
    #               [1, 1, 3]]
    # print("\n=== Ergebnisse für die 3x3 Matrix ===")
    # solve_matrix(matrix_3x3)
