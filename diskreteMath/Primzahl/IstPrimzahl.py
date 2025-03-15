def isPrimazhl(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i==0:
            return False
    return True

L = []
i = 100
while len(L) < 20:
    if isPrimazhl(i):
        L.append(i)
    i += 1

print(L)