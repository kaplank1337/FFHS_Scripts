import numpy as np

def is_subspace(predicate, vectors):
    """
    Prüft, ob eine Menge von Vektoren ein Unterraum von R^3 ist.

    :param predicate: Funktion, die eine Bedingung auf den Raum beschreibt.
    :param vectors: Liste von Vektoren, die getestet werden sollen.
    :return: True, wenn die Menge ein Unterraum ist, sonst False.
    """
    # 1. Nullvektor enthalten?
    if not predicate(np.array([0, 0, 0])):
        print("Die Menge enthält den Nullvektor nicht.")
        return False

    # 2. Abschluss unter Addition prüfen
    for v1 in vectors:
        for v2 in vectors:
            if not predicate(v1 + v2):
                print(f"Die Menge ist nicht abgeschlossen unter Addition: {v1} + {v2} nicht in Menge.")
                return False

    # 3. Abschluss unter Skalarmultiplikation prüfen
    for v in vectors:
        for scalar in [-1, 2]:  # Test mit ein paar Skalaren
            if not predicate(scalar * v):
                print(f"Die Menge ist nicht abgeschlossen unter Skalarmultiplikation: {scalar} * {v} nicht in Menge.")
                return False

    print("Die Menge erfüllt alle Unterraum-Eigenschaften.")
    return True

# Definition der Prädikate für die Mengen U1, U2 und U3
def U1_predicate(vector):
    x, y, z = vector
    return x + y + z == 0

def U2_predicate(vector):
    x, y, z = vector
    return x + y + z != 0

def U3_predicate(vector):
    x, y, z = vector
    return x + y + z <= 0

# Testvektoren (manuell anpassbar)
test_vectors = [
    np.array([1, -1, 0]),
    np.array([0, 1, -1]),
    np.array([-1, 0, 1])
]

# Überprüfung der drei Mengen
print("Überprüfung von U1:")
is_subspace(U1_predicate, test_vectors)

print("\nÜberprüfung von U2:")
is_subspace(U2_predicate, test_vectors)

print("\nÜberprüfung von U3:")
is_subspace(U3_predicate, test_vectors)
