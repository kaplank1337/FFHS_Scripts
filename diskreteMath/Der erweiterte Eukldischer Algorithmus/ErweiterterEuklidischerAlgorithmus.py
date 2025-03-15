def erweiterter_euklid(a, b):
    """
    Führt den erweiterten euklidischen Algorithmus durch.
    Gibt die Schritte und das Ergebnis im gewünschten Stil aus.

    :param a: Erste Zahl
    :param b: Zweite Zahl
    :return: Tupel (ggT, x, y), wobei x und y die Koeffizienten sind, die die Linearkombination ergeben.
    """
    print(f"Eingabe: a = {a}, b = {b}\n")

    # Speichern der Zwischenschritte
    steps = []

    # Initialisierung der Variablen
    original_a, original_b = a, b
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b  # Ganzzahliger Quotient
        r = a % b
        steps.append((a, b, q, r))
        a, b = b, r

        # Update der Koeffizienten
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    # Der ggT ist der letzte Wert von a (vor der letzten Iteration)
    ggT = a

    # Ausgabe der Zwischenschritte
    print("Zwischenschritte:")
    for step in steps:
        print(f"{step[0]} = {step[2]} ⋅ {step[1]} + {step[3]}")

    print("\nRücksubstitution:")

    # Rücksubstitution für Linearkombination
    s, t = x0, y0
    for i in range(len(steps) - 1, -1, -1):
        a, b, q, r = steps[i]
        if i > 0:
            prev_a, prev_b, _, _ = steps[i - 1]
            print(f"{r} = {prev_a} - {q} ⋅ {prev_b}")
        else:
            print(f"{r} = {original_a} - {q} ⋅ {original_b}")

    # Ausgabe der Linearkombination
    print(f"\nLinearkombination: {ggT} = {s} ⋅ {original_a} + {t} ⋅ {original_b}")

    print(f"\nErgebnis: ggT = {ggT}")
    return ggT, s, t

# Beispielzahlen zur Eingabe
a = 128
b = 34

# Algorithmus ausführen
erweiterter_euklid(a, b)
