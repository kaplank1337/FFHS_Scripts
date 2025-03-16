import numpy as np

def harmonische_teilsumme(n, p=1):
    """
    Berechnet die Teilsumme der allgemeinen harmonischen Reihe für gegebenes n und p.
    """
    return np.sum(1 / np.arange(1, n+1) ** p)

# Beispielaufruf
print(harmonische_teilsumme(1000, 1))  # Erwartet: Divergentes Verhalten
print(harmonische_teilsumme(1000, 2))  # Erwartet: Konvergentes Verhalten



import matplotlib.pyplot as plt

def plot_harmonische_reihe(n_max, p_values):
    """
    Plottet das Konvergenz-/Divergenzverhalten der harmonischen Reihe für verschiedene p-Werte.
    """
    n_values = np.arange(1, n_max + 1)

    plt.figure(figsize=(10, 6))
    for p in p_values:
        series = np.cumsum(1 / n_values ** p)
        plt.plot(n_values, series, label=f"p={p}")

    plt.xlabel("n")
    plt.ylabel("Teilsumme")
    plt.title("Konvergenz-/Divergenzverhalten der harmonischen Reihe")
    plt.legend()
    plt.grid()
    plt.show()

def plot_konvergenzgeschwindigkeit(n_max, p):
    """
    Visualisiert die Konvergenzgeschwindigkeit für p > 1.
    """
    n_values = np.arange(1, n_max + 1)
    series = np.cumsum(1 / n_values ** p)

    # Näherung des Grenzwerts durch die letzten 10 Werte
    S_inf_approx = np.mean(series[-10:])
    errors = np.abs(S_inf_approx - series)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, errors, label=f"p={p}")
    plt.yscale("log")  # Log-Skala für besseren Vergleich
    plt.xlabel("n")
    plt.ylabel("Fehler |S∞ - Sn|")
    plt.title("Konvergenzgeschwindigkeit der harmonischen Reihe")
    plt.legend()
    plt.grid()
    plt.show()

# Beispiel für p=2
plot_konvergenzgeschwindigkeit(1000, 2)


# # Beispielplot für verschiedene p-Werte
# plot_harmonische_reihe(1000, [1, 1.2, 1.5, 2])
