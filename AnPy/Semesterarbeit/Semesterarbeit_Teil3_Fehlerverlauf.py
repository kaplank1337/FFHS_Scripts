# spline_fehlervergleich_bc.py
# Autor: Kaan Kaplan
# Ziel: Vergleich des Fehlers bei 'natural' vs. 'clamped' Splines

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Zielfunktion
def f(x):
    return np.sin(x)

# Ableitung der Zielfunktion für 'clamped' Randbedingung
def f_prime(x):
    return np.cos(x)

# Fein aufgelöstes Gitter zur Fehlerberechnung
x_fine = np.linspace(0, 2 * np.pi, 1000)
y_exact = f(x_fine)

# Liste von Stützstellen-Anzahlen
n_values = [5, 10, 20, 40, 80]

# Fehlerlisten für beide Randbedingungen
errors_natural = []
errors_clamped = []

for n in n_values:
    # Erzeuge Stützstellen
    x_stuetz = np.linspace(0, 2 * np.pi, n)
    y_stuetz = f(x_stuetz)

    # --- Natürlicher Spline ---
    spline_natural = CubicSpline(x_stuetz, y_stuetz, bc_type='natural')
    y_natural = spline_natural(x_fine)
    max_error_natural = np.max(np.abs(y_natural - y_exact))
    errors_natural.append(max_error_natural)

    # --- Geklammerter Spline (mit f'(0) = cos(0) = 1, f'(2π) = cos(2π) = 1) ---
    spline_clamped = CubicSpline(x_stuetz, y_stuetz, bc_type=((1, 1.0), (1, 1.0)))
    y_clamped = spline_clamped(x_fine)
    max_error_clamped = np.max(np.abs(y_clamped - y_exact))
    errors_clamped.append(max_error_clamped)

# --- Plot: Fehlervergleich ---
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors_natural, 'bo-', label='Max. Fehler (natural)')
plt.plot(n_values, errors_clamped, 'go-', label='Max. Fehler (clamped)')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Anzahl Stützstellen (n)')
plt.ylabel('Maximaler Absolutfehler')
plt.title('Abbildung 3: Fehlervergleich für natural vs. clamped')
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig("spline_fehlervergleich_bc.png", dpi=300)
plt.show()
