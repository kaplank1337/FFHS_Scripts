from sympy import mod_inverse, factorint, prime

p, q = prime(50), prime(54)
n= p * q

phi = (p -1) * (q - 1)
print(factorint(phi))
e = 7 * 11 * 13

d = mod_inverse(e, phi)

crypt = lambda M, k: M ** k % n
N=51234
S = crypt(N, e)


print(f"Öffentlicher Schlüssel(n, e): {n}, {e}")
print(f"Privater Schlüssel(d): {d}")
print(f"Die Nachricht lautet: {N}")
print(f"Die verschlüsselte Nachricht lautet: {S}")
print(f"Die entschlüsselte Nacrhicht lautet: {crypt(S, d)}")