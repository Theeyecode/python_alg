import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, value):
        if value not in self.adjacency_list:
            self.adjacency_list[value] = []

    def add_edge(self, from_vertex, to_vertex, distance):
        edge = Edge(to_vertex, distance)
        self.adjacency_list[from_vertex].append(edge)

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph.adjacency_list}
    previous = {vertex: None for vertex in graph.adjacency_list}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        # If this vertex has been visited after its shortest path was found
        if current_distance > distances[current_vertex]:
            continue
        
        for edge in graph.adjacency_list[current_vertex]:
            neighbor = edge.vertex
            new_distance = current_distance + edge.distance
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heapq.heappush(queue, (new_distance, neighbor))
                
    return distances, previous

# Example usage:

# Example usage:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_vertex("H")


graph.add_edge("A", "B", 1.8)
graph.add_edge("A", "C", 1.5)
graph.add_edge("A", "D", 1.4)
graph.add_edge("D", "G", 2.4)
graph.add_edge("D", "F", 2.7)
graph.add_edge("C", "F", 2.1)
graph.add_edge("C", "E", 1.8)
graph.add_edge("B", "E", 1.6)
graph.add_edge("F", "G", 1.3)
graph.add_edge("F", "H", 1.2)
graph.add_edge("E", "F", 1.4)
graph.add_edge("E", "H", 1.6)
graph.add_edge("G", "H", 1.5)
