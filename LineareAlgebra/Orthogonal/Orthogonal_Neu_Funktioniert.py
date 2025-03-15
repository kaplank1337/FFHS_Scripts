import numpy as np

def gram_schmidt(vectors):
    """
    Wendet die Gram-Schmidt-Orthogonalisierung auf eine Menge von Vektoren an und normiert sie.

    Parameter:
    vectors : list of lists or numpy.ndarray
        Die Eingabevektoren, die orthogonalisiert werden sollen.

    Rückgabe:
    orthonormal_vectors : numpy.ndarray
        Die orthonormalisierten Vektoren.
    """
    vectors = np.array(vectors, dtype=float)
    orthogonal_vectors = []

    for v in vectors:
        # Orthogonalisiere v bzgl. der bereits orthogonalisierten Vektoren
        for u in orthogonal_vectors:
            proj = np.dot(v, u) / np.dot(u, u) * u
            v = v - proj
        # Nur hinzufügen, wenn der Vektor nicht Null ist (lineare Abhängigkeit vermeiden)
        if np.linalg.norm(v) > 1e-10:
            orthogonal_vectors.append(v / np.linalg.norm(v))  # Normiere den Vektor

    return np.array(orthogonal_vectors)

# Beispiel: Vektoren aus der Aufgabe
vectors = [
    [2, -1, 4],
    [0, 5, 6],
    [1, 6, 9]
]

orthonormal_vectors = gram_schmidt(vectors)
print("Orthogonalisierte und normierte Vektoren:")
print(orthonormal_vectors)
