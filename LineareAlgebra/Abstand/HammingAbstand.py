def hamming_distance(seq1, seq2):
    """
    Berechnet den Hamming-Abstand zwischen zwei Sequenzen.

    :param seq1: Erste Sequenz (z. B. String oder Liste).
    :param seq2: Zweite Sequenz (z. B. String oder Liste).
    :return: Hamming-Abstand (Anzahl der unterschiedlichen Positionen).
    :raises ValueError: Wenn die Sequenzen nicht gleich lang sind.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Die beiden Sequenzen müssen gleich lang sein.")

    # Zähle die Positionen, an denen sich die beiden Sequenzen unterscheiden
    distance = sum(el1 != el2 for el1, el2 in zip(seq1, seq2))
    return distance


# Beispielanwendung
if __name__ == "__main__":
    # Zwei Bit-Strings
    bit_string1 = "1010101"
    bit_string2 = "1001001"

    # Berechne den Hamming-Abstand
    try:
        distance = hamming_distance(bit_string1, bit_string2)
        print(f"Hamming-Abstand: {distance}")
    except ValueError as e:
        print(e)

    # Zwei Listen
    list1 = [1, 0, 1, 0, 1, 0, 1]
    list2 = [1, 0, 0, 1, 0, 0, 1]

    # Berechne den Hamming-Abstand
    try:
        distance = hamming_distance(list1, list2)
        print(f"Hamming-Abstand: {distance}")
    except ValueError as e:
        print(e)
