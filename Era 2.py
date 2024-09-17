# Medieval Era - Introduction of Zeta Influence
import matplotlib.pyplot as plt

# Reuse points and edges from the Ancient Era
points_medieval = points_ancient
edges_medieval = edges_ancient

# Add Zeta factor at the center
zeta_coord_medieval = (0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the edges
for edge in edges_medieval:
    point1, point2 = edge
    x_values = [points_medieval[point1][0], points_medieval[point2][0]]
    y_values = [points_medieval[point1][1], points_medieval[point2][1]]
    ax.plot(x_values, y_values, 'k-', lw=2)

# Plot the nodes and Zeta
for point, coord in points_medieval.items():
    ax.plot(coord[0], coord[1], 'ro')
    ax.text(coord[0] * 1.1, coord[1] * 1.1, point, ha='center', va='center', fontsize=12)
ax.plot(zeta_coord_medieval[0], zeta_coord_medieval[1], 'bo', markersize=10)
ax.text(zeta_coord_medieval[0], zeta_coord_medieval[1], 'Zeta', ha='center', va='center', fontsize=12, color='blue')

# Add arrows to represent the Zeta factor's influence
zeta_arrow_props_medieval = dict(facecolor='green', edgecolor='black', arrowstyle='->', lw=2)
for point, coord in points_medieval.items():
    ax.annotate('', xy=coord, xytext=zeta_coord_medieval, arrowprops=zeta_arrow_props_medieval)

ax.set_aspect('equal')
ax.axis('off')
plt.title("Medieval Era: Zeta Influence Introduction")
plt.show()
