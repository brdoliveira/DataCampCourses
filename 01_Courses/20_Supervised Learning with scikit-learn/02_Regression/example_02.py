"""
# The basics of linear regression

# Regression mechanics
# # y = ax + b
# # # Simple linear regression uses one feature
# # # # y = target
# # # # x = single feature
# # # # a, b = parameters/coefficients of the model - slope, intercept
# # # How do we choose a and b?
# # # # Define an error function for any given line
# # # # Choose the line that minimizes the error function
# # # Error function = loss function = cost function

# Linear regression in higher dimensions
# # y = a1 x1 + a2 x2 + b
# # To fit a linear regression model here:
# # # Need to specify 3 variables: a1 , a2 , b
# # In higher dimensions:
# # # Known as multiple regression
# # # Must specify coecients for each feature and the variable b
# y = a1 x1 + a2 x2 + a3 x3 + ... + an xn + b
# # scikit-learn works exactly the same way:
# # # Pass two arrays: features and target
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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
reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)

# R-squared
# # R^2 : quanties the variance in target values explained by the features
# # # Values range from 0 to 1
reg_all.score(X_test,y_test)

# RMSE in scikit-learn
# Measure RMSE in the same units at the target variable
# RMSE = MSE * 0.5
# # MSE is measured in target units, squared
mean_squared_error(y_test, y_pred, squared=False)