import numpy as np

# Funktion zur Berechnung der Determinante mit Ausgabe der Schritte
def determinant(matrix, level=0):
    n = len(matrix)
    indent = "  " * level  # Einrückung für die Ausgabe, um die Rekursionstiefe zu visualisieren

    # Basisfall für eine 2x2 Matrix
    if n == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        print(f"{indent}Basisfall 2x2: det = {det}")
        return det

    det = 0
    for col in range(n):
        # Berechne die Determinante mit Laplace-Entwicklung
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        cofactor = ((-1) ** col) * matrix[0][col]
        sub_det = determinant(minor, level + 1)
        term = cofactor * sub_det
        det += term
        print(f"{indent}Spalte {col}: Cofactor = {cofactor}, Subdeterminante = {sub_det}, Term = {term}")

    print(f"{indent}Determinante auf Level {level}: {det}")
    return det

# Funktion zur Überprüfung der Invertierbarkeit einer Matrix
def is_invertible(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        print("Die Matrix ist nicht quadratisch und kann daher nicht invertiert werden.")
        return False

    # Berechne die Determinante und überprüfe sie
    det = determinant(matrix.tolist())
    if det == 0:
        print("Die Matrix ist quadratisch, aber die Determinante ist null.")
        print("Dies bedeutet, dass die Matrix singulär ist und keine Inverse existiert.")
        return False

    print("Die Matrix ist quadratisch und hat eine Determinante ungleich null.")
    print("Die Matrix ist somit invertierbar.")
    return True

# Funktion zur Berechnung der Inversen mit Ausgabe der Schritte
def inverse(matrix):
    if not is_invertible(matrix):
        raise ValueError("Die Matrix erfüllt nicht die Voraussetzungen für eine Inversion.")

    n = len(matrix)
    print("\nErweiterte Matrix erstellen:")
    aug_matrix = np.hstack((matrix, np.eye(n)))
    print(aug_matrix)

    # Gauß-Jordan-Elimination
    for i in range(n):
        pivot = aug_matrix[i][i]
        if pivot == 0:
            for j in range(i + 1, n):
                if aug_matrix[j][i] != 0:
                    aug_matrix[[i, j]] = aug_matrix[[j, i]]
                    print(f"Zeile {i} und Zeile {j} vertauschen, da Pivot = 0:")
                    print(aug_matrix)
                    pivot = aug_matrix[i][i]
                    break
            if pivot == 0:
                raise ValueError("Matrix ist singulär und hat keine Inverse.")

        aug_matrix[i] = aug_matrix[i] / pivot
        print(f"Zeile {i} durch Pivot {pivot} teilen, um das Pivot-Element zu 1 zu machen:")
        print(aug_matrix)

        for j in range(n):
            if i != j:
                factor = aug_matrix[j][i]
                aug_matrix[j] -= aug_matrix[i] * factor
                print(f"Zeile {j} aktualisieren: Zeile {j} - ({factor}) * Zeile {i}")
                print(aug_matrix)

    inverse_matrix = aug_matrix[:, n:]
    print("Die Inverse der Matrix ist:")
    print(inverse_matrix)
    return inverse_matrix

##Polynome
# Beispielmengen von Polynomen
def polynome_grad_genau_n(n):
    """Erstellt eine Menge von Polynomen vom Grad genau n."""
    return [
        lambda x: 3*x**n + 2*x + 1,
        lambda x: -x**n + 4*x - 5,
        lambda x: 0.5*x**n - 3*x + 2
    ]

def polynome_grad_hoechstens_n(n):
    """Erstellt eine Menge von Polynomen vom Grad höchstens n."""
    return [
        lambda x: x**n + x + 1,
        lambda x: 2*x + 3,
        lambda x: 5,
        lambda x: 3*x**n - x + 2
    ]

# Funktion zur Überprüfung der Vektorraumeigenschaften
def ist_vektorraum(menge, grad_genau_n=False, n=None):
    """Überprüft, ob eine gegebene Menge von Polynomen die Vektorraumeigenschaften erfüllt."""
    # Überprüfung der Nullvektor-Bedingung (Existenz des Nullpolynoms)
    nullpolynom = lambda x: 0
    null_in_menge = any(all(p(x) == 0 for x in range(-10, 11)) for p in menge)

    if not null_in_menge:
        print("Die Menge enthält das Nullpolynom nicht und ist daher kein Vektorraum.")
        return False

    # Überprüfung der Abgeschlossenheit unter Addition
    for i in range(len(menge)):
        for j in range(i, len(menge)):
            p = menge[i]
            q = menge[j]
            summe = lambda x: p(x) + q(x)

            # Überprüfe den Grad der Summe
            if grad_genau_n and n is not None:
                max_grad = max([summe(x) != 0 for x in range(-10, 11)])
                if max_grad != n:
                    print("Die Menge ist unter Addition nicht abgeschlossen, da die Summe zweier Polynome nicht immer den Grad n hat.")
                    return False

    # Überprüfung der Abgeschlossenheit unter Skalarmultiplikation
    skalar = 2
    for p in menge:
        skalarprodukt = lambda x: skalar * p(x)

        # Überprüfe den Grad des Skalarprodukts
        if grad_genau_n and n is not None:
            max_grad = max([skalarprodukt(x) != 0 for x in range(-10, 11)])
            if max_grad != n:
                print("Die Menge ist unter Skalarmultiplikation nicht abgeschlossen, da das Skalarprodukt nicht immer den Grad n hat.")
                return False

    print("Die Menge erfüllt alle Vektorraumeigenschaften und ist daher ein Vektorraum.")
    return True

from itertools import combinations

def hamming_distance(code1, code2):
    """Berechnet die Hamming-Distanz zwischen zwei Codewörtern."""
    return sum(c1 != c2 for c1, c2 in zip(code1, code2))

def minimalabstand(codes):
    """Berechnet den Minimalabstand und gibt die Hamming-Distanzen aller Paare aus."""
    hamming_distanzen = []

    # Berechne die Hamming-Distanzen für alle Paare von Codewörtern
    for code1, code2 in combinations(codes, 2):
        dist = hamming_distance(code1, code2)
        hamming_distanzen.append(dist)
        print(f"Hamming-Distanz zwischen {code1} und {code2}: {dist}")

    # Finde den Minimalabstand
    minimal_distanz = min(hamming_distanzen)
    print(f"\nMinimalabstand des Codes: {minimal_distanz}")
    return minimal_distanz

def ist_linearer_code(codes):
    # Prüfe, ob das Nullwort (z.B. "00000") in der Liste ist
    nullwort = "0" * len(codes[0])
    if nullwort not in codes:
        print("Der Code enthält das Nullwort nicht und ist daher kein linearer Code.")
        return False
    print("Das Nullwort ist enthalten.")

    # Überprüfe die Abgeschlossenheit unter der XOR-Operation
    for code1, code2 in combinations(codes, 2):
        # XOR-Operation zwischen den beiden Codewörtern
        xor_result = "".join("1" if bit1 != bit2 else "0" for bit1, bit2 in zip(code1, code2))
        if xor_result not in codes:
            print(f"Der Code ist nicht abgeschlossen unter der Addition: {code1} XOR {code2} = {xor_result} ist nicht im Code.")
            return False
        print(f"{code1} XOR {code2} = {xor_result} (ist im Code)")

    print("Der Code erfüllt alle Voraussetzungen für einen linearen Code.")
    return True

def xor_binary_strings(a, b):
    """Führt bitweises XOR für zwei Binärstrings gleicher Länge aus."""
    return ''.join('1' if bit_a != bit_b else '0' for bit_a, bit_b in zip(a, b))

def ist_unabhaengig(codewort, basis):
    """Prüft, ob ein Codewort durch eine XOR-Kombination der Basisvektoren darstellbar ist."""
    for r in range(1, len(basis) + 1):
        for kombination in combinations(basis, r):
            xor_result = kombination[0]
            for vec in kombination[1:]:
                xor_result = xor_binary_strings(xor_result, vec)
            if xor_result == codewort:
                return False
    return True

def finde_basis(codes):
    """Findet die Basis eines linearen Codes."""
    # Nullwort entfernen, wenn es existiert
    nullwort = '0' * len(codes[0])
    codes = [code for code in codes if code != nullwort]

    basis = []
    for codewort in codes:
        if ist_unabhaengig(codewort, basis):
            basis.append(codewort)

    return basis

def xor_binary_strings(a, b):
    """Führt eine bitweise XOR-Operation auf zwei Binärstrings gleicher Länge aus."""
    return ''.join('1' if bit_a != bit_b else '0' for bit_a, bit_b in zip(a, b))

def generate_subspace(vectors):
    """Erzeugt den Unterraum durch alle möglichen XOR-Kombinationen der gegebenen Vektoren."""
    subspace = set()  # Verwende ein Set, um doppelte Kombinationen zu vermeiden
    subspace.add('0000')  # Nullwort ist immer Teil des Unterraums
    print("Start: Nullwort (0000) ist im Unterraum C enthalten")

    # Führe XOR-Operationen auf alle möglichen Kombinationen von Vektoren durch
    for r in range(1, len(vectors) + 1):
        for combination in combinations(vectors, r):
            xor_result = combination[0]
            print(f"\nKombination: {' XOR '.join(combination)}")
            for vec in combination[1:]:
                xor_result = xor_binary_strings(xor_result, vec)
                print(f"  XOR mit {vec}: {xor_result}")
            subspace.add(xor_result)
            print(f"Ergebnis dieser Kombination: {xor_result} (im Unterraum C)")

    return sorted(subspace)

def matrix_rank(matrix):
    """Berechnet den Rang einer Matrix und gibt alle Schritte zur Berechnung aus."""
    # Konvertiere die Eingabe in ein numpy Array für einfachere Manipulation
    mat = np.array(matrix, dtype=float)
    (rows, cols) = mat.shape

    print("Startmatrix:")
    print(mat)
    print("\nGauss-Jordan-Eliminationsverfahren, um die Matrix in Zeilenstufenform zu bringen:")

    rank = 0  # Der Rang beginnt bei 0 und wird mit jeder Pivotzeile erhöht

    for col in range(cols):
        # Suche nach dem Pivot in der aktuellen Spalte
        pivot_row = None
        for row in range(rank, rows):
            if mat[row, col] != 0:
                pivot_row = row
                break

        # Falls kein Pivot gefunden wurde, gehe zur nächsten Spalte
        if pivot_row is None:
            continue

        # Vertausche die Pivotzeile nach oben, falls nötig
        if pivot_row != rank:
            mat[[rank, pivot_row]] = mat[[pivot_row, rank]]
            print(f"\nZeilen {rank} und {pivot_row} vertauschen, um das Pivot-Element nach oben zu bringen:")
            print(mat)

        # Normalisiere die Pivotzeile, sodass das Pivot-Element 1 wird
        pivot_value = mat[rank, col]
        mat[rank] = mat[rank] / pivot_value
        print(f"\nZeile {rank} durch das Pivot-Element {pivot_value} teilen, um 1 als Pivot zu erhalten:")
        print(mat)

        # Setze alle anderen Einträge in der Pivotspalte auf 0
        for row in range(rows):
            if row != rank:
                factor = mat[row, col]
                mat[row] -= factor * mat[rank]
                print(f"\nZeile {row} - ({factor}) * Zeile {rank} (um 0 in Spalte {col} zu setzen):")
                print(mat)

        # Erhöhe den Rang, da wir eine neue Pivotzeile gefunden haben
        rank += 1

    print("\nEndmatrix in Zeilenstufenform:")
    print(mat)
    print(f"\nDer Rang der Matrix ist: {rank}")

    return rank

def generatormatrix_from_checkmatrix(H):
    """
    Berechnet die Generatormatrix G aus der gegebenen Prüfmatrix H.

    Die Prüfmatrix H muss in der Form [I | P] vorliegen, wobei I eine Identitätsmatrix ist.

    Parameter:
    H (numpy.array): Die Prüfmatrix des Codes.

    Rückgabewert:
    G (numpy.array): Die berechnete Generatormatrix des Codes.
    """
    # Anzahl der Zeilen und Spalten von H
    rows, cols = H.shape

    # Die Anzahl der Spalten von I ist gleich der Anzahl der Zeilen von H
    # Wir nehmen an, dass H die Form [I | P] hat
    I_n_k = H[:, :rows]  # Linker Teil von H (Identitätsmatrix)
    P = H[:, rows:]      # Rechter Teil von H

    # Überprüfen, ob der linke Teil von H eine Identitätsmatrix ist
    if not np.array_equal(I_n_k, np.eye(rows)):
        raise ValueError("Die linke Seite der Prüfmatrix H ist keine Identitätsmatrix. Überprüfen Sie die Eingabe.")

    # Die Generatormatrix G ist gegeben durch [P^T | I_k]
    P_T = P.T  # Transponiere P
    I_k = np.eye(cols - rows)  # Erzeuge eine Identitätsmatrix der Größe (cols - rows)
    G = np.hstack((P_T, I_k))  # Zusammenfügen von [P^T | I_k]

    print("Prüfmatrix H:")
    print(H)
    print("\nTransponierte von P (P^T):")
    print(P_T)
    print("\nIdentitätsmatrix I_k:")
    print(I_k)
    print("\nGeneratormatrix G:")
    print(G)

    return G

def calculate_redundant_bits(data_bits):
    """Berechnet die Anzahl der benötigten Redundanzbits."""
    m = len(data_bits)
    for r in range(m):
        if (2**r) >= m + r + 1:
            return r
    return 0

def generate_hamming_code(data_bits):
    """Generiert ein Hamming-Codewort mit den gegebenen Datenbits."""
    m = len(data_bits)
    r = calculate_redundant_bits(data_bits)
    codeword = ['0'] * (m + r)

    # Setze die Datenbits in das Codewort (alle Positionen, die keine Potenzen von 2 sind)
    j = 0
    for i in range(1, len(codeword) + 1):
        if not (i & (i - 1)) == 0:  # Nicht-Potenz von 2
            codeword[i - 1] = data_bits[j]
            j += 1

    # Berechne die Redundanzbits
    for i in range(r):
        position = 2 ** i
        codeword[position - 1] = calculate_parity_bit(codeword, position)

    return ''.join(codeword)

def calculate_parity_bit(codeword, position):
    """Berechnet ein einzelnes Paritätsbit an der gegebenen Position."""
    parity = 0
    for i in range(position - 1, len(codeword), 2 * position):
        for j in range(i, i + position):
            if j < len(codeword) and codeword[j] == '1':
                parity ^= 1
    return str(parity)

def detect_and_correct_error(received_code):
    """Erkennt und korrigiert einen 1-Bit-Fehler im erhaltenen Hamming-Codewort."""
    n = len(received_code)
    error_position = 0

    # Berechnung der Paritätsbits und Fehlerposition
    for i in range(int(np.log2(n)) + 1):
        position = 2 ** i
        parity = calculate_parity_bit(received_code, position)
        if parity == '1':
            error_position += position

    # Ausgabe des Fehlerstatus
    if error_position == 0:
        print("Kein Fehler im Codewort.")
    else:
        print(f"Fehler an Position {error_position} erkannt.")
        # Fehlerkorrektur durch Umkippen des fehlerhaften Bits
        corrected_code = list(received_code)
        corrected_code[error_position - 1] = '1' if received_code[error_position - 1] == '0' else '0'
        print("Korrigiertes Codewort:", ''.join(corrected_code))
        return ''.join(corrected_code)


# Beispiel: Eingabe der Codes (kann angepasst werden)
codes = [
    "1100",
    "0011",
    "0110",
    "1001"
]

# Definieren der Matrix A
A = np.array([
    [1, 5, -1],
    [1, 4, -1],
    [2, 2, -1]
], dtype=float)

# #Berechnung des Minimalabstands und der Hamming-Distanzen
 minimalabstand(codes)

# # Überprüfe, ob die gegebene Menge ein linearer Code ist
# ist_linearer_code(codes)

# # Berechnung der Inversen einer Matrix
# print("Überprüfung der Matrix A auf Invertierbarkeit und Berechnung der Inversen:")
# inverse_A = inverse(A)

# # Berechnung der Basis
# basis = finde_basis(codes)
# print("Basis des Codes:", basis)


# # Berechnung des Unterraums C
# subspace = generate_subspace(codes)
# print("\nElemente des Unterraums C:")
# print(subspace)


# # Berechnung Rang einer Matrix
# matrix_rank(A)


# # Beispiel: Prüfmatrix H
H = np.array([
 [1, 0, 1],
 [0, 1, 1]
], dtype=int)
#
# # Berechnung der Generatormatrix G
G = generatormatrix_from_checkmatrix(H)

# # Beispiel zur Verwendung Hamming Codes
# data_bits = '1011'  # Beispiel-Datenbits
# hamming_code = generate_hamming_code(data_bits)
# print("Hamming-Codewort:", hamming_code)

# Beispiel zur Verwendung
received_code = '1100101'
detect_and_correct_error(received_code)