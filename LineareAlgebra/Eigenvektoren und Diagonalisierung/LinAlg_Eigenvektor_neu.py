from sympy import Matrix, symbols, simplify
from sympy.abc import x

def analyze_matrix(matrix):
    matrix = Matrix(matrix)
    print("\nMatrix:")
    print(matrix)

    # Charakteristisches Polynom
    char_poly = matrix.charpoly(x)
    print("\nCharakteristisches Polynom:")
    print(simplify(char_poly.as_expr()))

    # Eigenwerte und algebraische Vielfachheit
    eigenvals = matrix.eigenvals()
    print("\nEigenwerte und algebraische Vielfachheit:")
    for eigenvalue, algebraic_multiplicity in eigenvals.items():
        print(f"Eigenwert: {eigenvalue}, Algebraische Vielfachheit: {algebraic_multiplicity}")

    # Eigenvektoren und Diagonalisierung und geometrische Vielfachheit
    eigenvects = matrix.eigenvects()
    print("\nEigenvektoren und Diagonalisierung, normierte Eigenvektoren und Diagonalisierung und geometrische Vielfachheit:")
    for eigenvalue, algebraic_multiplicity, eigenvectors in eigenvects:
        print(f"\nEigenwert: {eigenvalue}")
        print(f"Geometrische Vielfachheit: {len(eigenvectors)}")
        for idx, vec in enumerate(eigenvectors, start=1):
            normalized_vec = vec.normalized()
            print(f"Eigenvektor {idx}: {vec}")
            print(f"Normierter Eigenvektor {idx}: {normalized_vec}")

    # Diagonalisierbarkeit und diagonalisierte Matrix
    is_diagonalizable = matrix.is_diagonalizable()
    print("\nIst die Matrix diagonalisierbar?", "Ja" if is_diagonalizable else "Nein")

    if is_diagonalizable:
        P, D = matrix.diagonalize()
        print("\nDiagonalisierte Matrix:")
        print(D)
        print("\nTransformation Matrix P:")
        print(P)
    else:
        print("\nMatrix ist nicht diagonalisierbar.")

if __name__ == "__main__":
    # Beispielmatrix hier definieren
    matrix_input = [[0, 5],
                    [-5, 0]]
    print("Analyzing predefined matrix:")
    analyze_matrix(matrix_input)
