"""
# Measuring model perfomance

# Measuring model performance
# # In classication, accuracy is a commonly used metric
# # Accuracy: correct predictions / total observations

# Measuring model performance
# # How do we measure accuracy?
# # Could compute accuracy on the data used to t the classier
# # NOT indicative of ability to generalize
"""
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
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

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=21, stratify=y)
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))

# Model complexity
# # Larger k = less complex model = can cause undering
# # Smaller k = more complex model = can lead to overing

# Model complexity and over/underfitting
train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1, 26)

for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors=neighbor)
    knn.fit(X_train, y_train)
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)

# Plotting our results
plt.figure(figsize=(8, 6))
plt.title("KNN: Varying Number of Neighbors")
plt.plot(neighbors, train_accuracies.values(), label="Training Accuracy",color="blue")
plt.plot(neighbors, test_accuracies.values(), label="Testing Accuracy",color="red")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()