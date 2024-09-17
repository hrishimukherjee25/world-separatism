import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Each row represents a story, and each column represents the presence/importance of a concept in that story
data = np.array([
    [3, 1, 2, 4, 3, 1, 0, 2, 1, 4],  # Story 1 (Future)
    [2, 4, 3, 1, 2, 0, 3, 2, 3, 1],  # Story 2 (Intergalactic)
    [4, 1, 2, 0, 3, 2, 1, 4, 2, 3],  # Story 3 (Boltzmann Brain and Multiverse)
])

# Labels for the concepts/lemmas
concepts = ['Diaspora', 'Warp Drive', 'Multiverse', 'Quantum', 'Alien', 'Consciousness', 'Conflict', 'Exploration', 'Peace', 'Evolution']

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data, annot=True, cmap='YlOrRd', xticklabels=concepts, yticklabels=['Future', 'Intergalactic', 'Boltzmann Multiverse'], cbar=True)

plt.title("Heatmap of Lemmas Across 3 Extension Stories")
plt.show()
