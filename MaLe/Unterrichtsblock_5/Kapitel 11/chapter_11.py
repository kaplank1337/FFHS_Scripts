import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, optimizers, callbacks
from sklearn.model_selection import train_test_split
import time

#Voraussetzung: pip install tensorflow scikit-learn

# Daten laden und vorbereiten
(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train_full = X_train_full.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
X_train_full = X_train_full.reshape(-1, 28 * 28)
X_test = X_test.reshape(-1, 28 * 28)

# Aufgabe 8: Trainingsdaten 0–4
mask_0_4 = y_train_full < 5
X_0_4 = X_train_full[mask_0_4]
y_0_4 = y_train_full[mask_0_4]

# Modellbau-Funktion
def build_dnn_model(batch_norm=False, dropout=False, output_units=5, output_activation='softmax'):
    model = keras.models.Sequential()
    model.add(layers.Input(shape=(784,)))
    for _ in range(5):
        model.add(layers.Dense(100, kernel_initializer="he_normal"))
        if batch_norm:
            model.add(layers.BatchNormalization())
        model.add(layers.ELU())
        if dropout:
            model.add(layers.Dropout(0.3))
    model.add(layers.Dense(output_units, activation=output_activation))
    return model

# Aufgabe 8b: Training auf Ziffern 0–4 mit Adam und EarlyStopping
model_8 = build_dnn_model()
model_8.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
checkpoint_cb = callbacks.ModelCheckpoint("dnn_mnist_0_4.h5", save_best_only=True)
earlystop_cb = callbacks.EarlyStopping(patience=5, restore_best_weights=True)
history_8 = model_8.fit(X_0_4, y_0_4, epochs=30, validation_split=0.1,
                        callbacks=[checkpoint_cb, earlystop_cb], batch_size=64)

# Aufgabe 9: Transfer Learning auf Ziffern 5–9
mask_5_9 = y_train_full >= 5
X_5_9_full = X_train_full[mask_5_9]
y_5_9_full = y_train_full[mask_5_9]
X_5_9 = []
y_5_9 = []
for digit in range(5, 10):
    idx = np.where(y_5_9_full == digit)[0][:100]
    X_5_9.append(X_5_9_full[idx])
    y_5_9.append(y_5_9_full[idx] - 5)
X_5_9 = np.concatenate(X_5_9, axis=0)
y_5_9 = np.concatenate(y_5_9, axis=0)

# Eingefrorenes Modell laden und anpassen
pretrained = keras.models.load_model("dnn_mnist_0_4.h5")
transfer_model = keras.models.Sequential()
for layer in pretrained.layers[:-1]:
    layer.trainable = False
    transfer_model.add(layer)
transfer_model.add(layers.Dense(5, activation="softmax"))

transfer_model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
start_time = time.time()
transfer_model.fit(X_5_9, y_5_9, epochs=20, validation_split=0.1, batch_size=32)
transfer_duration = time.time() - start_time

# Aufgabe 10a: Vergleichs-DNNs A und B für Gleichheitserkennung
def build_shared_dnn():
    model = keras.models.Sequential()
    model.add(layers.Input(shape=(784,)))
    for _ in range(5):
        model.add(layers.Dense(100, activation="elu", kernel_initializer="he_normal"))
    return model

dnn_A = build_shared_dnn()
dnn_B = build_shared_dnn()

input_A = keras.Input(shape=(784,))
input_B = keras.Input(shape=(784,))
out_A = dnn_A(input_A)
out_B = dnn_B(input_B)
merged = layers.Concatenate()([out_A, out_B])
hidden = layers.Dense(10, activation="elu")(merged)
output = layers.Dense(1, activation="sigmoid")(hidden)
comparison_model = keras.Model(inputs=[input_A, input_B], outputs=output)

comparison_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Aufgabe 10b: Trainingsdaten-Paare generieren
def generate_pairs(X, y, n_pairs):
    pairs_A, pairs_B, labels = [], [], []
    num_classes = np.max(y) + 1
    class_indices = [np.where(y == i)[0] for i in range(num_classes)]
    for _ in range(n_pairs // 2):
        c = np.random.randint(0, num_classes)
        i1, i2 = np.random.choice(class_indices[c], 2, replace=False)
        pairs_A.append(X[i1])
        pairs_B.append(X[i2])
        labels.append(0)
        c1, c2 = np.random.choice(num_classes, 2, replace=False)
        i1 = np.random.choice(class_indices[c1])
        i2 = np.random.choice(class_indices[c2])
        pairs_A.append(X[i1])
        pairs_B.append(X[i2])
        labels.append(1)
    return np.array(pairs_A), np.array(pairs_B), np.array(labels)

X_split1, X_split2, y_split1, y_split2 = train_test_split(X_train_full, y_train_full, test_size=5000, stratify=y_train_full)
X_A, X_B, y_pairs = generate_pairs(X_split1, y_split1, 10000)

# Aufgabe 10c: Modell trainieren
comparison_model.fit([X_A, X_B], y_pairs, epochs=10, batch_size=64, validation_split=0.1)

# Aufgabe 10d: Klassifikations-DNN auf Basis von DNN A
frozen_base = dnn_A
for layer in frozen_base.layers:
    layer.trainable = False
clf_input = keras.Input(shape=(784,))
x = frozen_base(clf_input)
output = layers.Dense(10, activation="softmax")(x)
final_classifier = keras.Model(inputs=clf_input, outputs=output)

final_classifier.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
mask_split2 = np.isin(y_split2, np.arange(10))
X_clf = X_split2[mask_split2]
y_clf = y_split2[mask_split2]
final_classifier.fit(X_clf, y_clf, epochs=20, validation_split=0.1, batch_size=32)
