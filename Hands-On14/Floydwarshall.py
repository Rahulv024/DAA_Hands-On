def shortest_path_all_pairs(network):
    # Initialize distances as infinity
    points = list(network.keys())
    point_indices = {point: idx for idx, point in enumerate(points)}
    n = len(points)

    # Initialize distance and next_point matrices
    node_distances = [[float('inf')] * n for _ in range(n)]
    next_point = [[None] * n for _ in range(n)]

    # Distance to self is 0
    for i in range(n):
        node_distances[i][i] = 0

    # Add edges to the distance matrix
    for start in network:
        for end, weight in network[start]:
            i, j = point_indices[start], point_indices[end]
            node_distances[i][j] = weight
            next_point[i][j] = end

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if node_distances[i][k] + node_distances[k][j] < node_distances[i][j]:
                    node_distances[i][j] = node_distances[i][k] + node_distances[k][j]
                    next_point[i][j] = next_point[i][k]

    return node_distances, next_point, points


# Print matrix
def print_matrix(matrix, points):
    print("   ", "  ".join(points))
    for i, row in enumerate(matrix):
        print(f"{points[i]:<3}", "  ".join(f"{val if val != float('inf') else '∞':<3}" for val in row))


# Graph definition with updated node names and distances
network = {
    'f': [('g', 8), ('h', 10)],
    'g': [('h', 4), ('j', 7)],
    'h': [('g', 2), ('j', 5), ('k', 12)],
    'j': [('k', 3)],
    'k': [('f', 9), ('j', 14)]
}

# Run Floyd-Warshall algorithm
node_distances, next_point, points = shortest_path_all_pairs(network)

# Display results
print("Distance matrix:")
print_matrix(node_distances, points)


#OUTPUT:
#Distance matrix:
#    f  g  h  j  k
#f   0    8    10   15   18 
#g   19   0    4    7    10 
#h   17   2    0    5    8  
#j   12   20   22   0    3  
#k   9    17   19   14   0
