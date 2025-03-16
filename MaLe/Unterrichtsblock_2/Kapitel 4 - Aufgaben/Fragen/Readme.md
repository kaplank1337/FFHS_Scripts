# Machine Learning Übungen - Fragen und Antworten

## 1. Welchen linearen Regressionsalgorithmus kann man verwenden, wenn das Trainingsset Millionen von Features hat?
<span style="color:green">Stochastic Gradient Descent (SGD) oder Mini-Batch Gradient Descent. Diese Methoden sind effizient für große Datensätze, da sie Parameter iterativ aktualisieren und somit weniger Rechenleistung benötigen als Methoden wie die Normalengleichung oder Singular Value Decomposition (SVD).</span>

## 2. Angenommen, die Features im Trainingsset haben sehr unterschiedliche Skalen. Welche Algorithmen könnten darunter leiden und warum? Was kann man dagegen tun?
<span style="color:green">Algorithmen wie Gradient Descent, k-Nearest Neighbors (k-NN) und Support Vector Machines (SVMs) können darunter leiden, weil Features mit großen Zahlenwerten die Optimierung dominieren. Die Lösung ist **Feature Scaling**, z. B. mit Standardisierung (StandardScaler) oder Normalisierung (MinMaxScaler).</span>

## 3. Kann Gradient Descent in einem lokalen Minimum stecken bleiben, wenn eine logistische Regression trainiert wird?
<span style="color:green">Nein, da die Kostenfunktion der logistischen Regression konvex ist und somit nur ein globales Minimum existiert.</span>

## 4. Führen alle Gradient-Descent-Algorithmen zum gleichen Modell, wenn man sie lange genug laufen lässt?
<span style="color:green">Ja, für konvexe Probleme wie lineare und logistische Regression. Für nicht-konvexe Probleme (z. B. neuronale Netze) kann der Algorithmus jedoch in verschiedenen lokalen Minima landen.</span>

## 5. Angenommen, man verwendet Batch Gradient Descent und beobachtet, dass der Validierungsfehler mit jeder Epoche steigt. Was passiert wahrscheinlich? Wie kann man das beheben?
<span style="color:green">Das Modell overfittet. Lösungen: **Regulierung (Ridge oder Lasso Regression), Early Stopping oder mehr Trainingsdaten sammeln**.</span>

## 6. Sollte man Mini-Batch Gradient Descent sofort stoppen, wenn der Validierungsfehler steigt?
<span style="color:green">Nein. Mini-Batch Gradient Descent schwankt stärker, daher sollte man erst nach mehreren aufeinanderfolgenden Verschlechterungen stoppen (Early Stopping mit Geduld).</span>

## 7. Welcher Gradient-Descent-Algorithmus erreicht am schnellsten die Nähe der optimalen Lösung? Welcher konvergiert tatsächlich? Wie kann man die anderen zur Konvergenz bringen?
<span style="color:green">Mini-Batch Gradient Descent erreicht am schnellsten die Nähe der optimalen Lösung. Batch Gradient Descent konvergiert zuverlässig. Man kann andere Methoden durch Lernraten-Anpassung stabilisieren.</span>

## 8. Angenommen, man nutzt eine polynomiale Regression. Die Lernkurven zeigen einen großen Unterschied zwischen Trainingsfehler und Validierungsfehler. Was passiert? Welche drei Möglichkeiten gibt es, dies zu lösen?
<span style="color:green">Das Modell overfittet. Lösungen: (1) Regulierung (Ridge oder Lasso), (2) Polynomgrad reduzieren, (3) Mehr Trainingsdaten sammeln.</span>

## 9. Angenommen, man verwendet Ridge Regression und beobachtet, dass Trainings- und Validierungsfehler fast gleich und relativ hoch sind. Liegt ein hoher Bias oder eine hohe Varianz vor? Sollte man den Regularisierungsparameter α erhöhen oder verringern?
<span style="color:green">Hoher Bias (Underfitting). **Lösung:** α reduzieren, um dem Modell mehr Flexibilität zu geben.</span>

## 10. Warum sollte man verwenden:
### Ridge Regression statt normaler linearer Regression?
<span style="color:green">Um Overfitting zu verhindern, da Ridge L2-Regularisierung verwendet, um große Koeffizienten zu vermeiden.</span>

### Lasso statt Ridge Regression?
<span style="color:green">Lasso kann Feature Selection durchführen, indem es einige Koeffizienten auf 0 setzt, was das Modell sparsamer macht.</span>

### Elastic Net statt Lasso Regression?
<span style="color:green">Elastic Net ist stabiler als Lasso und funktioniert gut, wenn Features stark korreliert sind.</span>

## 11. Angenommen, man möchte Bilder als "Outdoor/Indoor" und "Tag/Nacht" klassifizieren. Sollte man zwei logistische Regressionsmodelle oder eine Softmax Regression implementieren?
<span style="color:green">Man sollte **zwei logistische Regressionsmodelle** verwenden, da "Outdoor/Indoor" und "Tag/Nacht" unabhängige Labels sind.</span>

## 12. Implementiere Batch Gradient Descent mit Early Stopping für Softmax Regression ohne Scikit-Learn, nur mit NumPy. Wende es auf eine Klassifikationsaufgabe wie den Iris-Datensatz an.
<span style="color:green">Hier ist eine Implementierung von Softmax Regression mit Batch Gradient Descent und Early Stopping:</span>

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Iris-Datensatz laden
iris = load_iris()
X, y = iris.data, iris.target

# Features normalisieren
X = (X - X.mean(axis=0)) / X.std(axis=0)

# Zielwerte in One-Hot-Encoding umwandeln
y_one_hot = np.eye(np.max(y) + 1)[y]

# Train-Test-Split
X_train, X_test, y_train, y_test = train_test_split(X, y_one_hot, test_size=0.2, random_state=42)

# Parameter initialisieren
n_samples, n_features = X_train.shape
n_classes = y_train.shape[1]
W = np.random.randn(n_features, n_classes) * 0.01
b = np.zeros((1, n_classes))
learning_rate = 0.1
epochs = 1000
tol = 1e-4
best_loss = float("inf")
patience = 10
wait = 0

# Softmax-Funktion
def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# Trainingsschleife
for epoch in range(epochs):
    logits = X_train @ W + b
    y_pred = softmax(logits)

    loss = -np.mean(np.sum(y_train * np.log(y_pred + 1e-9), axis=1))  # Cross-Entropy Loss

    if loss < best_loss - tol:
        best_loss = loss
        wait = 0  # Geduld zurücksetzen
    else:
        wait += 1
        if wait >= patience:
            print(f"Early Stopping nach Epoche {epoch}")
            break

    # Gradienten berechnen
    dW = X_train.T @ (y_pred - y_train) / n_samples
    db = np.sum(y_pred - y_train, axis=0, keepdims=True) / n_samples

    # Parameter aktualisieren
    W -= learning_rate * dW
    b -= learning_rate * db

print("Training abgeschlossen.")
```
