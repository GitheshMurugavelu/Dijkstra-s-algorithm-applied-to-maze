import heapq

def dijkstra(graph, start, end):
    # Priority queue for the nodes to explore
    queue = [(0, start)]
    # Store the shortest distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Store the shortest path
    previous = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    return path, distances[end]

# Example Maze Graph (nodes and distances between them)
maze = {
    'A': {'B': 1, 'P': 1},
    'B': {'A': 1, 'C': 1},
    'C': {'B': 1, 'D': 1, 'K': 1},
    'D': {'C': 1, 'E': 1, 'G': 1},
    'E': {'D': 1, 'F': 1},
    'F': {'E': 1, 'G': 1},
    'G': {'D': 1, 'F': 1, 'H': 1},
    'H': {'I': 1, 'J': 1, 'G': 1},
    'I': {'H': 1},
    'J': {'K': 1, 'L': 1, 'H': 1},
    'K': {'C': 1, 'J': 1, 'M': 1},
    'L': {'M': 1, 'J': 1},
    'M': {'L': 1, 'K': 1, 'N': 1},
    'N': {'M': 1, 'O': 1},
    'O': {'P': 1, 'N': 1},
    'P': {'O': 1, 'A': 1}
}

# Set the start and end points
start_node = 'A'
end_node = 'F'

# Run the algorithm
shortest_path, total_distance = dijkstra(maze, start_node, end_node)

# Print results
print("Shortest path:", shortest_path)
print("Total distance:", total_distance)
