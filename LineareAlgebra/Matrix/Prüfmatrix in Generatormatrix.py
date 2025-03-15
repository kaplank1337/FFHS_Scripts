import numpy as np
from itertools import product

def h_to_g(h_matrix):
    """
    Wandelt die Prüfmatrix H in die Generatormatrix G um.
    """
    # Dimensionen der Matrix
    n = h_matrix.shape[1]  # Länge der Codewörter
    r = h_matrix.shape[0]  # Anzahl der Prüfgleichungen
    k = n - r  # Dimension des Codes

    # Zerlege H in [-P^T | I_r]
    p_transposed = h_matrix[:, :k]
    identity_r = h_matrix[:, k:]

    # Berechne P aus -P^T
    p_matrix = -p_transposed % 2

    # Konstruiere G = [I_k | P]
    identity_k = np.eye(k, dtype=int)
    g_matrix = np.hstack((identity_k, p_matrix.T))

    return g_matrix, n, k

def generate_codewords(g_matrix):
    """
    Generiert alle Codewörter basierend auf der Generatormatrix G.
    """
    k = g_matrix.shape[0]
    n = g_matrix.shape[1]

    # Alle möglichen Informationsvektoren
    info_vectors = np.array(list(product([0, 1], repeat=k)))

    # Codewörter berechnen
    codewords = (info_vectors @ g_matrix) % 2

    return codewords

def calculate_minimum_distance(codewords):
    """
    Berechnet die Minimaldistanz d des Codes.
    """
    distances = []
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            distance = np.sum(codewords[i] != codewords[j])
            distances.append(distance)

    return min(distances)

# Beispiel-Prüfmatrix H
h_matrix = np.array([
    [1, 0, 0, 1],
    [0, 1, 1, 0]
], dtype=int)

# Schritt 1: H in G umwandeln
g_matrix, n, k = h_to_g(h_matrix)
print("Generatormatrix (G):\n", g_matrix)

# Schritt 2: Alle Codewörter generieren
codewords = generate_codewords(g_matrix)
print("Alle Codewörter:")
for cw in codewords:
    print("".join(map(str, cw)))

# Schritt 3: Minimaldistanz berechnen
d = calculate_minimum_distance(codewords)

# Ausgabe der Parameter
print(f"\nParameter des Codes:")
print(f"n (Länge der Codewörter): {n}")
print(f"k (Dimension des Codes): {k}")
print(f"d (Minimaldistanz): {d}")
