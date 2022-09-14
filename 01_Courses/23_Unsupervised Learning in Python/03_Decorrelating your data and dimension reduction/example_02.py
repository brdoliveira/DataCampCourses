"""
# Intrinsic dimension

# # Intrisic dimension of a flight path
# # # 2 features: longitude and latitude at points along a flight path
# # # Dataset appears to be 2-dimensional
# # # But can approximate using one feature: displacement along flight path
# # # Is intrinsically 1-dimensional

# # Intrinsic dimension
# # # Intrinsic dimension = number of features needed to approximate the dataset
# # # Essential idea behind dimension reduction
# # # What is the most compact representation of the samples?
# # # Can be derected with PCA

# # Versicolor dataset
# # # "versicolor", one of the iris species
# # # Only 3 features: spepal length, sepal width, and petal width
# # # Samples are points in 3D space

# # Versicolor dataset has intrisic dimension 2
# # # Samples lie close to be a flat 2-dimensional sheet
# # # So can be approximated using 2 features

# # PCA identifies intrisic dimension
# # # Scatter plots work only if samples have 2 or 3 features
# # # PCA identifies intrisic dimension when samples have any number of features
# # # Intrisic dimension = number of PCA features with significant variance

# # Variance and intrisic dimension
# # # Intrisic dimension is number of PCA features with significant variance
# # # In our example: the first two PCA features
# # # So intrisic is 2

# # Plotting the variances of PCA features
# # # samples = array of versicolor samples
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
pca = PCA()
pca.fit(samples)

features = range(pca.n_components_)

plt.bar(features, pca.explained_variance_)
plt.xticks(features)
plt.ylabel('variance')
plt.xlabel('PCA feature')
plt.show()

# # Intrisic dimension can be ambiguous
# # # Intrisic dimension is an idealization
# # # ... there is not always one correct answer!
# # # Piedmont wines: could argue for 2, or for 3, or more
"""