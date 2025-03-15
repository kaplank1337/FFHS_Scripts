import numpy as np

def g_to_h(g_matrix):
    """
    Wandelt eine Generatormatrix G in eine Prüfmatrix H um.
    """
    # Dimensionen der Matrix
    k = g_matrix.shape[0]  # Anzahl der Informationsbits
    n = g_matrix.shape[1]  # Länge der Codewörter
    r = n - k              # Anzahl der Prüfbits

    # Zerlege G in [I_k | P]
    identity_k = g_matrix[:, :k]
    p_matrix = g_matrix[:, k:]

    # Erstelle H = [-P^T | I_r]
    p_transposed = p_matrix.T
    identity_r = np.eye(r, dtype=int)
    h_matrix = np.hstack((p_transposed, identity_r))

    return h_matrix

# Beispiel-Generatormatrix G
g_matrix = np.array([
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
], dtype=int)

# Wandeln von G in H
h_matrix = g_to_h(g_matrix)
print("Generatormatrix (G):\n", g_matrix)
print("\nPrüfmatrix (H):\n", h_matrix)
