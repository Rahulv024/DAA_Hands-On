from collections import defaultdict

def depth_first_search(connections, start_node):
    adjacency_list = defaultdict(list)
    for source, target in connections:
        adjacency_list[source].append(target)

    visited_nodes = set()

    def dfs(node):
        if node not in visited_nodes:
            print(node, end=' ')
            visited_nodes.add(node)
            for neighbor in adjacency_list[node]:
                dfs(neighbor)

    dfs(start_node)
    print()

# Define connections for DFS example
connections_dfs = [
    ("u", "v"),
    ("u", "x"),
    ("v", "y"),
    ("y", "x"),
    ("x", "v"),
    ("w", "z"),
    ("w", "y"),
    ("z", "z")  # self-loop
]

print("Depth-First Search from 'u':")
depth_first_search(connections_dfs, 'u')

#OUTPUT
#Depth-First Search from 'u':
#u v y x 
