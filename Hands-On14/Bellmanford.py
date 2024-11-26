def find_shortest_paths(network, source):
    # Initialize distances to all vertices as infinity and the start node as 0
    node_distances = {point: float('inf') for point in network}
    node_distances[source] = 0

    # Dictionary to store the shortest path
    previous_points = {point: None for point in network}

    # Flatten the graph edges into a list of (source, destination, weight)
    connections = [(start, end, weight) for start in network for end, weight in network[start]]

    # Relax edges |V| - 1 times
    for _ in range(len(network) - 1):
        for start, end, weight in connections:
            if node_distances[start] + weight < node_distances[end]:
                node_distances[end] = node_distances[start] + weight
                previous_points[end] = start

    # Check for negative weight cycles
    for start, end, weight in connections:
        if node_distances[start] + weight < node_distances[end]:
            raise ValueError("Network contains a negative weight cycle")

    return node_distances, previous_points


# Graph definition with updated node names and distances
network = {
    'f': [('g', 8), ('h', 10)],
    'g': [('h', 4), ('j', 7)],
    'h': [('g', 2), ('j', 5), ('k', 12)],
    'j': [('k', 3)],
    'k': [('f', 9), ('j', 14)]
}

# Run Bellman-Ford algorithm from source node 'f'
try:
    node_distances, previous_points = find_shortest_paths(network, 'f')

    # Display results
    print("Shortest distances from source 'f':")
    for point, distance in node_distances.items():
        print(f"{point}: {distance}")

    print("\nShortest paths from source 'f':")
    for point in previous_points:
        path = []
        current = point
        while current is not None:
            path.insert(0, current)
            current = previous_points[current]
        print(f"Path to {point}: {' -> '.join(path)}")
except ValueError as e:
    print(e)


#OUTPUT:
#Shortest distances from source 'f':
#f: 0
#g: 8
#h: 10
#j: 15
#k: 18

#Shortest paths from source 'f':
#Path to f: f
#Path to g: f -> g
#Path to h: f -> h
#Path to j: f -> g -> j
#Path to k: f -> g -> j -> k
