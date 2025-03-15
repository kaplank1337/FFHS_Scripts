import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

class Parallellepiped:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def vertices(self):
        return np.array([[0, 0, 0], [self.a, 0, 0], [self.a, self.b, 0], [0, self.b, 0],
                         [0, 0, self.c], [self.a, 0, self.c], [self.a, self.b, self.c], [0, self.b, self.c]])

    def edges(self):
        return [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
                (0, 4), (1, 5), (2, 6), (3, 7)]

def zentralprojektion(parallelepiped, proj_z):
    proj_center = np.array([0, 0, proj_z])

    vertices = parallelepiped.vertices()
    projected_vertices = []

    for vertex in vertices:
        x, y, z = vertex
        x_proj = (proj_center[2] * x) / (z - proj_center[2])
        y_proj = (proj_center[2] * y) / (z - proj_center[2])
        projected_vertices.append([x_proj, y_proj])

    return np.array(projected_vertices)

def plot_parallellepiped(parallelepiped, proj_z):
    projected_vertices = zentralprojektion(parallelepiped, proj_z)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(projected_vertices[:, 0], projected_vertices[:, 1], color='r')

    for edge in parallelepiped.edges():
        start, end = projected_vertices[edge[0]], projected_vertices[edge[1]]
        ax.plot([start[0], end[0]], [start[1], end[1]], color='b')

    ax.set_xlabel('X-Achse')
    ax.set_ylabel('Y-Achse')
    ax.set_title('Zentralprojektion des Parallellepipeds')
    ax.axis('equal')
    plt.grid()
    plt.show()

parallelepiped = Parallellepiped(a=2, b=3, c=4)
plot_parallellepiped(parallelepiped, proj_z=5)
