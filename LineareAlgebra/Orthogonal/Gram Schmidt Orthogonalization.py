import numpy as np

def gram_schmidt(vectors):
    """
    Wendet die Gram-Schmidt-Orthogonalisierung auf eine Menge von Vektoren an.

    Parameter:
    vectors : list of lists or numpy.ndarray
        Die Eingabevektoren, die orthogonalisiert werden sollen.

    Rückgabe:
    orthogonal_vectors : numpy.ndarray
        Die orthogonalisierten Vektoren.
    """
    vectors = np.array(vectors, dtype=float)
    orthogonal_vectors = []

    for v in vectors:
        # Orthogonalisiere v bzgl. der bereits orthogonalisierten Vektoren
        for u in orthogonal_vectors:
            proj = np.dot(v, u) / np.dot(u, u) * u
            v = v - proj
        orthogonal_vectors.append(v)

    return np.array(orthogonal_vectors)

# Beispiel: Vektoren a, b, c, d
vectors = [
    [-1, 1, 1, 1],
    [1, -1, 1, 1],
    [-1, 1, -1, 1],
    [1, 1, 1, -1]
]

orthogonal_vectors = gram_schmidt(vectors)
print("Orthogonalisierte Vektoren:")
print(orthogonal_vectors)
