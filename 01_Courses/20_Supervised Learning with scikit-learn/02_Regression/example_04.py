"""
# Regularized regression

# Why regularize?
# # Recall: Linear regression minimizes a loss function
# # It chooses a coefficient, a, for each feature variable, plus b
# # Large coefficient can lead to overing
# # Regularization: Penalize large coefficient

# Ridge regression
# # Loss function = OLS loss function +
# # Ridge penalizes large positive or negative coefficients
# # α: parameter we need to choose
# # Picking α is similar to picking k in KNN
# # Hyperparameter: variable used to optimize model parameters
# # α controls model complexity
# # α = 0 = OLS (Can lead to overffiting)
# # Very high α: Can lead to underffiting
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
import matplotlib.pyplot as plt
import pandas as pd

# Predictions blood glucose levels
diabetes_df = pd.read_csv("./data/diabetes_clean.csv")
print(diabetes_df.head())

# Creating feature and target arrays
X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values
print(type(X), type(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=42)

scores = []
for alpha in [0.1, 1.0, 10.0, 100.0, 1000.0]:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    y_pred = ridge.predict(X_test)
    scores.append(ridge.score(X_test, y_test))
print(scores)

# Lasso regression for feature selection
# # Lasso can select important features of a dataset
# # Shrinks the coecients of less important features to zero
# # Features not shrunk to zero are selected by lasso

# Lasso for feature selection in scikit-learn
names = diabetes_df.drop("glucose", axis=1).columns
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X, y).coef_

plt.bar(names, lasso_coef)
plt.xticks(rotation=45)
plt.show()