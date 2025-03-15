import numpy as np

def berechne_invertierte_matrix(matrix):
    """
    Berechnet die Inverse einer beliebigen n-dimensionalen quadratischen Matrix.

    :param matrix: 2D-Liste oder numpy-Array
    :return: Invertierte Matrix als numpy-Array oder Fehlermeldung
    """
    try:
        # Matrix in ein numpy-Array umwandeln
        matrix_np = np.array(matrix, dtype=float)

        # Prüfen, ob die Matrix quadratisch ist
        if matrix_np.shape[0] != matrix_np.shape[1]:
            return "Fehler: Die Matrix muss quadratisch sein."

        # Inverse berechnen
        invers_matrix = np.linalg.inv(matrix_np)
        return invers_matrix
    except np.linalg.LinAlgError as e:
        return f"Fehler: Die Matrix ist nicht invertierbar. ({str(e)})"

if __name__ == "__main__":
    # Matrix direkt im Code definieren
    matrix = [
        [1, 2, 2],
        [2, 1, 2],
        [2, 2, 1]
    ]

    # Inverse berechnen
    result = berechne_invertierte_matrix(matrix)

    # Ergebnis ausgeben
    if isinstance(result, str):  # Wenn ein Fehler vorliegt
        print(result)
    else:
        print("Die Inverse der Matrix ist:")
        print(result)
