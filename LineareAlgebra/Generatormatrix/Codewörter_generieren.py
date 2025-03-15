import numpy as np

def generate_codewords(G):
    """
    Generiert alle möglichen Codewörter aus der Generatormatrix G.

    Parameter:
    G : numpy.ndarray
        Die Generatormatrix (k x n)

    Rückgabe:
    codewords : numpy.ndarray
        Alle möglichen Codewörter (2^k x n)
    """
    k = G.shape[0]  # Anzahl der Informationsbits (Zeilen von G)
    n = G.shape[1]  # Länge der Codewörter (Spalten von G)
    codewords = []

    # Alle möglichen Informationsvektoren durchgehen
    for i in range(2**k):
        # Informationsvektor als Binärarray erstellen
        m = np.array([int(bit) for bit in f"{i:0{k}b}"], dtype=int)
        # Codewort berechnen: m * G (mod 2)
        c = np.dot(m, G) % 2
        codewords.append(c)

    return np.array(codewords)

# Gegebene Generatormatrix
G = np.array([
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0]
], dtype=int)

# Codewörter generieren
codewords = generate_codewords(G)

print("Generierte Codewörter:")
for codeword in codewords:
    print("".join(map(str, codeword)))
