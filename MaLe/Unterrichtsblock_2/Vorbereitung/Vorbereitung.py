import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', as_frame=False)
X, y = mnist.data, mnist.target

def plot_digit(image_data):
    image = image_data.reshape(28, 28)
    plt.imshow(image, cmap="binary")
    plt.axis("off")

some_digit = X[0]
print('What is Y: ' + y[0])
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
plot_digit(some_digit)
plt.show()