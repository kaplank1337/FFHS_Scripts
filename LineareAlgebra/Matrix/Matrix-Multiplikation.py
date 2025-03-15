import numpy as np

def multipliziere_matrizen(matrix_1, matrix_2):
    """
    Multipliziert zwei Matrizen, wenn die Dimensionen kompatibel sind.

    :param matrix_1: Erste Matrix als 2D-Liste oder numpy-Array
    :param matrix_2: Zweite Matrix als 2D-Liste oder numpy-Array
    :return: Resultierende Matrix als numpy-Array oder Fehlermeldung
    """
    try:
        # Beide Matrizen in numpy-Arrays umwandeln
        matrix_1_np = np.array(matrix_1, dtype=float)
        matrix_2_np = np.array(matrix_2, dtype=float)

        # Prüfen, ob die Matrizen für die Multiplikation kompatibel sind
        if matrix_1_np.shape[1] != matrix_2_np.shape[0]:
            return "Fehler: Die Anzahl der Spalten der ersten Matrix muss gleich der Anzahl der Zeilen der zweiten Matrix sein."

        # Matrizenmultiplikation durchführen
        result = np.dot(matrix_1_np, matrix_2_np)
        return result
    except Exception as e:
        return f"Fehler: {str(e)}"

if __name__ == "__main__":
    # Beide Matrizen definieren
    matrix_1 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]

    matrix_2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Matrizen multiplizieren
    result = multipliziere_matrizen(matrix_1, matrix_2)

    # Ergebnis ausgeben
    if isinstance(result, str):  # Wenn ein Fehler vorliegt
        print(result)
    else:
        print("Das Resultat der Multiplikation ist:")
        print(result)
