"""
# Evaluating a clustering
# # Can check correspondence with e.g. iris species
# # ... but what if there are no species to check against?
# # Measure quality of a clustering
# # Informs choice of how many clusters to look for

# Cross tabulation with pandas
# # Clusters vs species is a "cross-tabulation"
# # Use the pandas library
# # Given the species of each sample as a list species
print(species)

# Aligning labels and species
import pandas as pd
df = pd.DataFrame({'labels':labels,'species': species})
print(df)

# Cros of labels and species
ct = pd.crosstab(df['labels'],df['species'])
print(ct)
# # How to evaluate a clustering, if there were no species information?

# Measuring clustering quality
# # Using only samples and their cluster labels
# # A good clustering has tight clusters
# # Samples in each cluster bunched together

# Inertia measures clustering quality
# # Measures how spread out the clusters are (lower is beer)
# # Distance from each sample to centroid of its cluster
# # After fit() , available as aribute inertia_
# # k-means attempts to minimize the inertia when choosing clusters
from sklearn.cluster import KMeans

model = KMens(n_clusters=3)
model.fit(samples)
print(model.inertia_)

# The number of clusters
# # Clusterings of the iris dataset with different numbers of clusters
# # More clusters means lower inertia
# # What is the best number of clusters?

# How many clusters to choose?
# # A good clustering has tight clusters (so low inertia)
# # ... but not too many clusters!
# # Choose an "elbow" in the inertia plot
# # Where inertia begins to decrease more slowly
# # E.g., for iris dataset, 3 is a good choice
"""