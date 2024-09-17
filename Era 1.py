# Ancient Era - Basic Node Points and Edges Visualization
import matplotlib.pyplot as plt

# Define the node points and their coordinates in the diamond shape
points_ancient = {
    "Authoritarianship": (0, 1),
    "Espionage": (-1, 0),
    "Anarchy": (0, -1),
    "Migration": (1, 0)
}

# Define the connections (edges) between the points
edges_ancient = [
    ("Authoritarianship", "Espionage"),
    ("Espionage", "Anarchy"),
    ("Anarchy", "Migration"),
    ("Migration", "Authoritarianship"),
]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the edges
for edge in edges_ancient:
    point1, point2 = edge
    x_values = [points_ancient[point1][0], points_ancient[point2][0]]
    y_values = [points_ancient[point1][1], points_ancient[point2][1]]
    ax.plot(x_values, y_values, 'k-', lw=2)

# Plot the nodes
for point, coord in points_ancient.items():
    ax.plot(coord[0], coord[1], 'ro')
    ax.text(coord[0] * 1.1, coord[1] * 1.1, point, ha='center', va='center', fontsize=12)

ax.set_aspect('equal')
ax.axis('off')
plt.title("Ancient Era: Basic Geometry")
plt.show()
