"""
# Cross-validation

# Cross-validation motivation
# # Model performance is dependent on the way we split up the data
# # Not representative of the model's ability to generalize to unseen data
# # Solution: Cross-validation!

# Cross-validation and model performance
# # 5 folds = 5-fold CV
# # 10 folds = 10-fold CV
# # k folds = k-fold CV
# # More folds = More computationally expensive
"""
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# Predictions blood glucose levels
diabetes_df = pd.read_csv("./data/diabetes_clean.csv")
print(diabetes_df.head())

# Creating feature and target arrays
X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values
print(type(X), type(y))

# Cross-validation in scikit-learn
kf = KFold(n_splits=6, shuffle=True, random_state=42)
reg = LinearRegression()
cv_results = cross_val_score(reg, X, y, cv=kf)

# Evaluating cross-valuation peformance
print(cv_results)

print(np.mean(cv_results),np.std(cv_results))

print(np.quantile(cv_results,[0.025,0.975]))