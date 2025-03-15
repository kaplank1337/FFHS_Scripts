import numpy as np

def check_and_correct_codeword(H, received_word):
    """
    Prüft, ob ein Codewort fehlerhaft ist, und korrigiert es, falls möglich.

    Parameter:
    H : numpy.ndarray
        Die Prüfmatrix (n-k x n)
    received_word : list or numpy.ndarray
        Das empfangene Codewort (1 x n)

    Rückgabe:
    corrected_word : numpy.ndarray
        Das korrigierte Codewort (1 x n)
    is_valid : bool
        True, wenn das empfangene Wort gültig war, False, wenn es korrigiert wurde.
    syndrome : numpy.ndarray
        Das Syndrom, das den Fehler beschreibt (n-k x 1)
    """
    received_word = np.array(received_word, dtype=int)  # Empfangenes Wort als Array
    syndrome = np.dot(H, received_word) % 2  # Syndromberechnung

    if np.all(syndrome == 0):
        # Kein Fehler, das Wort ist gültig
        return received_word, True, syndrome

    # Fehlerlokalisierung: Vergleiche das Syndrom mit den Spalten von H
    for i in range(H.shape[1]):
        if np.array_equal(H[:, i], syndrome):
            # Fehler gefunden, korrigiere das entsprechende Bit
            received_word[i] = (received_word[i] + 1) % 2  # Bit umdrehen
            return received_word, False, syndrome

    # Wenn kein Fehler gefunden wurde, ist die Korrektur nicht möglich
    raise ValueError("Fehler konnte nicht lokalisiert werden.")

# Beispiel-Prüfmatrix
H = np.array([
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1]
], dtype=int)

# Empfangenes Codewort
received_word = [1, 1, 0, 0, 0, 1, 1]  # Beispiel mit möglichem Fehler

# Fehler prüfen und korrigieren
try:
    corrected_word, is_valid, syndrome = check_and_correct_codeword(H, received_word)
    if is_valid:
        print(f"Das empfangene Codewort {received_word} ist gültig.")
    else:
        print(f"Das empfangene Codewort war fehlerhaft.")
        print(f"Syndrom: {syndrome}")
        print(f"Korrigiertes Codewort: {corrected_word}")
except ValueError as e:
    print(f"Fehler: {e}")
