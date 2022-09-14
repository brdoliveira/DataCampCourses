"""
# Hyperparameter tuning
# # Ridge/lasso regression: Choosing alpha
# # KNN: Choosing n_neighbors
# # Hyperparameters: Parameters we specify before fitting the model
# # # Like alpha and n_neighbors

# Choosing the correct hyperparameters
# # 1. Try lots of dierent hyperparameter values
# # 2. Fit all of them separately
# # 3. See how well they perform
# # 4. Choose the best performing values

# # This is called hyperparameter tuning
# # It is essential to use cross-validation to avoid overffiting to the test set
# # We can still split the data and perform cross-validation on the training set
# # We withhold the test set for nal evaluation
"""
from sklearn.model_selection import KFold, GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression, Ridge
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Predictions blood glucose levels
diabetes_df = pd.read_csv("./data/diabetes_clean.csv")
print(diabetes_df.head())

# Creating feature and target arrays
X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values
print(type(X), type(y))


# Logistic regression in scikit-learn
logreg = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)

# GridSearchCV in scikit-learn
kf = KFold(n_splits=5, shuffle=True, random_state=42)
param_grid = {"alpha": np.arange(0.0001, 1, 10),"solver": ["sag","lsqr"]}
ridge = Ridge()
ridge_cv = GridSearchCV(ridge, param_grid, cv=kf)
ridge_cv.fit(X_train, y_train)
print(ridge_cv.best_params_, ridge_cv.best_score_)

# Limitations and an alternative approach
# # 3-fold cross-validation, 1 hyperparameter, 10 total values = 30 ts
# # 10 fold cross-validation, 3 hyperparameters, 30 total values = 900 ts

# RanomizedSearchCV
kf = KFold(n_splits=5, shuffle=True, random_state=42)
param_grid = {'alpha': np.arange(0.0001, 1, 10),
              "solver": ['sag','lsqr']}
ridge = Ridge()
ridge_cv = RandomizedSearchCV(ridge, param_grid, cv=kf, n_iter=2)
ridge_cv.fit(X_train, y_train)
print(ridge_cv.best_params_, ridge_cv.best_score_)

# Evaluating on the test set
test_score = ridge_cv.score(X_test, y_test)
print(test_score)