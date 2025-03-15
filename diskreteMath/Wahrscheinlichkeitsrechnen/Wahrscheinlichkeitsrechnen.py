import math

def combinations(n, k):
    """
    Berechnet die Anzahl der Varianten (Kombinationen) von k Zügen aus n Kugeln ohne Zurücklegen.
    :param n: Gesamtanzahl der Kugeln
    :param k: Anzahl der zu ziehenden Kugeln
    :return: Anzahl der Kombinationen
    """
    if k > n:
        return 0  # Es können nicht mehr Kugeln gezogen werden als vorhanden
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

#Beispiel: Anzahl der Varianten bei 3 Zügen aus 6 Kugeln
# print(combinations(6, 3))  # Ausgabe: 20


def specificity(true_negatives, actual_negatives):
    """
    Berechnet die Spezifität.
    :param true_negatives: Anzahl der richtig negativen Fälle
    :param actual_negatives: Anzahl aller tatsächlichen negativen Fälle
    :return: Spezifität
    """
    return true_negatives / actual_negatives
# print(specificity(180, 200))  # Spezifität mit 180 von 200 erkannten Gesunden

def variations_with_replacement(n, k):
    """
    Berechnet die Anzahl der Varianten (Ziehen mit Zurücklegen und Berücksichtigung der Reihenfolge).
    :param n: Gesamtanzahl der Kugeln
    :param k: Anzahl der Züge
    :return: Anzahl der Varianten
    """
    return n ** k

# Beispiel: Anzahl der Varianten bei 3 Zügen aus 6 Kugeln
# print(variations_with_replacement(6, 3))  # Ausgabe: 216




def laplace_probability(favorable_cases, total_cases):
    """
    Berechnet die Laplace-Wahrscheinlichkeit.
    :param favorable_cases: Anzahl der günstigen Fälle
    :param total_cases: Anzahl der möglichen Fälle
    :return: Wahrscheinlichkeit
    """
    return favorable_cases / total_cases
# print(laplace_probability(1, 6))  # Würfel: Wahrscheinlichkeit für eine 6

def conditional_probability(P_A_and_B, P_B):
    """
    Berechnet die bedingte Wahrscheinlichkeit.
    :param P_A_and_B: Wahrscheinlichkeit von A und B
    :param P_B: Wahrscheinlichkeit von B
    :return: Bedingte Wahrscheinlichkeit
    """
    return P_A_and_B / P_B
# print(conditional_probability(0.3, 0.5))  # Beispielwerte für P(A ∩ B) und P(B)

def check_independence(P_A, P_B, P_A_and_B):
    """
    Prüft, ob zwei Ereignisse unabhängig sind.
    :param P_A: Wahrscheinlichkeit von A
    :param P_B: Wahrscheinlichkeit von B
    :param P_A_and_B: Wahrscheinlichkeit von A und B
    :return: True, wenn unabhängig, sonst False
    """
    return P_A_and_B == P_A * P_B
print(check_independence(0.5, 0.4, 0.2))  # Prüft Unabhängigkeit

def sensitivity(true_positives, actual_positives):
    """
    Berechnet die Sensitivität.
    :param true_positives: Anzahl der richtig positiven Fälle
    :param actual_positives: Anzahl aller tatsächlichen positiven Fälle
    :return: Sensitivität
    """
    return true_positives / actual_positives
# print(sensitivity(90, 100))  # Sensitivität mit 90 von 100 erkannten Fällen


def specificity(true_negatives, actual_negatives):
    """
    Berechnet die Spezifität.
    :param true_negatives: Anzahl der richtig negativen Fälle
    :param actual_negatives: Anzahl aller tatsächlichen negativen Fälle
    :return: Spezifität
    """
    return true_negatives / actual_negatives
# print(specificity(180, 200))  # Spezifität mit 180 von 200 erkannten Gesunden


def false_alarm_rate(specificity_value):
    """
    Berechnet die Fehlalarmrate.
    :param specificity_value: Spezifität
    :return: Fehlalarmrate
    """
    return 1 - specificity_value
# print(false_alarm_rate(0.9))  # Fehlalarmrate bei Spezifität von 0.9
