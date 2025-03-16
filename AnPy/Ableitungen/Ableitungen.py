from sympy import symbols, diff, Function

def ableitung_berechnen(func_expr, variable, n):
    """
    Berechnet die n-te Ableitung einer Funktion.

    :param func_expr: Die Funktion als SymPy-Ausdruck.
    :param variable: Die Variable, nach der abgeleitet wird.
    :param n: Anzahl der Ableitungen.
    :return: n-te Ableitung der Funktion.
    """
    abgeleitet = func_expr
    for _ in range(n):
        abgeleitet = diff(abgeleitet, variable)
    return abgeleitet


# Variablen definieren
x = symbols('x')
g, h = symbols('g h', cls=Function)

# Funktion definieren
f = g(x) * h(x)

# Anzahl der Ableitungen
anzahl_ableitungen = 3

# Ableitungen berechnen
for i in range(1, anzahl_ableitungen + 1):
    result = ableitung_berechnen(f, x, i)
    print(f"{i}. Ableitung von f(x): {result}")
