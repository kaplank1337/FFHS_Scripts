import heapq
from prettytable import PrettyTable

def dijkstra(graph, start):
    """
    Berechnet die kürzesten Wege von einem Startknoten zu allen anderen Knoten im Graphen.

    :param graph: Dictionary, das den Graphen darstellt.
                  Der Schlüssel ist der Knoten, die Werte sind Dictionaries mit Nachbarn und deren Gewichten.
    :param start: Startknoten
    :return: Zwei Dictionaries:
             - distances: kürzeste Entfernung zu jedem Knoten
             - previous: Vorgängerknoten für den kürzesten Weg
    """
    # Initialisierung
    distances = {node: float('inf') for node in graph}  # Alle Distanzen auf Unendlich setzen
    distances[start] = 0  # Startknoten hat Distanz 0
    previous = {node: None for node in graph}  # Vorgänger für jeden Knoten
    priority_queue = [(0, start)]  # Min-Heap mit (Distanz, Knoten)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Knoten mit geringster Distanz

        # Wenn eine kürzere Distanz gefunden wurde, überspringe diesen Eintrag
        if current_distance > distances[current_node]:
            continue

        # Überprüfe alle Nachbarn des aktuellen Knotens
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Wenn ein kürzerer Weg gefunden wurde, aktualisiere
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

def reconstruct_path(previous, start, target):
    """
    Rekonstruiert den kürzesten Weg von Start zu Ziel.

    :param previous: Dictionary mit Vorgängerknoten
    :param start: Startknoten
    :param target: Zielknoten
    :return: Liste der Knoten im kürzesten Weg
    """
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()  # Umkehren, da wir vom Ziel zum Start zurückverfolgt haben

    if path[0] == start:
        return path
    else:
        return []  # Kein Weg gefunden

def display_results(distances, previous, start):
    """
    Zeigt die Ergebnisse in tabellarischer Form an.

    :param distances: Dictionary mit den kürzesten Distanzen zu jedem Knoten
    :param previous: Dictionary mit den Vorgängerknoten
    :param start: Startknoten
    """
    table = PrettyTable()
    table.field_names = ["Knoten", "Distanz vom Start", "Vorgänger"]

    for node in distances:
        table.add_row([node, distances[node], previous[node]])

    print(f"Ergebnisse für Startknoten '{start}':")
    print(table)

# Beispielgraph
graph = {
    'A': {'B': 100, 'D': 50},
    'B': {'C': 100, 'E': 250},
    'C': {'E': 50},
    'D': {'E': 250},
    'E': {}
}

# Beispielnutzung
start_node = 'A'
distances, previous = dijkstra(graph, start_node)

# Ergebnisse anzeigen
display_results(distances, previous, start_node)

# Kürzesten Weg zu einem Zielknoten anzeigen
target_node = 'E'
path = reconstruct_path(previous, start_node, target_node)
print(f"\nKürzester Weg von {start_node} nach {target_node}: {path}")
