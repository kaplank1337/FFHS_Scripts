def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler (ggT) von a und b."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Erweiterter euklidischer Algorithmus: Berechnet den ggT sowie x und y."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """Berechnet das modulare Inverse von e mod phi."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modulares Inverses existiert nicht.')
    return x % phi

def rsa_keygen(p, q, e):
    """Erstellt ein RSA-Schlüsselpaar und zeigt die Zwischenschritte."""
    print(f"Primzahlen p = {p}, q = {q}")

    # Berechne n
    n = p * q
    print(f"n = p * q = {p} * {q} = {n}")

    # Berechne phi(n)
    phi = (p - 1) * (q - 1)
    print(f"phi(n) = (p - 1) * (q - 1) = {p - 1} * {q - 1} = {phi}")

    # Wähle das kleinste e > 1, sodass ggT(e, phi(n)) = 1
    if gcd(e, phi) != 1:
        raise ValueError(f"e = {e} ist nicht teilerfremd zu phi(n) = {phi}.")
    print(f"e = {e} ist teilerfremd zu phi(n) = {phi}")

    # Berechne d (das modulare Inverse von e mod phi)
    d = mod_inverse(e, phi)
    print(f"d ist das modulare Inverse von e mod phi(n): d = {d}")

    # Öffentlicher und privater Schlüssel
    public_key = (n, e)
    private_key = (n, d)

    print(f"Öffentlicher Schlüssel: (n, e) = ({n}, {e})")
    print(f"Privater Schlüssel: (n, d) = ({n}, {d})")

    return public_key, private_key

# Beispielaufruf
p = 7
q = 13
e = 7

rsa_keygen(p,q,e)