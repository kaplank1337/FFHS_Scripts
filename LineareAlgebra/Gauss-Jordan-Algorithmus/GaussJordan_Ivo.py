def gauss_elimination(A, b):
    """
    Führt das Gaußsche Eliminationsverfahren zur Lösung eines linearen Gleichungssystems Ax = b durch.

    :param A: Koeffizientenmatrix (2D-Liste oder numpy-Array)
    :param b: rechte Seite (1D-Liste oder numpy-Array)
    :return: Lösung des Gleichungssystems als Liste oder Meldung bei Inkonsistenz
    """
    import numpy as np

    # Kombiniere A und b zu einer erweiterten Matrix
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    augmented_matrix = np.hstack((A, b))

    n = len(b)  # Anzahl der Zeilen

    print("\nSchritt 1: Start der Gauß-Elimination")
    print("Erweiterte Matrix:")
    print(augmented_matrix)

    # Vorwärtssubstitution (Dreiecksform)
    for i in range(n):
        print(f"\nSchritt 2.{i + 1}: Verarbeitung der Zeile {i + 1}")

        # Pivotisierung: Tausche Zeilen, wenn das Pivot-Element Null ist
        if augmented_matrix[i, i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    print(f"Zeilen {i + 1} und {j + 1} wurden getauscht:")
                    print(augmented_matrix)
                    break

        # Prüfe auf Inkonsistenz (Zeile mit nur Nullen außer der erweiterten Spalte)
        if np.all(augmented_matrix[i, :-1] == 0) and augmented_matrix[i, -1] != 0:
            print("\nDas Gleichungssystem ist inkonsistent. Keine Lösung vorhanden.")
            return None

        # Normiere die Pivot-Zeile
        pivot = augmented_matrix[i, i]
        if pivot != 0:
            augmented_matrix[i] = augmented_matrix[i] / pivot
            print(f"Pivot-Zeile {i + 1} normiert:")
            print(augmented_matrix)

        # Eliminiere die Einträge unterhalb des Pivots
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j] -= factor * augmented_matrix[i]
            print(f"Eliminierung in Zeile {j + 1} mit Faktor {factor}:")
            print(augmented_matrix)

    print("\nSchritt 3: Vorwärtssubstitution abgeschlossen")
    print("Dreiecksform der Matrix:")
    print(augmented_matrix)

    # Rückwärtssubstitution (Berechnung der Lösung)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:n], x[i + 1:n])
        print(f"Rückwärtssubstitution für x[{i + 1}]: {x[i]}")

    return x

def main():
    print("Gaußsches Eliminationsverfahren zur Lösung von Ax = b")

    try:
        # Eingabe der Koeffizientenmatrix A
        n = int(input("Geben Sie die Dimension der quadratischen Matrix A ein: "))
        print("Geben Sie die Elemente der Matrix A zeilenweise ein:")
        A = []
        for i in range(n):
            row = list(map(float, input(f"Zeile {i + 1}: ").split()))
            if len(row) != n:
                raise ValueError("Die Matrix A muss quadratisch sein!")
            A.append(row)

        # Eingabe der rechten Seite b
        print("Geben Sie die Elemente des Vektors b ein (getrennt durch Leerzeichen):")
        b = list(map(float, input().split()))
        if len(b) != n:
            raise ValueError("Der Vektor b muss die gleiche Anzahl von Einträgen wie die Dimension der Matrix A haben!")

        # Gauß-Elimination durchführen
        x = gauss_elimination(A, b)

        # Ergebnis ausgeben
        if x is not None:
            print("\nLösung des Gleichungssystems (x):")
            print(x)

    except ValueError as e:
        print(f"Fehler: {e}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()