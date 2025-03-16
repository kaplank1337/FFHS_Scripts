
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from scipy.stats import mode

# Aufgabe 7: Decision Tree mit Grid Search auf moons-Dataset
def aufgabe_7_decision_tree_grid_search():
    X, y = make_moons(n_samples=10000, noise=0.4, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    param_grid = {"max_leaf_nodes": list(range(2, 100))}
    grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    best_tree = grid_search.best_estimator_
    y_pred = best_tree.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("Aufgabe 7:")
    print(f"Beste max_leaf_nodes: {grid_search.best_params_['max_leaf_nodes']}")
    print(f"Test Accuracy: {acc:.4f}\n")
    return best_tree, X_train, y_train, X_test, y_test

# Aufgabe 8: Random Forest "von Hand" mit Majority Voting
def aufgabe_8_custom_random_forest(X_train, y_train, X_test, y_test, base_tree):
    n_trees = 1000
    n_instances = 100
    rng = np.random.RandomState(42)
    mini_sets = []

    for _ in range(n_trees):
        indices = rng.randint(0, len(X_train), n_instances)
        mini_sets.append((X_train[indices], y_train[indices]))

    forest = [DecisionTreeClassifier(max_leaf_nodes=base_tree.max_leaf_nodes, random_state=rng.randint(10000)).fit(X_mini, y_mini)
              for X_mini, y_mini in mini_sets]

    predictions = np.array([tree.predict(X_test) for tree in forest])
    majority_votes = mode(predictions, axis=0, keepdims=False).mode

    accuracy = accuracy_score(y_test, majority_votes)
    print("Aufgabe 8:")
    print(f"Majority Voting Accuracy mit 1000 Bäumen: {accuracy:.4f}")

# Hauptfunktion
if __name__ == "__main__":
    best_tree, X_train, y_train, X_test, y_test = aufgabe_7_decision_tree_grid_search()
    aufgabe_8_custom_random_forest(X_train, y_train, X_test, y_test, best_tree)
