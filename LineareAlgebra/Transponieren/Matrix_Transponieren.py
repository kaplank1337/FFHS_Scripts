def transpose_matrix(matrix):
    """
    Transponiert die gegebene Matrix.

    :param matrix: Liste von Listen, die die Matrix repräsentiert.
    :return: Transponierte Matrix.
    """
    # Transponiere die Matrix (Zeilen werden zu Spalten)
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

# Beispiel: Eingabematrix Q
Q = [
    [2/3, -1/3, 2/3],
    [-1/3, 2/3, 2/3],
    [2/3, 2/3, -1/3]
]

# Transponiere die Matrix
Q_transposed = transpose_matrix(Q)

# Ausgabe
print("Originale Matrix Q:")
for row in Q:
    print(row)

print("\nTransponierte Matrix Q^T:")
for row in Q_transposed:
    print(row)
