from sympy import symbols, Or, And, Not, Implies, to_dnf, to_cnf
from sympy.parsing.sympy_parser import parse_expr

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
    print("Willkommen! Bitte logischen Ausdruck eingeben.")
    print("Verfügbare Operatoren:")
    print("  - ODER: | (z. B. A | B)")
    print("  - UND: & (z. B. A & B)")
    print("  - NICHT: ~ (z. B. ~A)")
    print("  - IMPLIKATION: >> (z. B. A >> B)")
    print("  - Variablen können Buchstaben wie A, B, C sein.")

    # Eingabe des logischen Ausdrucks als String
    ausdruck_string = input("Logischen Ausdruck eingeben: ")

    try:
        # Variablen erstellen (A-Z)
        variablen = symbols("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")

        # Ausdruck parsen
        ausdruck = parse_expr(ausdruck_string, local_dict={str(v): v for v in variablen})

        # DNF und KNF berechnen
        dnf, knf = berechne_normalformen(ausdruck)

        print("\nLogischer Ausdruck:", ausdruck)
        print("Disjunktive Normalform (DNF):", dnf)
        print("Konjunktive Normalform (KNF):", knf)
    except Exception as e:
        print("Fehler bei der Verarbeitung des Ausdrucks:", e)
