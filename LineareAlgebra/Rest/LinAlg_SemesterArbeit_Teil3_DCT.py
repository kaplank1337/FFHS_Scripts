import numpy as np
from scipy.fftpack import dct, idct

np.set_printoptions(linewidth=np.inf)

def generate_dct_matrix(N):
    """
    Erstellt die Transformationsmatrix für die eindimensionale diskrete Kosinustransformation (DCT).

    Parameters:
        N (int): Größe des Signals.

    Returns:
        numpy.ndarray: DCT-Transformationsmatrix.
    """
    dct_matrix = np.zeros((N, N))
    for k in range(N):
        for n in range(N):
            if k == 0:
                dct_matrix[k, n] = np.sqrt(1 / N)
            else:
                dct_matrix[k, n] = np.sqrt(2 / N) * np.cos(np.pi * k * (2 * n + 1) / (2 * N))
    return dct_matrix

def dct_transform(signal):
    """
    Führt die eindimensionale diskrete Kosinustransformation (DCT) eines Signals aus.

    Parameters:
        signal (numpy.ndarray): Eingabesignal (1D-Array).

    Returns:
        numpy.ndarray: Transformiertes Signal im Frequenzbereich.
    """
    return dct(signal, type=2, norm='ortho')

def idct_transform(transformed_signal):
    """
    Führt die Rücktransformation (inverse DCT) eines transformierten Signals aus.

    Parameters:
        transformed_signal (numpy.ndarray): Signal im Frequenzbereich (1D-Array).

    Returns:
        numpy.ndarray: Rücktransformiertes Signal in der Zeitdomäne.
    """
    return idct(transformed_signal, type=2, norm='ortho')

# Beispiel: Demonstration der Funktion
if __name__ == "__main__":
    # Originalsignal
    signal = np.array([10, 20, 30, 40, 50, 60, 70, 80])
    print("Originalsignal:", signal)

    # DCT durchführen
    transformed_signal = dct_transform(signal)
    print("Transformiertes Signal (DCT):", transformed_signal)

    # Rücktransformation (IDCT) durchführen
    recovered_signal = idct_transform(transformed_signal)
    print("Rücktransformiertes Signal (IDCT):", recovered_signal)

    # Transformationsmatrix erstellen
    N = len(signal)
    dct_matrix = generate_dct_matrix(N)
    print("DCT-Transformationsmatrix:")
    print(dct_matrix)

    # DCT mit Transformationsmatrix durchführen
    transformed_with_matrix = np.dot(dct_matrix, signal)
    print("Transformiertes Signal mit Transformationsmatrix:", transformed_with_matrix)

    # Rücktransformation mit der Inversen der Transformationsmatrix durchführen
    inverse_dct_matrix = np.linalg.inv(dct_matrix)
    recovered_with_matrix = np.dot(inverse_dct_matrix, transformed_with_matrix)
    print("Rücktransformiertes Signal mit Inverser der Transformationsmatrix:", recovered_with_matrix)
