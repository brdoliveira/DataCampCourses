"""
# Visualizing hierarchies

# # Visualizations communicate insight
# # # "t-SNE" : Creates a 2D map of a dataset (later)
# # # "Hierarchical clustering" (this video)

# # A hierarchy of groups
# # # Groups of living things can form a hierarchy
# # # Clusters are contained in one another

# # Eurovision scoring dataset
# # # Countries gaves scores to songs perfomed at the Eurovision 2016
# # # 2D array of scores
# # # Rows are countries, column are songs

# # Hierarchical clustering
# # # Every begings in a separate cluster
# # # At each step, the two closest clusters are merged
# # # Continue the until all countries in a single cluster
# # # This is "agglomerative" hierarchical clustering

# # The dendrogram of a hierarchical clustering
# # # Read from the bottom up
# # # Vertical lines represent clusters

# # Hierarchical clustering with SciPy
# # # Given samples (the array of scores), and country_names
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendogram

mergings = linkage(samples, method='complete')
dendogram(mergings,
        labels=country_names,
        leaf_rotation=90,
        leaf_font_size=6)
plt.show()
"""