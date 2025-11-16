import networkx as nx

# Build the graph from the given edgelist
edges = [
    ("N1","N2"), ("N1","N3"), ("N1","N4"),
    ("N2","N3"), ("N2","N4"), ("N3","N4"),
    ("N5","N6"), ("N5","N7"), ("N5","N8"),
    ("N6","N7"), ("N6","N8"), ("N7","N8"),
    ("N9","N10"), ("N9","N11"), ("N9","N12"),
    ("N10","N11"), ("N10","N12"), ("N11","N12"),
    ("N4","N6"), ("N9","N6"), ("N10","N5"), ("N1","N8")
]

G = nx.Graph()
G.add_edges_from(edges)

# compute betweeness
bc = nx.betweenness_centrality(G)

# Find the node with highest centrality
top_actor = max(bc, key=bc.get)
top_value = bc[top_actor]

print("Highest Betweenness Centrality:", top_actor, bc[top_actor])

# Print top 3 actors for sanity check
top3 = sorted(bc.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3:", top3)
