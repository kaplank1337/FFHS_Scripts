import numpy as np

def matrix_rank(matrix):
    """
    Funktion, um den Rang einer Matrix zu berechnen.

    Parameter:
        matrix (list of lists or numpy array): Die Eingabematrix (2D).

    Rückgabe:
        int: Rang der Matrix.
    """
    # Umwandlung in eine NumPy-Matrix, falls noch nicht erfolgt
    np_matrix = np.array(matrix)

    # Berechnung des Rangs
    rank = np.linalg.matrix_rank(np_matrix)

    return rank

# Beispielnutzung
# # 2x2 Matrix
# matrix_2d = [[0, 1],
#              [0, 0]]
# rank_2d = matrix_rank(matrix_2d)

# # 3x3 Matrix
# matrix_3d = [[1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9]]
# rank_3d = matrix_rank(matrix_3d)

#4x4 Matrix
matrix_4d = [[1, 1, 2, 2],
             [1, 2, 3, 4],
             [3, 4, 7, 8],
             [2, 3, 5, 6]]
rank_4d = matrix_rank(matrix_4d)

# print(rank_2d)
# print(rank_3d)
print(rank_4d)

