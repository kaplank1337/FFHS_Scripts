def hamming_distance(seq1, seq2):
    """
    Berechnet den Hamming-Abstand zwischen zwei Sequenzen.

    :param seq1: Erste Sequenz (z. B. String oder Liste).
    :param seq2: Zweite Sequenz (z. B. String oder Liste).
    :return: Hamming-Abstand (Anzahl der unterschiedlichen Positionen).
    """
    if len(seq1) != len(seq2):
        raise ValueError("Die beiden Sequenzen müssen gleich lang sein.")
    return sum(el1 != el2 for el1, el2 in zip(seq1, seq2))


def minimal_hamming_distance(codewords):
    """
    Berechnet den minimalen Hamming-Abstand in einer Menge von Codewörtern.

    :param codewords: Liste von Codewörtern (z. B. Strings oder Listen).
    :return: Minimaler Hamming-Abstand.
    """
    if len(codewords) < 2:
        raise ValueError("Es müssen mindestens zwei Codewörter vorhanden sein.")

    min_distance = float('inf')  # Startwert setzen

    # Vergleiche jedes Paar von Codewörtern
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            distance = hamming_distance(codewords[i], codewords[j])
            if distance < min_distance:
                min_distance = distance

    return min_distance


# Beispielanwendung
if __name__ == "__main__":
    # Beispiel-Codewörter
    codewords = [
        "1010101",
        "1001001",
        "1111111",
        "0000000"
    ]

    try:
        min_distance = minimal_hamming_distance(codewords)
        print(f"Minimaler Hamming-Abstand: {min_distance}")
    except ValueError as e:
        print(e)
