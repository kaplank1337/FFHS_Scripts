def determinante_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        print("Die Matrix muss 2x2 sein.")
        return None

    # Einzelne Elemente der Matrix extrahieren
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    print(f"Schritt 1: Extrahiere die Elemente a={a}, b={b}, c={c}, d={d}")
    print(f"Schritt 2: Berechne die Determinante als a*d - b*c")

    det = a * d - b * c

    print(f"Ergebnis: Determinante = {det}")
    return det


def determinante_3x3(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        print("Die Matrix muss 3x3 sein.")
        return None

    # Einzelne Elemente der Matrix extrahieren
    a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
    d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
    g, h, i = matrix[2][0], matrix[2][1], matrix[2][2]

    print(f"Schritt 1: Extrahiere die Elemente a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}, i={i}")
    print("Schritt 2: Berechne die Determinante mit der Formel:")
    print("det = a * (e*i - f*h) - b * (d*i - f*g) + c * (d*h - e*g)")

    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    print(f"Ergebnis: Determinante = {det}")
    return det


#matrix_2x2 = [[4, 3], [2, 1]]
#determinante_2x2(matrix_2x2)


# matrix_3x3 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
# determinante_3x3(matrix_3x3)

import numpy as np

# Definiere eine 3x3 Matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Definiere eine 3x4 Matrix B
B = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

#[]x,
# Matrix von B (3x4) und A (3x3), dies ist nicht möglich
try:
    C = np.dot(A, B)
    print("Das Ergebnis der Matrix A * B ist:")
    print(C)
except ValueError as e:
    print(f"Fehler bei der Matrix: {e}")

# # Matrix von B und A in der umgekehrten Reihenfolge
# C = np.dot(B, A)
# print("Das Ergebnis der Matrix B * A ist:")
# print(C)




# Funktion zur Matrix zweier Matrizen
def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Überprüfen, ob die Matrizen multipliziert werden können
    if cols_A != rows_B:
        raise ValueError("Die Anzahl der Spalten der ersten Matrix muss mit der Anzahl der Zeilen der zweiten Matrix übereinstimmen.")

    # Ergebnis-Matrix initialisieren
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Matrizenmultiplikation durchführen
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Funktion zur Matrix von drei Matrizen
def multiply_three_matrices(A, B, C):
    # Zuerst multiplizieren wir A und B
    result_AB = matrix_multiply(A, B)
    # Dann multiplizieren wir das Ergebnis mit C
    result_ABC = matrix_multiply(result_AB, C)
    return result_ABC

# Beispielmatrizen
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

C = [[9, 10],
     [11, 12]]

# Aufrufen der Funktion und Ergebnis anzeigen
result = multiply_three_matrices(A, B, C)

for row in result:
    print(row)




import numpy as np

# Definiere eine 3x3 Matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Definiere eine 3x4 Matrix B
B = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

#[]x,
# Matrix von B (3x4) und A (3x3), dies ist nicht möglich
try:
    C = np.dot(A, B)
    print("Das Ergebnis der Matrix A * B ist:")
    print(C)
except ValueError as e:
    print(f"Fehler bei der Matrix: {e}")

# # Matrix von B und A in der umgekehrten Reihenfolge
# C = np.dot(B, A)
# print("Das Ergebnis der Matrix B * A ist:")
# print(C)