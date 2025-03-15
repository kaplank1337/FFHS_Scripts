import math

def eratosthenes(n):
    primzahlen = []
    zahlen = list(range(2, n))
    aktuell = 2

    while aktuell < math.sqrt(n):
        for _ in range(aktuell, n, aktuell):
            if _ in zahlen:
                zahlen.remove(_)
        primzahlen.append(aktuell)
        aktuell = zahlen[0]

    return primzahlen + zahlen



print(f"Alle Primzahlen bis hier:{eratosthenes(53)}")