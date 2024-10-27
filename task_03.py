import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph.edges}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 5)
    graph.add_edge("B", "D", 10)
    graph.add_edge("C", "D", 3)
    graph.add_edge("D", "E", 1)
    graph.add_edge("C", "E", 8)

    start_vertex = "A"
    distances = dijkstra(graph, start_vertex)

    print(f"Найкоротші відстані від вершини '{start_vertex}':")
    for vertex, distance in distances.items():
        print(f"Відстань до {vertex}: {distance}")
