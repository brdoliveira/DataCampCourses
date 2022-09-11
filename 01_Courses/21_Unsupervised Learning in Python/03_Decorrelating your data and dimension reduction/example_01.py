"""
# Visualizing the PCA transformation

# # Dimension reduction
# # # More efficient storage and computation
# # # Remove less-informative "noise" features
# # # ...which cause problems for prediction talks, e.g. classification, regression

# # Principal Component Analysis
# # # PCA = "Principal Component Analysis"
# # # Fundamental dimension reduction technique
# # # First step "decorrelation" (considered here)
# # # Second step reduces dimension (considered later)

# # PCA aligns data with axes
# # # Rotate data samples to be alignedwith axes
# # # Shifts data samples so they have mean 0
# # # No information is lost

# # PCA follows the fit/transform pattern
# # # PCA is scikit-learn component like KMeans or StandardScaler
# # # fit() learns the transformation from given data
# # # transform() applies the learned transformation
# # # transform() can also be applied to new data

# # Using scikit-learn PCA
# # # samples = array of two features (total_phenols & od280)
from sklearn.decomposition import PCA
model = PCA()
model.fit(samples)
transformed = model.transform(samples)

# # PCA features
# # # Rows of transformed correspond to samples
# # # Columns of transformed are the "PCA features"
# # # Rows gives PCA feature values of corresponding samples
print(transformed)

# # PCA features are not correlated
# # # Features of dataset are often correlated, e.g. total_phenols and od280
# # # PCA aligns the data with axes
# # # Resulting PCA features are not linearly correlated ("decorrelation")

# # Pearson Correlation
# # # Measures linear correlation of features
# # # Value between -1 and 1
# # # Value of 0 means no lines correlation

# # Principal components
# # # "Principal components" = directions of variance
# # # PCA align principal components with the axes
# # #  Available as components_ attribute of PCA object
# # # Each row defines displacement from mean
print(model.components_)

"""