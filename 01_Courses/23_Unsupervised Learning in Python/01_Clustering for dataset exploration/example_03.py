"""
# Transforming features for better clusterings

# Piedmont wines dataset
# # 178 samples from 3 distinct varieties of red wine: Barolo, Grignolino and Barbera
# # Features measure chemical composition e.g. alcohol content
# # Visual properties like "color intensity"

# Clustering the wines
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
labels = model.fit_predict(samples)

# Clusters vs. varietes
df = pd.DataFrame({'labels': labels,
                   'varieties': varieties})
ct = pd.crosstab(df['labels'], df['varieties'])
print(ct)

# Feature variances
# # The wine features have very different variances!
# # Variance of a feature measures spread of its values

# StandardScaler
# # In kmeans: feature variance = feature influence
# # StandardScaler transforms each feature to have mean 0 and variance 1
# # Features are said to be "standardized"
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(samples)
StandardScaler(copy=True, with_men=True, with_std=True)
samples_scaled = scaler.transform(samples)

# Similar methods
# # StandardScaler and KMeans have similar methods
# # Use fit() / transform() with StandardScaler
# # Use fit() / predict() with KMeans

# StandardScaler, then KMeans
# # Need to perform two steps: StandardScaler , then KMeans
# # Use sklearn pipeline to combine multiple steps
# # Data flows from one step into the next

# Pipelines combine multiple steps
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
scaler = StandardScaler()
kmeans = KMeans(n_clusters=3)

from sklearn.pipeline import make_pipeline
pipeline = make_pipeline(scaler, kmeans)
pipeline.fit(samples)

labels = pipeline.predict(samples)

# sklearn preprocessing steps
# # StandardScaler is a "preprocessing" step
# # MaxAbsScaler and Normalizer are other examples
"""