import numpy as np

def generate_parity_check_matrix(G):
    """
    Generiert die Paritätsprüfmatrix H aus einer gegebenen Generator-Matrix G.

    Args:
        G (numpy array): Generator-Matrix in der Form [I_k | P].

    Returns:
        numpy array: Paritätsprüfmatrix H.
    """
    # Dimensionen der Generator-Matrix
    rows, cols = G.shape

    # Extrahiere P aus der Generator-Matrix [I_k | P]
    k = rows
    P = G[:, k:cols]  # Paritätsmatrix (letzte cols - k Spalten)

    # Prüfe, ob die Matrix [I_k | P] korrekt aufgebaut ist
    I_k = G[:, :k]
    if not np.array_equal(I_k, np.eye(k, dtype=int)):
        raise ValueError("Die ersten k Spalten von G müssen eine Identitätsmatrix sein.")

    # Sicherstellen, dass die Dimensionen für das Stapeln übereinstimmen
    if P.shape[1] != cols - k:
        raise ValueError("Die Anzahl der Spalten von P stimmt nicht mit cols - k überein.")

    # Erstelle die Paritätsprüfmatrix H
    H = np.vstack((P.T, np.eye(cols - k, dtype=int)))
    return H

if __name__ == "__main__":
    # Beispielhafte Generator-Matrix
    G = np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ])

    # Generiere die Paritätsprüfmatrix
    try:
        H = generate_parity_check_matrix(G)
        print("Generator-Matrix G:")
        print(G)
        print("\nParitätsprüfmatrix H:")
        print(H)
    except ValueError as e:
        print(f"Fehler: {e}")
