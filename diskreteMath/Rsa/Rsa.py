import math
from sympy import gcd

def generate_rsa_keys(p, q):
    # 1. Schritt: Berechnung von n
    n = p * q
    print(f"1. Schritt: n = p * q = {p} * {q} = {n}")

    # 2. Schritt: Berechnung von phi(n)
    phi_n = (p - 1) * (q - 1)
    print(f"2. Schritt: phi(n) = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi_n}")

    # 3. Schritt: Wähle ein öffentliches Exponent e
    e = 2
    while e < phi_n and gcd(e, phi_n) != 1:
        e += 1
    print(f"3. Schritt: Öffentliches Exponent e gewählt: e = {e}")

    # 4. Schritt: Berechnung des privaten Schlüssels d
    d = pow(e, -1, phi_n)  # Modulare Inverse von e mod phi(n)
    print(f"4. Schritt: Privater Schlüssel d berechnet: d = {d}")

    # Rückgabe der Schlüssel
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# Hauptprogramm
print("Willkommen zur RSA-Schlüsselerzeugung!")
p = int(input("Gib die erste Primzahl (p) ein: "))
q = int(input("Gib die zweite Primzahl (q) ein: "))

# Überprüfen, ob die Eingaben Primzahlen sind
if not (p > 1 and q > 1 and all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1)) and all(q % i != 0 for i in range(2, int(math.sqrt(q)) + 1))):
    print("Beide Zahlen müssen Primzahlen sein!")
else:
    public_key, private_key = generate_rsa_keys(p, q)
    print("\nErgebnisse:")
    print(f"Öffentlicher Schlüssel: (e, n) = {public_key}")
    print(f"Privater Schlüssel: (d, n) = {private_key}")
