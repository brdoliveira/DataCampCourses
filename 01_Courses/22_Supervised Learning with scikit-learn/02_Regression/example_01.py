"""
# Introduction to regression
"""
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

# Predictions blood glucose levels
diabetes_df = pd.read_csv("./data/diabetes_clean.csv")
print(diabetes_df.head())

# Creating feature and target arrays
X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values
print(type(X), type(y))

# Making prediction from a single feature
X_bmi = X[:, 3]
print(y.shape, X_bmi.shape)

X_bmi = X_bmi.reshape(-1, 1)
print(X_bmi.shape)

# Plotting glucose vs. body mass index
reg = LinearRegression()

reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi)

plt.scatter(X_bmi, y)
plt.plot(X_bmi, predictions)
plt.ylabel("Blood Glucose (mg/dl)")
plt.xlabel("Body Mass Index")
plt.show()