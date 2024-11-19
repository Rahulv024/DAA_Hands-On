from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.insert(0, v)

    def topological_sort(self, nodes):
        visited = {node: False for node in nodes}
        stack = []
        for node in nodes:
            if not visited[node]:
                self.topological_sort_util(node, visited, stack)
        return stack

# Define nodes and edges for the example
nodes = ["undershorts", "pants", "belt", "shirt", "tie", "jacket", "socks", "shoes", "watch"]

# List of directed edges
edges = [
    ("undershorts", "pants"),
    ("pants", "belt"),
    ("pants", "shoes"),
    ("shirt", "belt"),
    ("shirt", "tie"),
    ("tie", "jacket"),
    ("belt", "jacket"),
    ("socks", "shoes")
]

# Create graph and add edges
g = Graph(len(nodes))
for u, v in edges:
    g.add_edge(u, v)

# Perform topological sort
print("Topological Sort:", g.topological_sort(nodes))

#OUTPUT:
#Topological Sort: ['watch', 'socks', 'shirt', 'tie', 'undershorts', 'pants', 'shoes', 'belt', 'jacket']
