import heapq


def shortest_path(network, source):
    # Priority queue to store (distance, node)
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))

    # Distance dictionary to store the shortest distance to each node
    node_distances = {point: float('inf') for point in network}
    node_distances[source] = 0

    # Dictionary to store the shortest path
    previous_points = {point: None for point in network}

    while priority_queue:
        current_cost, current_point = heapq.heappop(priority_queue)

        # If the current cost is greater than the stored distance, skip
        if current_cost > node_distances[current_point]:
            continue

        # Explore neighbors
        for neighbor, weight in network[current_point]:
            new_cost = current_cost + weight

            # If a shorter path is found, update distances and push to the queue
            if new_cost < node_distances[neighbor]:
                node_distances[neighbor] = new_cost
                previous_points[neighbor] = current_point
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return node_distances, previous_points


# Graph definition with new node names and distances
network = {
    'f': [('g', 8), ('h', 10)],
    'g': [('h', 4), ('j', 7)],
    'h': [('g', 2), ('j', 5), ('k', 12)],
    'j': [('k', 3)],
    'k': [('f', 9), ('j', 14)]
}

# Run the shortest path algorithm from source node 'f'
node_distances, previous_points = shortest_path(network, 'f')

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
