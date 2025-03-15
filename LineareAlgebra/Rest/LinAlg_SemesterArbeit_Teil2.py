import numpy as np

class HammingCode:
    def __init__(self, m):
        self.m = m
        self.n = 2**m - 1
        self.k = self.n - m

    def encode(self, word):
        """Erzeugt ein Codewort aus einem 0-1-Wort mit Paritätsbits an 2^i-Positionen."""
        if len(word) != self.k:
            raise ValueError("Länge des Wortes muss k = {} sein.".format(self.k))

        # Initialisiere Codewort mit Platzhaltern für Paritätsbits
        codeword = [0] * self.n
        data_index = 0

        # Setze Datenbits an Nicht-Paritätspositionen
        for i in range(1, self.n + 1):
            if (i & (i - 1)) != 0:  # Kein Potenz von 2 (keine Paritätsposition)
                codeword[i - 1] = word[data_index]
                data_index += 1

        # Berechne Paritätsbits an Positionen 2^i
        for i in range(self.m):
            parity_position = 2**i
            parity_value = 0
            for j in range(1, self.n + 1):
                if j & parity_position and j != parity_position:
                    parity_value ^= codeword[j - 1]
            codeword[parity_position - 1] = parity_value

        return codeword

    def decode(self, codeword):
        """Dekodiert ein Codewort und korrigiert einen einzelnen Fehler."""
        if len(codeword) != self.n:
            raise ValueError("Länge des Codewortes muss n = {} sein.".format(self.n))
        codeword = np.array(codeword, dtype=int)
        syndrome = 0

        # Berechne das Syndrom
        for i in range(self.m):
            parity_position = 2**i
            parity_value = 0
            for j in range(1, self.n + 1):
                if j & parity_position:
                    parity_value ^= codeword[j - 1]
            syndrome |= (parity_value << i)

        # Fehlerkorrektur, falls nötig
        if syndrome != 0:
            error_position = syndrome - 1
            codeword[error_position] ^= 1

        # Extrahiere Datenbits
        data = []
        for i in range(1, self.n + 1):
            if (i & (i - 1)) != 0:  # Kein Potenz von 2 (keine Paritätsposition)
                data.append(int(codeword[i - 1]))  # Konvertiere zu Standard-Integer

        return data

    def check(self, codeword):
        """Überprüft, ob ein Codewort korrekt ist."""
        if len(codeword) != self.n:
            raise ValueError("Länge des Codewortes muss n = {} sein.".format(self.n))
        codeword = np.array(codeword, dtype=int)
        syndrome = 0

        # Berechne das Syndrom
        for i in range(self.m):
            parity_position = 2**i
            parity_value = 0
            for j in range(1, self.n + 1):
                if j & parity_position:
                    parity_value ^= codeword[j - 1]
            syndrome |= (parity_value << i)

        return syndrome == 0


# Test für m = 3
hamming = HammingCode(m=3)

# Nachricht enkodieren
word = [1, 0, 1, 1]
print("Informationswort:", word)
codeword = hamming.encode(word)
print("Codewort mit Paritätsbits an 2^i-Positionen:", codeword)

# Richtiges Codewort prüfen
is_valid = hamming.check(codeword)
print("Ist das Codewort gültig?", is_valid)

# Fehler hinzufügen
codeword[2] ^= 1  # Flippt ein Bit
print("Codewort mit Fehler:", codeword)

# Falsches Codewort prüfen
isnt_valid = hamming.check(codeword)
print("Ist das Codewort gültig?", isnt_valid)

# Fehler korrigieren und dekodieren
decoded_word = hamming.decode(codeword)
print("Dekodiertes Wort:", decoded_word)
