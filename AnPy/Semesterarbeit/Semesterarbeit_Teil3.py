# spline_approximation.py
# Autor: [Kaan Kaplan]
# Beschreibung: Approximation der Sinusfunktion mittels kubischer Splines
# Bibliotheken: numpy, scipy, matplotlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 1. Definition der exakten Funktion, die approximiert werden soll
def f(x):
    return np.sin(x)

# 2. Erzeuge Stützpunkte im Intervall [0, 2π]
n = 10  # Anzahl der Stützstellen
x_stuetz = np.linspace(0, 2 * np.pi, n)
y_stuetz = f(x_stuetz)

# 3. Erzeuge kubischen Spline – wähle zwischen 'natural', 'clamped' oder 'not-a-knot'
# Für natürliche Splines: zweite Ableitungen am Rand sind 0
spline_natural = CubicSpline(x_stuetz, y_stuetz, bc_type='natural')

# Für geklammerte Splines: erste Ableitung an den Rändern ist vorgegeben (hier: cos(0) = 1, cos(2π) = 1)
spline_clamped = CubicSpline(x_stuetz, y_stuetz, bc_type=((1, 1.0), (1, 1.0)))

# 4. Erzeuge feines Auswertungsgitter für Plot
x_fine = np.linspace(0, 2 * np.pi, 1000)
y_exact = f(x_fine)
y_spline_natural = spline_natural(x_fine)
y_spline_clamped = spline_clamped(x_fine)

# 5. Visualisiere Ergebnisse mit Matplotlib
plt.figure(figsize=(10, 6))

# Exakte Funktion
plt.plot(x_fine, y_exact, 'k--', label='Exakte Funktion (sin(x))')

# Spline-Approximationen
plt.plot(x_fine, y_spline_natural, 'b-', label='Spline (natural)')
plt.plot(x_fine, y_spline_clamped, 'g-', label='Spline (clamped)')

# Stützpunkte markieren
plt.plot(x_stuetz, y_stuetz, 'ro', label='Stützpunkte')

# Plot-Einstellungen
plt.title('Approximation von sin(x) mit kubischen Splines')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()

# 6. Plot anzeigen
plt.show()
