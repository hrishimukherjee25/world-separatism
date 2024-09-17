import matplotlib.pyplot as plt
import networkx as nx

# Initialize a graph
G = nx.DiGraph()

# Define nodes (icebergs) with attributes
icebergs = {
    'Iceberg A': {'influence': 10},
    'Iceberg B': {'influence': 8},
    'Iceberg C': {'influence': 6},
    'Iceberg D': {'influence': 5}
}

# Add nodes with attributes
for iceberg, attr in icebergs.items():
    G.add_node(iceberg, size=attr['influence'])

# Define edges (interactions)
interactions = [
    ('Iceberg A', 'Iceberg B', 4),
    ('Iceberg B', 'Iceberg C', 2),
    ('Iceberg C', 'Iceberg D', 3),
    ('Iceberg D', 'Iceberg A', 1)
]

# Add edges with weights
for u, v, weight in interactions:
    G.add_edge(u, v, weight=weight)

# Node sizes based on influence
node_sizes = [G.nodes[n]['size'] * 100 for n in G.nodes]

# Edge weights
edge_weights = [G[u][v]['weight'] for u, v in G.edges]

# Draw the network
pos = nx.spring_layout(G)  # Layout algorithm
nx.draw(G, pos, with_labels=True, node_size=node_sizes, edge_color='blue', node_color='skyblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}' for u, v, w in interactions})

# Add title and show plot
plt.title("Network of Icebergs in a Storm Drain")
plt.show()
