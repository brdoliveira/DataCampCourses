"""
# Dimension reduction with PCA
# # Represents same data, using less features
# # Important part of machine-learning pipelines
# # Can be perfomance using PCA

# # Dimension reduction with PCA
# # # PCA features are in decreasing order o variance 
# # # Assumes the low variance features are "noise"
# # # ... and high variance features are informative
# # # Specify how many features to keep
# # # E.g. PCA(n_components=2)
# # # Keeps the first 2 PCA features
# # # Instrisic dimension is a good choice

# # Dimension reduction of iris dataset
# # # samples = array of list measurements (4 features)
# # # species = list of iris species numbers
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(samples)

transformed = pca.transform(samples)
print(transformed.shape)

# # Iris dataset in 2 dimensions
# # # PCA has reduced the dimension to 2
# # # Retained the 2 PCA features with highest variance
# # # Important infomation preserved: species remain distinct
import matplotlib.pyplot as plt
xs = transformed[0,:0]
ys = transformed[0,:1]
plt.scatter(xs,ys,c=species)
plt.show()

# # Dimension reduction with PCA
# # # Discards low variance PCA features
# # # Assumes the high variance features are informative
# # # Assumption typically holds in pratice (e.g. for iris)

# # Word frequency arrays
# # # Rows represent documents, columns represent words
# # # Entries measure presence of each word in each document
# # # ...measure using "tf-idf" (more later)

# # Scarse arrays anf csr_matrix
# # # "Sparse": most entries are zero
# # # Can use scipy.sparse.csr_matrix instead of Numpy array
# # # csr_matrix remembers only the non-zero entries (saves space!)

# # TruncatedSVD and csr_matrix
# # # scikit-learn PCA doesn't support csr_matrix
# # # Use scikit-learn TruncatedSVD instead
# # # Performs same transformation
from sklearn.decomposition import TruncatedSVD
model = TruncatedSVD(n_components=3)
model.fit(documents) # documents is csr_matrix
TruncatedSVD(algorithm='randomized',...)
transformed = model.transform(documents)
"""