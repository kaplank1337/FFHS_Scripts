def fermat_test_dynamic(base, power, divisor, constant):
    """
    Dynamischer Test mit dem kleinen Satz von Fermat.
    Prüft, ob divisor ein Teiler von base^power + constant ist.
    Gibt den Rechenweg dynamisch zurück.
    """
    rechenweg = []

    # Prüfen, ob der Divisor eine Primzahl ist
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not is_prime(divisor):
        rechenweg.append(f"1. {divisor} ist keine Primzahl, der kleine Satz von Fermat ist nicht anwendbar.")
        return "\n".join(rechenweg)

    rechenweg.append(f"1. Prüfen, ob {divisor} eine Primzahl ist: Ja, {divisor} ist eine Primzahl.")

    # Kleiner Satz von Fermat
    rechenweg.append(f"2. Kleiner Satz von Fermat: {base}^({divisor}-1) ≡ 1 (mod {divisor})")
    rechenweg.append(f"   {base}^({divisor-1}) ≡ 1 (mod {divisor}).")

    # Modulo-Reduktion des Exponenten
    reduced_exponent = power % (divisor - 1)
    rechenweg.append(f"3. Reduziere den Exponenten {power} modulo {divisor-1} (da {divisor}-1={divisor-1}):")
    rechenweg.append(f"   {power} % {divisor-1} = {reduced_exponent}.")

    # Modulo-Berechnung
    fermat_result = pow(base, reduced_exponent, divisor)
    rechenweg.append(f"4. Berechne {base}^{reduced_exponent} mod {divisor}:")
    rechenweg.append(f"   {base}^{reduced_exponent} ≡ {fermat_result} (mod {divisor}).")

    # Prüfen, ob base^power + constant durch divisor teilbar ist
    result = (fermat_result + constant) % divisor
    rechenweg.append(f"5. Prüfe, ob ({base}^{power} + {constant}) mod {divisor} = 0:")
    rechenweg.append(f"   ({fermat_result} + {constant}) mod {divisor} = {result}.")

    if result == 0:
        rechenweg.append(f"Ergebnis: Ja, {divisor} ist ein Teiler von {base}^{power} + {constant}.")
    else:
        rechenweg.append(f"Ergebnis: Nein, {divisor} ist kein Teiler von {base}^{power} + {constant}.")

    return "\n".join(rechenweg)


# Beispielparameter
#Beispielaufgabe: Überprüfen Sie mit dem kleinen Satz von Fermat ob 17 ein teiler von 11 hoch 104 + 1 ist.
base = 6    # Basis
power = 100003    # Exponent
divisor = 101  # Divisor
constant = 0  # Konstante

# Ausführen
rechenweg = fermat_test_dynamic(base, power, divisor, constant)
print(rechenweg)
