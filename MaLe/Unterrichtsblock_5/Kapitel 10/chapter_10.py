import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from datetime import datetime

# Voraussetzung: pip install tensorflow

# Daten laden und vorbereiten
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
X_train = X_train.reshape(-1, 28 * 28)
X_test = X_test.reshape(-1, 28 * 28)

# Modellaufbau
model = keras.models.Sequential([
    keras.layers.Dense(300, activation="relu", input_shape=(784,)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

# Callbacks einrichten
log_dir = os.path.join("logs", "fit", datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_cb = keras.callbacks.TensorBoard(log_dir=log_dir)
earlystop_cb = keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
checkpoint_cb = keras.callbacks.ModelCheckpoint("best_mlp_model.h5", save_best_only=True)

# Training starten
history = model.fit(X_train, y_train, epochs=30, validation_split=0.1,
                    callbacks=[tensorboard_cb, earlystop_cb, checkpoint_cb],
                    batch_size=64)

# Modell bewerten
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")

# Hinweis für TensorBoard
print(f"TensorBoard starten mit:\n  tensorboard --logdir={log_dir}")
