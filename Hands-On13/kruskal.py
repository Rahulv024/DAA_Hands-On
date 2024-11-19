class Edge:
    def __init__(self, cost, node1, node2):
        self.cost = cost
        self.node1 = node1
        self.node2 = node2

class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(vertices, edges):
    edges = sorted(edges, key=lambda e: e.cost)
    uf = UnionFind(vertices)
    mst_edges = []

    for edge in edges:
        if uf.find(edge.node1) != uf.find(edge.node2):
            uf.union(edge.node1, edge.node2)
            mst_edges.append(edge)

    return mst_edges

# Define vertices and edges for Kruskal's example
vertices_kruskal = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
edges_kruskal = [
    Edge(4, "a", "b"),
    Edge(8, "a", "h"),
    Edge(8, "b", "c"),
    Edge(11, "b", "h"),
    Edge(7, "c", "d"),
    Edge(4, "c", "f"),
    Edge(2, "c", "i"),
    Edge(6, "c", "g"),
    Edge(9, "d", "e"),
    Edge(14, "d", "f"),
    Edge(10, "e", "f"),
    Edge(2, "f", "g"),
    Edge(1, "g", "h"),
    Edge(7, "h", "i")
]

# Perform Kruskal's MST
mst_edges = kruskal(vertices_kruskal, edges_kruskal)
print("Kruskal's MST:")
for edge in mst_edges:
    print(f"Edge {edge.node1}-{edge.node2} with cost {edge.cost}")

#OUTPUT:
#Kruskal's MST:
#Edge g-h with cost 1
#Edge c-i with cost 2
#Edge f-g with cost 2
#Edge a-b with cost 4
#Edge c-f with cost 4
#Edge c-d with cost 7
#Edge a-h with cost 8
#Edge d-e with cost 9
