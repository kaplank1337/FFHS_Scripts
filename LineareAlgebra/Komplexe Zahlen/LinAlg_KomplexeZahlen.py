# Funktion zur Addition komplexer Zahlen
#Beispiel: (2+3i) + (4 + 5i)
#a_real = 2  # Realteil der ersten Zahl
#a_imag = 3  # Imaginärteil der ersten Zahl
#b_real = 4  # Realteil der zweiten Zahl
#b_imag = 5  # Imaginärteil der zweiten Zahl
def add_complex_numbers(a_real, a_imag, b_real, b_imag):
    """
    Addiert zwei komplexe Zahlen (a_real + a_imag*i) und (b_real + b_imag*i).
    Gibt eine Erklärung zu jedem Schritt zurück.
    """
    explanation = []

    # Eingabe der ersten komplexen Zahl
    explanation.append(f"Die erste Zahl ist: {a_real} + {a_imag}i")

    # Eingabe der zweiten komplexen Zahl
    explanation.append(f"Die zweite Zahl ist: {b_real} + {b_imag}i")

    # Addition der Realteile
    real_part = a_real + b_real
    explanation.append(f"1. Addiere die Realteile: {a_real} + {b_real} = {real_part}")

    # Addition der Imaginärteile
    imag_part = a_imag + b_imag
    explanation.append(f"2. Addiere die Imaginärteile: {a_imag} + {b_imag} = {imag_part}")

    # Ergebnis darstellen
    explanation.append(f"Das Ergebnis der Addition ist: {real_part} + {imag_part}i")

    return explanation


# Funktion zur Matrix komplexer Zahlen
def multiply_complex_numbers(a_real, a_imag, b_real, b_imag):
    """
    Multipliziert zwei komplexe Zahlen (a_real + a_imag*i) und (b_real + b_imag*i).
    Gibt eine Erklärung zu jedem Schritt zurück.
    """
    explanation = []

    # Eingabe der ersten komplexen Zahl
    explanation.append(f"Die erste Zahl ist: {a_real} + {a_imag}i")

    # Eingabe der zweiten komplexen Zahl
    explanation.append(f"Die zweite Zahl ist: {b_real} + {b_imag}i")

    # Berechnung der Realteile
    real_part = (a_real * b_real) - (a_imag * b_imag)
    explanation.append(f"1. Berechne den Realteil: ({a_real} * {b_real}) - ({a_imag} * {b_imag}) = {real_part}")

    # Berechnung der Imaginärteile
    imag_part = (a_real * b_imag) + (a_imag * b_real)
    explanation.append(f"2. Berechne den Imaginärteil: ({a_real} * {b_imag}) + ({a_imag} * {b_real}) = {imag_part}")

    # Ergebnis darstellen
    explanation.append(f"Das Ergebnis der Multiplikation ist: {real_part} + {imag_part}i")

    return explanation

# Funktion zur Division komplexer Zahlen
def divide_complex_numbers(a_real, a_imag, b_real, b_imag):
    """
    Dividiert zwei komplexe Zahlen (a_real + a_imag*i) und (b_real + b_imag*i).
    Gibt eine Erklärung zu jedem Schritt zurück.
    """
    explanation = []

    # Eingabe der ersten komplexen Zahl (Zähler)
    explanation.append(f"Die erste Zahl (Zähler) ist: {a_real} + {a_imag}i")

    # Eingabe der zweiten komplexen Zahl (Nenner)
    explanation.append(f"Die zweite Zahl (Nenner) ist: {b_real} + {b_imag}i")

    # Berechnung des Konjugierten des Nenners
    conjugate_real = b_real
    conjugate_imag = -b_imag
    explanation.append(f"Das konjugierte des Nenners ist: {conjugate_real} + {conjugate_imag}i")

    # Matrix von Zähler und konjugiertem Nenner
    numerator_real = (a_real * conjugate_real) - (a_imag * conjugate_imag)
    numerator_imag = (a_real * conjugate_imag) + (a_imag * conjugate_real)
    explanation.append(f"Zähler nach Multiplikation mit dem Konjugierten des Nenners: "
                       f"({a_real} * {conjugate_real}) - ({a_imag} * {conjugate_imag}) = {numerator_real}, "
                       f"({a_real} * {conjugate_imag}) + ({a_imag} * {conjugate_real}) = {numerator_imag}")

    # Berechnung des quadrierten Betrags des Nenners
    denominator = (b_real**2 + b_imag**2)
    explanation.append(f"Der quadrierte Betrag des Nenners ist: {b_real}^2 + {b_imag}^2 = {denominator}")

    # Division
    real_part = numerator_real / denominator
    imag_part = numerator_imag / denominator
    explanation.append(f"Die Real- und Imaginärteile nach Division: {numerator_real} / {denominator} = {real_part}, "
                       f"{numerator_imag} / {denominator} = {imag_part}")

    # Ergebnis
    explanation.append(f"Das Ergebnis der Division ist: {real_part} + {imag_part}i")

    return explanation

# Funktion zur Lösung der Aufgabe
def task_addition_und_BruchstrichUeberKlammer(a1_real, a1_imag, a2_real, a2_imag):
    """
    Löse die Aufgabe:
    ((a1 + b1i) + (a2 + b2i)) / (a1 + b1i)  Beispiel mit
    a_real = 2  # Realteil der ersten Zahl
    a_imag = 3  # Imaginärteil der ersten Zahl Lösung = 2a
    """
    explanation = []

    # Schritt 1: Addiere die beiden komplexen Zahlen
    real_sum = a1_real + a2_real
    imag_sum = a1_imag + a2_imag
    explanation.append(f"1. Addiere die beiden komplexen Zahlen (a1 + b1i) + (a2 + b2i):")
    explanation.append(f"   Realteil: {a1_real} + {a2_real} = {real_sum}")
    explanation.append(f"   Imaginärteil: {a1_imag} + {a2_imag} = {imag_sum}")
    explanation.append(f"   Ergebnis der Addition: {real_sum} + {imag_sum}i")

    # Schritt 2: Berechne die Division: (Ergebnis der Addition) / (a1 + b1i)
    conjugate_real = a1_real
    conjugate_imag = -a1_imag
    explanation.append(f"2. Berechne die Division:")
    explanation.append(f"   Konjugiertes des Nenners: {conjugate_real} + {conjugate_imag}i")

    # Zähler mit konjugiertem Nenner multiplizieren
    numerator_real = (real_sum * conjugate_real) - (imag_sum * conjugate_imag)
    numerator_imag = (real_sum * conjugate_imag) + (imag_sum * conjugate_real)
    explanation.append(f"   Multipliziere den Zähler mit dem konjugierten Nenner:")
    explanation.append(f"   Realteil: ({real_sum} * {conjugate_real}) - ({imag_sum} * {conjugate_imag}) = {numerator_real}")
    explanation.append(f"   Imaginärteil: ({real_sum} * {conjugate_imag}) + ({imag_sum} * {conjugate_real}) = {numerator_imag}")

    # Berechnung des quadrierten Betrags des Nenners
    denominator = (a1_real**2 + a1_imag**2)
    explanation.append(f"   Quadrierter Betrag des Nenners: {a1_real}^2 + {a1_imag}^2 = {denominator}")

    # Division durchführen
    result_real = numerator_real / denominator
    result_imag = numerator_imag / denominator
    explanation.append(f"   Ergebnis der Division:")
    explanation.append(f"   Realteil: {numerator_real} / {denominator} = {result_real}")
    explanation.append(f"   Imaginärteil: {numerator_imag} / {denominator} = {result_imag}")

    # Endergebnis
    explanation.append(f"3. Das Ergebnis der Aufgabe ist: {result_real} + {result_imag}i")

    return explanation

# Funktion zur Subtraktion komplexer Zahlen
def subtract_complex_numbers(a_real, a_imag, b_real, b_imag):
    """
    Subtrahiert zwei komplexe Zahlen (a_real + a_imag*i) und (b_real + b_imag*i).
    Gibt eine Erklärung zu jedem Schritt zurück.
    """
    explanation = []

    # Eingabe der ersten komplexen Zahl
    explanation.append(f"Die erste Zahl ist: {a_real} + {a_imag}i")

    # Eingabe der zweiten komplexen Zahl
    explanation.append(f"Die zweite Zahl ist: {b_real} + {b_imag}i")

    # Subtraktion der Realteile
    real_part = a_real - b_real
    explanation.append(f"1. Subtrahiere die Realteile: {a_real} - {b_real} = {real_part}")

    # Subtraktion der Imaginärteile
    imag_part = a_imag - b_imag
    explanation.append(f"2. Subtrahiere die Imaginärteile: {a_imag} - {b_imag} = {imag_part}")

    # Ergebnis darstellen
    explanation.append(f"Das Ergebnis der Subtraktion ist: {real_part} + {imag_part}i")

    return explanation

# Funktion zur Berechnung des Betrags einer komplexen Zahl
def modulus_complex_number(a_real, a_imag):
    """
    Berechnet den Betrag einer komplexen Zahl (a_real + a_imag*i).
    Gibt eine Erklärung zu jedem Schritt zurück.
    """
    explanation = []

    # Eingabe der komplexen Zahl
    explanation.append(f"Die komplexe Zahl ist: {a_real} + {a_imag}i")

    # Berechnung der Quadrate der Real- und Imaginärteile
    real_square = a_real**2
    imag_square = a_imag**2
    explanation.append(f"1. Quadriere den Realteil: {a_real}^2 = {real_square}")
    explanation.append(f"2. Quadriere den Imaginärteil: {a_imag}^2 = {imag_square}")

    # Berechnung der Summe der Quadrate
    sum_squares = real_square + imag_square
    explanation.append(f"3. Addiere die Quadrate: {real_square} + {imag_square} = {sum_squares}")

    # Berechnung der Quadratwurzel
    modulus = sum_squares**0.5
    explanation.append(f"4. Ziehe die Quadratwurzel: sqrt({sum_squares}) = {modulus}")

    # Ergebnis
    explanation.append(f"Der Betrag der komplexen Zahl ist: {modulus}")

    return explanation


# Beispiel: Zwei komplexe Zahlen addieren
a_real = 12  # Realteil der ersten Zahl
a_imag = 5 # Imaginärteil der ersten Zahl
b_real = 2  # Realteil der zweiten Zahl
b_imag = 3  # Imaginärteil der zweiten Zahl

# Addition
# print("Addition der komplexen Zahlen:")
# steps_add = add_complex_numbers(a_real, a_imag, b_real, b_imag)
# for step in steps_add:
#     print(step)

# # Matrix
# print("\nMultiplikation der komplexen Zahlen:")
# steps_multiply = multiply_complex_numbers(a_real, a_imag, b_real, b_imag)
# for step in steps_multiply:
#     print(step)


# # Division
# print("\nDivision der komplexen Zahlen:")
# steps_divide = divide_complex_numbers(a_real, a_imag, b_real, b_imag)
# for step in steps_divide:
#     print(step)

# # Addition mit Bruchstrich über den zweiten
# steps_task = task_addition_und_BruchstrichUeberKlammer(a_real, a_imag, a_real, a_imag)
# for step in steps_task:
#     print(step)

# # Subtraktion mit Bruchstrich über den zweiten
# print("\nSubtraktion der komplexen Zahlen:")
# steps_subtract = subtract_complex_numbers(a_real, a_imag, b_real, b_imag)
# for step in steps_subtract:
#     print(step)

# # Betrag berechnen
# print("\nBetrag der komplexen Zahl:")
# steps_modulus = modulus_complex_number(a_real, a_imag)
# for step in steps_modulus:
#     print(step)