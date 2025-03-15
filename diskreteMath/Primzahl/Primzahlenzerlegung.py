def prime_factors(n):
    """
    Berechnet die Primfaktorzerlegung einer gegebenen Zahl.

    :param n: Die zu zerlegende Zahl
    :return: Ein Dictionary mit Primfaktoren und deren Potenzen
    """
    factors = {}
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1

        # Optimierung: Keine unnötigen Prüfungen über die Quadratwurzel von n hinaus
        if divisor * divisor > n and n > 1:
            factors[n] = 1
            break

    return factors

def display_factors(number, factors):
    """
    Gibt die Primfaktorzerlegung einer Zahl formatiert aus.

    :param number: Die ursprüngliche Zahl
    :param factors: Dictionary mit Primfaktoren und Potenzen
    """
    factor_string = " · ".join([f"{prime}^{power}" if power > 1 else f"{prime}" for prime, power in factors.items()])
    print(f"Die Primfaktorzerlegung von {number} ist: {factor_string}")

if __name__ == "__main__":
    # Zahlen für die Zerlegung
    numbers = [1234, 36000]

    for number in numbers:
        factors = prime_factors(number)
        display_factors(number, factors)
