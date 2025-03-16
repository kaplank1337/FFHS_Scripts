### mnist_classifier.py
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# MNIST-Datensatz laden
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target.astype(np.uint8)

# Training & Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=10000, random_state=42, stratify=y)

# Hyperparameter-Tuning mit Grid Search
param_grid = {"n_neighbors": [3, 4, 5], "weights": ["uniform", "distance"]}
knn_clf = GridSearchCV(KNeighborsClassifier(), param_grid, cv=3, scoring="accuracy", n_jobs=-1)
knn_clf.fit(X_train, y_train)

# Bestes Modell testen
y_pred = knn_clf.best_estimator_.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")


### mnist_data_augmentation.py
import scipy.ndimage
import matplotlib.pyplot as plt

def shift_image(image, dx, dy):
    image = image.reshape((28, 28))
    shifted = scipy.ndimage.shift(image, [dy, dx], cval=0)
    return shifted.reshape([-1])

# Erweitertes Trainingsset erstellen
X_train_aug, y_train_aug = [], []
for img, label in zip(X_train, y_train):
    X_train_aug.append(img)
    X_train_aug.append(shift_image(img, 1, 0))
    X_train_aug.append(shift_image(img, -1, 0))
    X_train_aug.append(shift_image(img, 0, 1))
    X_train_aug.append(shift_image(img, 0, -1))
    y_train_aug.extend([label] * 5)

X_train_aug, y_train_aug = np.array(X_train_aug), np.array(y_train_aug)

# Neues Modell trainieren
knn_clf.best_estimator_.fit(X_train_aug, y_train_aug)
y_pred_aug = knn_clf.best_estimator_.predict(X_test)
print(f"Test Accuracy after Data Augmentation: {accuracy_score(y_test, y_pred_aug):.4f}")


### titanic_classifier.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Titanic-Daten laden
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# Features vorbereiten
y_train = train_data["Survived"]
X_train = train_data.drop(["Survived", "Name", "Ticket", "Cabin"], axis=1)
X_test = test_data.drop(["Name", "Ticket", "Cabin"], axis=1)
X_train = pd.get_dummies(X_train, drop_first=True)
X_test = pd.get_dummies(X_test, drop_first=True)

# Modell trainieren
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Titanic Model trained successfully.")


### spam_classifier.py
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def load_emails(directory):
    emails = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), "r", encoding="latin1") as f:
            emails.append(f.read())
    return emails

spam_emails = load_emails("spamassassin/spam")
ham_emails = load_emails("spamassassin/ham")

# Feature-Engineering
X = spam_emails + ham_emails
y = [1] * len(spam_emails) + [0] * len(ham_emails)
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_transformed = vectorizer.fit_transform(X)

# Train/Test-Split & Modelltraining
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
spam_clf = MultinomialNB()
spam_clf.fit(X_train, y_train)

print(f"Spam Classifier Accuracy: {spam_clf.score(X_test, y_test):.4f}")
