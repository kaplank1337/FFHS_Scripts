import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# MNIST laden
print("Lade MNIST...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser="pandas")
X, y = mnist.data, mnist.target.astype(np.uint8)

# Trainings-, Validierungs- und Testset erstellen
X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=10000, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, test_size=10000, random_state=42)

# Klassifikatoren trainieren
print("Trainiere Einzelmodelle...")
rnd_clf = RandomForestClassifier(n_estimators=100, random_state=42)
ext_clf = ExtraTreesClassifier(n_estimators=100, random_state=42)
svm_clf = SVC(probability=True, random_state=42)

rnd_clf.fit(X_train, y_train)
ext_clf.fit(X_train, y_train)
svm_clf.fit(X_train, y_train)

# Soft Voting Classifier
voting_clf = VotingClassifier(
    estimators=[('rf', rnd_clf), ('et', ext_clf), ('svm', svm_clf)],
    voting='soft'
)
voting_clf.fit(X_valid, y_valid)
voting_preds = voting_clf.predict(X_test)
voting_acc = accuracy_score(y_test, voting_preds)
print(f"Soft Voting Accuracy auf Testset: {voting_acc:.4f}")

# Aufgabe 9: Stacking Ensemble
print("Trainiere Stacking Ensemble...")
# Vorhersagen auf Validierungsset als neue Trainingsdaten für Meta-Classifier
valid_pred_rf = rnd_clf.predict(X_valid)
valid_pred_et = ext_clf.predict(X_valid)
valid_pred_svm = svm_clf.predict(X_valid)

X_blender_train = np.c_[valid_pred_rf, valid_pred_et, valid_pred_svm]
y_blender_train = y_valid

# Meta-Classifier (Blender)
blender = LogisticRegression(max_iter=1000)
blender.fit(X_blender_train, y_blender_train)

# Testdaten vorhersagen und zum Blender geben
test_pred_rf = rnd_clf.predict(X_test)
test_pred_et = ext_clf.predict(X_test)
test_pred_svm = svm_clf.predict(X_test)

X_blender_test = np.c_[test_pred_rf, test_pred_et, test_pred_svm]
final_preds = blender.predict(X_blender_test)

# Ergebnis auswerten
stacking_acc = accuracy_score(y_test, final_preds)
print(f"Stacking Ensemble Accuracy auf Testset: {stacking_acc:.4f}")
