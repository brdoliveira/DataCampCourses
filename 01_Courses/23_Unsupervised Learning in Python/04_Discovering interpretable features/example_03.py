"""
# Building recommender system using NMF

# # Finding similar articles
# # # Engineer at a large online newspaper
# # # Task: recommended articles similar to article being read by customer
# # # Similar articles should have similar topics

# # Strategy
# # # Apply NMF to the word-frequency array
# # # NMF feature values describe the topics
# # # ...so similar documents have similar NMF feature values
# # # Compare NMF feature values?

# # Apply NMF to the word-frequency array
# # # 'articles' is a word frequency array
from sklearn.decomposition import NMF
nmf = NMF(n_components=6)
nmf_features = nmf.fit_transform(articles)

# # Strategy
# # # Apply NMF to the word-frequency array
# # # NMF feature values describe the topics
# # # ...so similar documents have similar NMF feature values
# # # Compare NMF feature values? 

# # Versions of articles
# # # Different versions of the same document have same topic proportions
# # # ...exact feature values may be different!
# # # E.g. because one version uses many meaningless words
# # # But all versions lie on the same line through the origion

# # Cosine Similarity
# # # Uses the angle between the lines
# # # Higher values means more similar
# # # Maximum value is 1, when angle is 0 degress

# # Calculating the cosune similarities
from sklearn.preprocessing import normalize
norm_features = normalize(nmf_features)
# if has index 23
current_article = norm_features[23,:]
similarities = norm_features.dot(current_article)
print(similarities)

# # DataFrames and labels
# # # Label similarities with the article titles, using DtaFrame
# # # Titles given as a list: titles
import pandas as pd
norm_features = normalize(nmf_features)
df = pd.DataFrame(norm_features, index=titles)
current_article = df.loc['Dog bites man']
similarities = df.dot(current_article)
print(similarities.nlargest())

"""