class Restklassenring:
    def __init__(self, modulo):
        """
        Erstellt einen Restklassenring modulo n.
        :param modulo: Modulo-Wert des Rings
        """
        self.modulo = modulo

    def add(self, a, b):
        """
        Addiert zwei Zahlen in der Restklasse.
        """
        return (a + b) % self.modulo

    def subtract(self, a, b):
        """
        Subtrahiert zwei Zahlen in der Restklasse.
        """
        return (a - b) % self.modulo

    def multiply(self, a, b):
        """
        Multipliziert zwei Zahlen in der Restklasse.
        """
        return (a * b) % self.modulo

    def divide(self, a, b):
        """
        Dividiert zwei Zahlen in der Restklasse (wenn möglich).
        Division erfordert, dass b ein multiplikatives Inverses hat.
        """
        inverse = self.modular_inverse(b)
        if inverse is None:
            raise ValueError(f"Die Zahl {b} hat kein Inverses in Z_{self.modulo}.")
        return (a * inverse) % self.modulo

    def modular_inverse(self, a):
        """
        Berechnet das multiplikative Inverse von a modulo n, falls vorhanden.
        """
        g, x, _ = self.extended_euclid(a, self.modulo)
        if g != 1:
            return None  # Kein Inverses, wenn ggT(a, modulo) != 1
        return x % self.modulo

    @staticmethod
    def extended_euclid(a, b):
        """
        Führt den erweiterten euklidischen Algorithmus durch.
        :return: ggT, x, y mit ggT = a * x + b * y
        """
        if b == 0:
            return a, 1, 0
        g, x1, y1 = Restklassenring.extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

# Beispielnutzung
modulo = 7
ring = Restklassenring(modulo)

a = 3
b = 5

print(f"Modulo Invers: ({a} + {b}) = {ring.modular_inverse(a,b)}")
print(f"Addition: ({a} + {b}) mod {modulo} = {ring.add(a, b)}")
print(f"Subtraktion: ({a} - {b}) mod {modulo} = {ring.subtract(a, b)}")
print(f"Multiplikation: ({a} * {b}) mod {modulo} = {ring.multiply(a, b)}")
try:
    print(f"Division: ({a} / {b}) mod {modulo} = {ring.divide(a, b)}")
except ValueError as e:
    print(e)
