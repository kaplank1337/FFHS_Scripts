import numpy as np

def create_generator_and_check_matrix():
    # Dimensionen
    k = 4  # Anzahl der Informationsbits
    n = 8  # Gesamtlänge des Codes (Informationsbits + Prüfbits)

    # Generatormatrix G
    I_k = np.eye(k, dtype=int)  # Einheitsmatrix (4x4)
    P = np.array([
        [1, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 1]
    ])  # Block P für die Prüfbits
    G = np.hstack((I_k, P))  # G = [I_k | P]

    # Prüfmatrix H
    I_nk = np.eye(n - k, dtype=int)  # Einheitsmatrix (2x2)
    P_T = P.T  # Transponierte von P
    H = np.hstack((P_T, I_nk))  # H = [P^T | I_nk]

    return G, H

# Generiere die Matrizen
G, H = create_generator_and_check_matrix()

# Ausgabe
print("Generatormatrix G:")
print(G)
print("\nPrüfmatrix H:")
print(H)
