import numpy as np

def gram_schmidt(vectors):
    """
    Gram-Schmidt Orthogonalization Process

    Args:
        vectors (list of np.array): List of input vectors to orthogonalize.

    Returns:
        list of np.array: List of orthogonalized vectors.
    """
    orthogonal_vectors = []

    for v in vectors:
        # Subtract projections onto all previously computed orthogonal vectors
        for u in orthogonal_vectors:
            v = v - (np.dot(u, v) / np.dot(u, u)) * u

        orthogonal_vectors.append(v)

    return orthogonal_vectors

# Example Usage
if __name__ == "__main__":
    # Input vectors
    vectors = [
        np.array([13, -4, -2, -6]),
        np.array([-4, 7, -4, -12]),
        np.array([-2, -4, 13, -6]),
        np.array([1, -13, 1, -27])
    ]

    # Apply Gram-Schmidt Orthogonalization
    orthogonalized_vectors = gram_schmidt(vectors)

    # Print Results
    print("Orthogonalized Vectors:")
    for i, vec in enumerate(orthogonalized_vectors, 1):
        print(f"u{i} = {vec}")
