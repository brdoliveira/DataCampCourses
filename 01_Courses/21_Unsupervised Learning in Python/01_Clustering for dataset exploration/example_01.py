"""
# Unsupervised learning
# # Unsupervised learning finnds patterns in data
# # E.g., clustering customers by their purchases
# # Compressing the data using purchase patterns (dimension reduction)

# Supervised vs unsupervised learning
# # Supervised learning finds patterns for a prediction task
# # E.g., classify tumors as benign or cancerous (labels)
# # Unsupervised learning finds patterns in data
# # ...but without a specic prediction task in mind

# Iris dataset
# # Measurements of many iris plants
# # Three species of iris:
# # # setosa
# # # versicolor
# # # virginica
# # Petal length, petal width,sepal length, sepal width(the features of the dataset)

# Arrays, features & samples
# # 2D NumPy array
# # Columns are measurements (the features)
# # Rows represent iris plants (the samples)

# Iris data is 4-dimensional
# # Iris samples are points in 4 dimensional space
# # Dimension = number of features
# # Dimension too high to visualize!
# # ... but unsupervised learning gives insight

# k-means clustering
# # Finds clusters of samples
# # Number of clusters must be specified
# # Implemented in sklearn ("scikit-learn")

print(samples)

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(samples)

labels = model.predict(samples)
print(labels)

# Cluster labels for new samples
# # New samples can be assigned to existing clusters
# # k-means remembers the mean of each cluster (the "centroids")
# # Finds the nearest centroid to each new sample
print(new_samples)

new_labels = model.predict(new_samples)
print(new_labels)

# Scatter plots
# # Scatter plot of sepal length vs. petal length
# # Each point represents an iris sample
# # Color points by cluster labels
# # PyPlot ( matplotlib.pyplot )

import matpltot.pyplot as plt
xs = samples[:,0]
ys = samples[:,2]
plt.sctter(xs,ys,c=labels)
plt.show()
"""