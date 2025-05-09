import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# MNIST-Daten laden
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist["data"], mnist["target"].astype(np.uint8)

# Trainings- und Testdaten splitten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=10000, train_size=60000, random_state=42)

# Aufgabe 9 - Random Forest auf originalen Daten
print("Training Random Forest auf originalen Daten...")
start = time.time()
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
duration_rf = time.time() - start
y_pred = rf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred)
print(f"Trainingsdauer (original): {duration_rf:.2f} Sekunden | Accuracy: {accuracy_rf:.4f}")

# PCA mit 95% Varianz
print("Anwenden von PCA...")
pca = PCA(n_components=0.95, random_state=42)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)

# Random Forest auf reduzierten Daten
print("Training Random Forest auf reduzierten Daten...")
start = time.time()
rf_reduced = RandomForestClassifier(n_estimators=100, random_state=42)
rf_reduced.fit(X_train_reduced, y_train)
duration_rf_reduced = time.time() - start
y_pred_reduced = rf_reduced.predict(X_test_reduced)
accuracy_rf_reduced = accuracy_score(y_test, y_pred_reduced)
print(f"Trainingsdauer (reduziert): {duration_rf_reduced:.2f} Sekunden | Accuracy: {accuracy_rf_reduced:.4f}")

# Aufgabe 10 - t-SNE für Visualisierung
print("t-SNE wird berechnet...")
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
X_2d = tsne.fit_transform(X_test[:3000])  # nur Teilmenge für Visualisierung
y_2d = y_test[:3000]

# Visualisierung
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y_2d, cmap='tab10', alpha=0.7, s=15)
plt.colorbar(scatter, ticks=range(10))
plt.title("t-SNE Visualisierung der MNIST-Daten (Testmenge)")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.grid(True)
plt.show()
