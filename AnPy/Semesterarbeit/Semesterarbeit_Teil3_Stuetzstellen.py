# spline_error_analysis.py
# Autor: Kaan Kaplan
# Ziel: Einfluss der Anzahl der Stützstellen auf den Approximationsfehler untersuchen

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Zielfunktion
def f(x):
    return np.sin(x)

# Gitter für feine Auswertung der exakten und approximierten Funktion
x_fine = np.linspace(0, 2 * np.pi, 1000)
y_exact = f(x_fine)

# Werte für n (Anzahl der Stützstellen)
n_values = [5, 10, 20, 40, 80]
errors = []

for n in n_values:
    # 1. Erzeuge Stützpunkte und Funktionswerte
    x_stuetz = np.linspace(0, 2 * np.pi, n)
    y_stuetz = f(x_stuetz)

    # 2. Erstelle natürlichen Spline (Alternativ: clamped)
    spline = CubicSpline(x_stuetz, y_stuetz, bc_type='natural')

    # 3. Werte Spline auf feinem Gitter aus
    y_spline = spline(x_fine)

    # 4. Berechne maximalen Absolutfehler
    max_error = np.max(np.abs(y_spline - y_exact))
    errors.append(max_error)

    # Optional: Plot der einzelnen Spline-Kurven
    plt.figure(figsize=(8, 4))
    plt.plot(x_fine, y_exact, 'k--', label='Exakte Funktion')
    plt.plot(x_fine, y_spline, label=f'Spline (n={n})')
    plt.plot(x_stuetz, y_stuetz, 'ro', label='Stützpunkte')
    plt.title(f'Spline-Approximation für n = {n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"spline_plot_n{n}.png", dpi=300)
    plt.close()

# Plot: Fehler gegen Anzahl der Stützstellen
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors, 'o-', label='Maximaler Fehler')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Anzahl Stützpunkte (n)')
plt.ylabel('Maximaler Absolutfehler')
plt.title('Abbildung 2: Einfluss von n auf den Approximationsfehler')
plt.grid(True, which='both', ls='--')
plt.legend()
plt.tight_layout()
plt.savefig("spline_fehlerplot.png", dpi=300)
plt.show()
