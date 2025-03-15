#Dieser Test entscheided ob eine grosse Zahl eine Primzahl ist.

import random

def is_prime_miller_rabin(n, k=520):
    """
    Prüft, ob die Zahl n (wahrscheinlich) eine Primzahl ist, mit dem Miller-Rabin-Test.

    :param n: Die zu prüfende Zahl
    :param k: Anzahl der Testdurchläufe (je mehr, desto genauer)
    :return: True, wenn n wahrscheinlich eine Primzahl ist, sonst False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Zerlege n - 1 in 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Wiederhole den Test k-mal
    for _ in range(k):
        a = random.randint(2, n - 2)  # Wähle zufällige Basis a
        x = pow(a, d, n)  # Berechne a^d mod n
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def check_primes(numbers):
    """
    Prüft ein Array von Zahlen mit dem Miller-Rabin-Test.

    :param numbers: Liste von Zahlen
    :return: Dictionary mit den Zahlen und deren Ergebnis (True/False)
    """
    results = {}
    for num in numbers:
        results[num] = is_prime_miller_rabin(num)
    return results

# Beispiel-Array
numbers = [1105]

# Zahlen prüfen
results = check_primes(numbers)

# Ergebnisse ausgeben
for num, is_prime in results.items():
    print(f"{num} ist {'eine Primzahl' if is_prime else 'keine Primzahl'}")
