"""
# Non-negative matrix factorization
# # NMF = "non-negative matrix factorization"
# # Dimension reduction technique
# # NMF models are intepretable (unlike PCA)
# # Easy to interpret mean easy to explain !
# # However, all sample features must be non-negative (>=0)

# # Interpretable parts
# # # NMF expresses documents as combinations of topics (or "themes")
# # # NMF expresses images as combinations of patterns

# # Using scikit-learn NMF
# # # Follow fit() / transform() pattern
# # # Must specify number of components e.g. NMF(n_components=2)
# # # Works with NumPy arrays and with csr_matrix

# # Example word-frequency array
# # # Word frequency array, 4 words, many documents
# # # Measure presence of words in each document using "tf-idf"
# # # # "tf" = frequency of word in document
# # # # "idf" = reduces influences of frequent word

# #  Example usage of NMF
# # #  'samples' is the word-frequency
from sklearn.decomposition import NMF
model = NMF(n_components=2)
model.fit(samples)
nmf_features = model.transform(samples)

# # NMF components
# # # NMF has components
# # # ...just like PCA has principal components
# # # Dimension of components = dimension of samples
# # # Entries are non-negative
print(model.components_)

# # NMF features
# # # NMF feature values are non-negative
# # # Can be used to reconstruct the samples
# # # ... combine feature values with components
print(nmf_features)

# # Reconstruction of a sample
print(samples[i,:])
print(nmf_features[i,:])

# # Sample reconstruction
# # # Multiply components by feature values, and add up
# # # Can also be expressed as a product of matrices
# # # This is the "Matrix Factorization" in "NMF"

# # NMF fits to non-negative data only
# # # Word frequencies in each document
# # # Images encoded as arrays
# # # Audio spectrograms
# # # Purchase histories on e-commerce sites
# # # ...and many here!

"""