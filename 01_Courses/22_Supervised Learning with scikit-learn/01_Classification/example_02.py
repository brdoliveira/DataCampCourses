"""
# The classification challenge

# Classifying labels of unseen data
# 1. Build a model
# 2. Model learns from the labeled data we pass to it
# 3. Pass unlabeled data to the model as input
# 4. Model predicts the labels of the unseen data
# # Labeled data = training data

# k-Nearest Neighbors
# # Predict the label of a data point by
# # # Looking at the k closest labeled data points
# # # Taking a majority vote
"""
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

churn_df = pd.read_csv("./data/telecom_churn_clean.csv")

X = churn_df[["total_day_charge","total_eve_charge"]].values
y = churn_df["churn"].values
print(X.shape, y.shape)

knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X, y)

# Predicting on unlabeled data
X_new = np.array([[56.8, 17.5],
                [24.4, 24.1],
                [50.1, 10.9]])
print(X_new.shape)

predictions = knn.predict(X_new)
print('Predictions: {}'.format(predictions))