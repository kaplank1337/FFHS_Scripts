from sympy import symbols, Or, And, Not, Implies, to_dnf, to_cnf

def berechne_normalformen(logischer_ausdruck):
    """
    Berechnet die DNF und KNF eines logischen Ausdrucks.

    :param logischer_ausdruck: Ein sympy-Logik-Ausdruck
    :return: Ein Tuple (DNF, KNF)
    """
    dnf = to_dnf(logischer_ausdruck, simplify=True)
    knf = to_cnf(logischer_ausdruck, simplify=True)
    return dnf, knf

if __name__ == "__main__":
    # Variablen definieren
    A, B, C = symbols('A B C')

    # Logischen Ausdruck eingeben
    # Beispiel: (A ∨ B) → C
    ausdruck = Implies(Or(A, B), C)

    # Normalformen berechnen
    dnf, knf = berechne_normalformen(ausdruck)

    print("Logischer Ausdruck:", ausdruck)
    print("Disjunktive Normalform (DNF):", dnf)
    print("Konjunktive Normalform (KNF):", knf)
