"""
# How good is your model?

# Classification metrics
# # Measuring model performance with accuracy:
# # # Fraction of correctly classied samples
# # # Not always a useful metric

# Class imbalance
# # Classication for predicting fraudulent bank transactions
# # # 99% of transactions are legitimate; 1% are fraudulent
# # Could build a classier that predicts NONE of the transactions are fraudulent
# # # 99% accurate!
# # # But terrible at actually predicting fraudulent transactions
# # # Fails at its original purpose
# # Class imbalance: Uneven frequency of classes
# # Need a different way to assess performance

# Confusion matrix for assessing classification performance
# # Confusion matrix

# Assessing classification performance
# # Accuracy: (tp + tn) / (tp + tn + fp + fn)

# Precision (True Positive + False Positive)
# # true positives / (true positives + false positives)
# # # High precision = lower false positive rate
# # # High precision: Not many legitimate transactions are predicted to be fraudulent

# Recall (True Positive + False Negative)
# # true positives / (true positives + false negatives)
# # # High recall = lower false negative rate
# # # High recall: Predicted most fraudulent transactions correctly

# F1 score
# # F1 score: 2 * (precision * recall / precision + recall)
"""
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# Predictions blood glucose levels
diabetes_df = pd.read_csv("./data/diabetes_clean.csv")
print(diabetes_df.head())

# Creating feature and target arrays
X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values
print(type(X), type(y))

knn = KNeighborsClassifier(n_neighbors=7)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,random_state=42)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(confusion_matrix(y_test, y_pred)) # Confusion matrix in scikit-learn

print(classification_report(y_test, y_pred)) # Classification report in scikit-learn