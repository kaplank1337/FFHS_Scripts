import numpy as np

def potenz_matrix(A, power):
    """
    Berechnet die Potenzmatrix A^power
    :param A: Adjazenzmatrix (2D numpy array)
    :param power: Die Potenz, auf die die Matrix erhoben werden soll
    :return: Die Potenzmatrix A^power
    """
    result = np.linalg.matrix_power(A, power)
    return result

# Beispiel einer Adjazenzmatrix
A = np.array([[0, 1, 1, 1],
              [1, 0, 1, 1],
              [1, 1, 0, 1],
              [1, 1, 1, 0]])

# Berechnung der Potenzmatrix A^2
power = 2
A_squared = potenz_matrix(A, power)

# print(f"Die Potenzmatrix A^{power} ist:")
# print(A_squared)


################################################################################



import heapq
import pandas as pd

# Definiere den Graphen basierend auf den Kanten und ihren Gewichten
graph = {
    'O': {'A': 4, 'C': 5, 'B': 6},
    'A': {'D': 7, 'B': 1, 'O': 4},
    'B': {'D': 5, 'E': 4, 'A': 1, 'C': 2, 'O': 6},
    'C': {'B': 2, 'O': 5, 'E': 5},
    'D': {'T': 6, 'E': 1, 'B': 5, 'A': 7},
    'E': {'T': 8, 'D': 1, 'B': 5, 'C': 5},
    'T': {}
}

# Dijkstra-Funktion
def dijkstra_with_table(graph, start, ziel):
    # Initialisierung
    distances = {node: float('inf') for node in graph}  # Unendliche Entfernung für alle Knoten
    distances[start] = 0  # Entfernung zum Startknoten ist 0
    priority_queue = [(0, start)]  # Prioritätswarteschlange für den Dijkstra-Algorithmus
    previous_nodes = {node: None for node in graph}  # Um den Pfad zurückzuverfolgen
    table = []  # Tabelle für die Ausgaben

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip, wenn der aktuelle Weg nicht besser ist
        if current_distance > distances[current_node]:
            continue

        # Betrachte die Nachbarn des aktuellen Knotens
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Wenn ein kürzerer Weg gefunden wird, aktualisiere die Entfernung
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

            # Tabelle aktualisieren
            table.append({
                "n-te Knoten": current_node,
                "Knoten mit Me-Verbindung": neighbor,
                "Kürzeste": f"{neighbor}({weight})",
                "Gesamt": distance,
                "M1 neu": previous_nodes[current_node] if previous_nodes[current_node] else "Start"
            })

    # Kürzester Pfad zum Zielknoten finden
    path = []
    current = ziel
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    # Tabelle in DataFrame umwandeln
    df = pd.DataFrame(table)
    print(df)  # Tabelle ausgeben

    # Kürzester Pfad ausgeben
    if distances[ziel] == float('inf'):
        return f"Kein Pfad von {start} zu {ziel} gefunden."
    else:
        return path, distances[ziel]

# Start- und Zielknoten
start_node = 'O'
ziel_node = 'T'

# Dijkstra-Algorithmus ausführen
path, distance = dijkstra_with_table(graph, start_node, ziel_node)
print(f"Kürzester Pfad von {start_node} zu {ziel_node}: {' -> '.join(path)} mit einer Entfernung von {distance}")
