import numpy as np

def calculate_check_matrix(G):
    """
    Berechnet die Prüfmatrix H aus der Generatormatrix G.
    """
    k, n = G.shape
    P = G[:, k:]  # Paritätsmatrix aus G
    r = n - k     # Anzahl der Prüfbits
    I_r = np.eye(r, dtype=int)
    H = np.hstack((P.T, I_r))
    return H

def is_codeword(H, word):
    """
    Prüft, ob ein gegebenes Wort ein gültiges Codewort ist.
    """
    word = np.array([int(bit) for bit in word])  # Binärstring zu Array
    syndrome = np.dot(H, word) % 2  # Syndromberechnung
    return np.all(syndrome == 0), syndrome

def generate_codewords(G):
    """
    Generiert alle möglichen Codewörter aus der Generatormatrix G.
    """
    k = G.shape[0]
    codewords = []
    for i in range(2**k):
        m = np.array([int(bit) for bit in f"{i:0{k}b}"])  # Informationsvektor
        c = np.dot(m, G) % 2  # Codewort
        codewords.append(c)
    return np.array(codewords)

def hamming_distance(word1, word2):
    """
    Berechnet den Hamming-Abstand zwischen zwei Binärwörtern.
    """
    return np.sum(word1 != word2)

def closest_codeword(codewords, word):
    """
    Findet das Codewort mit dem kleinsten Hamming-Abstand zu einem gegebenen Wort.
    """
    word = np.array([int(bit) for bit in word])
    distances = [hamming_distance(word, codeword) for codeword in codewords]
    min_distance = min(distances)
    closest = codewords[distances.index(min_distance)]
    return closest, min_distance

# Gegebene Generatormatrix G
G = np.array([
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0]
], dtype=int)

# Gegebene Wörter
v = "1111111"
w = "1100011"

# Schritt 1: Prüfmatrix H berechnen
H = calculate_check_matrix(G)

# Schritt 2: Prüfen, ob die Wörter gültige Codewörter sind
is_v_codeword, syndrome_v = is_codeword(H, v)
is_w_codeword, syndrome_w = is_codeword(H, w)

print(f"v = {v} ist ein gültiges Codewort: {is_v_codeword}, Syndrom: {syndrome_v}")
print(f"w = {w} ist ein gültiges Codewort: {is_w_codeword}, Syndrom: {syndrome_w}")

# Schritt 3: Falls nicht, finde das nächste gültige Codewort
if not is_v_codeword or not is_w_codeword:
    codewords = generate_codewords(G)
    if not is_v_codeword:
        closest_v, dist_v = closest_codeword(codewords, v)
        print(f"Nächstes Codewort zu v: {closest_v}, Hamming-Abstand: {dist_v}")
    if not is_w_codeword:
        closest_w, dist_w = closest_codeword(codewords, w)
        print(f"Nächstes Codewort zu w: {closest_w}, Hamming-Abstand: {dist_w}")
