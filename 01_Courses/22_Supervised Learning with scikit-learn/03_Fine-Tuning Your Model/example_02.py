"""
# Logistic regression and the ROC courve

# Logistic regression for binary classification
# # Logistic regression is used for classication problems
# # Logistic regression outputs probabilities
# # If the probability, p > 0.5:
# # # The data is labeled 1
# # If the probability, p < 0.5:
# # # The data is labeled 0
"""
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import pandas as pd

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
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

# Predicting probabilities
y_pred_probs = logreg.predict_proba(X_test)[:, 1]
print(y_pred_probs[0])

# Probability thresholds
# # By default, logistic regression threshold = 0.5
# # Not specic to logistic regression
# # # KNN classiers also have thresholds
# # What happens if we vary the threshold?

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_probs)
plt.plot([0, 1], [0, 1],'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logistic Regression ROC Curve')
plt.show()

# ROC AUC in scikit-learn
print(roc_auc_score(y_test,y_pred_probs))