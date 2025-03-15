from sympy import primepi
from random import randrange
from sympy import mod_inverse
from sympy import factorint
import math

def isPrimzahl(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i==0:
            return False
    return True
#
#
L = []
i = 2
while len(L) < 20:
    if isPrimzahl(i):
        L.append(i)
    i += 1
#
#
#


# a = [2,5,7]
#
#
def sieve (n):
    primes = []
    numbers = list(range(2,n))
    c = 2
    while c * c < n:
        for k in range (c,n,c):
            if k in numbers:
                numbers.remove(k)
        primes.append(c)
        c = numbers[0]
    return primes + numbers
#
# print(sieve(100))


#
primes = [2,3,5,7,11,13,17,19]
#
def foo (n):
    c = 0
    res = 1
    while c < n:
        res *= primes[c]
        c+=1
    k = res + 1
    return k, isPrimzahl(k)

def satzVonFermat(p):
    return [a ** (p-1) % p for a in range (p)]


def FermaTest (p):
    return randrange(2, p) ** (p-1) % p == 1


# print(FermaTest(24))

def MillerRabin (p):
    d = p-1
    r = 0
    while d % 2 == 0:
        d //=2
        r+=1
    a= randrange(2,p-1)
    x = (a ** d) % p
    if x == 1 or x == p-1:
        return True
    while r > 1:
        x = (x * x) % p
        if x == 1:
            return False
        if x == p-1:
            return True
        r -= 1
    return False

from sympy import prime

#50. und 54. Primzahl
p,q = prime(50), prime(54)
n = p * q
p, q, n



# phi = (p-1) * (q-1)
# print(factorint(phi)) #{2: 3, 3: 1, 5: 3, 19: 1}
# e = 7 * 11 * 13
# print(e) # --> 1001







def derKleineSatzVonFermat(base, exponent, prime):
    # Nutze den kleinen Satz von Fermat, um den Exponenten zu reduzieren
    reduced_exponent = exponent % (prime - 1)

    # Berechne (base^reduced_exponent) % prime
    result =(base ** reduced_exponent) % prime

    return result

# # Beispiel-Aufruf für das gegebene Problem:
# base = 17
# exponent = 45
# prime = 61
#
# result = derKleineSatzVonFermat(base, exponent, prime)
# print(f"Das Ergebnis von {base}^{exponent} mod {prime} ist: {result}")


def ist_teilerfremd(zahl, n):
    # Berechne den größten gemeinsamen Teiler (ggT)
    return math.gcd(zahl, n) == 1

# # Beispielaufruf
# zahl = 7
# n = 72
#
# if ist_teilerfremd(zahl, n):
#     print(f"{zahl} ist teilerfremd zu {n}.")
# else:
#     print(f"{zahl} ist nicht teilerfremd zu {n}.")




def euklidischer_algorithmus(a, b):
    """
    Berechnet den größten gemeinsamen Teiler (GGT) von a und b
    und gibt zudem die Koeffizienten (x, y) zurück, die die Linearkombination erfüllen:
    GGT(a, b) = a * x + b * y
    """
    # Initiale Werte
    original_a, original_b = a, b
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    # a enthält nun den GGT, und x0, y0 sind die Koeffizienten der Linearkombination
    return a, x0, y0

# Beispielverwendung:
a, b = 230,185
ggt, x, y = euklidischer_algorithmus(a, b)
print(f"GGT({a}, {b}) = {ggt}")
print(f"Linearkombination: {ggt} = {a} * ({x}) + {b} * ({y})")

#Um die inverse zu berechnen. (d bei RSA)S
#print(f"Um die Inverse zu berechnen: {mod_inverse(3,40)}")


def euclidean_gcd_with_steps(a, b):
    print(f"Berechnung des ggT von {a} und {b}:")
    while b != 0:
        print(f"{a} = ({a} // {b}) * {b} + {a % b}")
        a, b = b, a % b
    print(f"Der ggT ist: {a}")
    return a


#print(f"KAAN test: {euclidean_gcd_with_steps(234,111)}")
