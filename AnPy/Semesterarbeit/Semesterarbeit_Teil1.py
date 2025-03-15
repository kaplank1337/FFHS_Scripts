import time

def fib(n):
    """
    Berechnet die n-te Fibonacci-Zahl mit einer naiven rekursiven Methode.
    Diese Methode folgt direkt der mathematischen Definition.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def count_fib_calls(n, calls=[0]):
    """
    Zählt, wie oft die Funktion fib(n) aufgerufen wird.
    """
    calls[0] += 1  # Erhöht den Zähler für jeden Funktionsaufruf
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return count_fib_calls(n - 1, calls) + count_fib_calls(n - 2, calls)

# Anzahl der Funktionsaufrufe für bestimmte Fibonacci-Zahlen prüfen
for i in range(10):
    calls = [0]
    count_fib_calls(i, calls)
    print(f"fib({i}) wird {calls[0]} mal aufgerufen.")

def measure_time(n):
    """
    Misst die Zeit, die benötigt wird, um die n-te Fibonacci-Zahl zu berechnen.
    """
    start_time = time.time()
    fib(n)
    end_time = time.time()
    return end_time - start_time

# Zeitmessung für einige Werte
for i in range(30):
    duration = measure_time(i)
    print(f"Berechnungszeit für fib({i}): {duration:.6f} Sekunden")

def fib_efficient(n):
    """
    Berechnet die n-te Fibonacci-Zahl mit einer iterativen Methode,
    die wesentlich effizienter als die rekursive Methode ist.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test der effizienten Fibonacci-Funktion
for i in range(10):
    print(f"fib_efficient({i}) = {fib_efficient(i)}")



