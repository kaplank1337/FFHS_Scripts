import numpy as np

def complete_generator_matrix(G):
    """
    Vervollständigt die fehlenden Werte in einer Generator-Matrix G.

    Args:
        G (numpy array): Generator-Matrix mit möglichen fehlenden Einträgen (z. B. `?`).

    Returns:
        numpy array: Vervollständigte Generator-Matrix.
    """
    rows, cols = G.shape

    # Konvertiere die Matrix in einen objektbasierten Datentyp für gemischte Eingaben
    G = G.astype(object)

    # Ersetze '?' durch -1
    G = np.where(G == '?', -1, G).astype(int)

    # Trenne die Matrix in [I_k | P]
    k = rows
    I_k = G[:, :k]  # Identitätsmatrix
    P = G[:, k:]    # Paritätsmatrix

    # Prüfe, ob I_k eine Identitätsmatrix ist
    if not np.array_equal(I_k, np.eye(k, dtype=int)):
        raise ValueError("Die ersten k Spalten von G müssen eine Identitätsmatrix sein.")

    # Berechnung der fehlenden Einträge in P
    for i in range(P.shape[0]):
        for j in range(P.shape[1]):
            if P[i, j] == -1:
                # Setze fehlende Einträge so, dass lineare Unabhängigkeit gewährleistet bleibt
                P[i, j] = 0 if np.sum(P[:, j]) % 2 == 0 else 1

    # Zusammensetzen der vollständigen Matrix
    G_completed = np.hstack((I_k, P))
    return G_completed

if __name__ == "__main__":
    # Beispielhafte Generator-Matrix mit fehlenden Einträgen
    G = np.array([
        [1, 0, 0, 0, 1, '?', 0],
        [0, 1, 0, 0, 1, 0, '?'],
        [0, 0, 1, 0, 0, 1, '?'],
        [0, 0, 0, 1, 1, 1, 1]
    ], dtype=object)  # Setze dtype explizit auf object

    # Vervollständige die Matrix
    completed_G = complete_generator_matrix(G)

    print("Vervollständigte Generator-Matrix:")
    print(completed_G)
