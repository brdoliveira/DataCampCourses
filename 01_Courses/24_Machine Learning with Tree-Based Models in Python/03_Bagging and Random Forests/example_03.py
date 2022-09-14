"""
# Random Forests

# # Bagging 
# # # Base estimator: Decision Tree, Logistic Regression, Neural Net, ...
# # # Each estimator is trained on a district bootstrap sample of the training set
# # # Estimators use all features for training and prediction

# # Further Diversity with Random Forests
# # # Base estimator: Decision Tree
# # # Each estimator is trained on a different bootstrap sample having the same size as the training set
# # # RF introduces further randomization in the training of individual trees
# # # d features are sampled at each node without replacement
# # # # (d < total number of features)

# # Random Forests: Classification & Regression
# # # Classification:
# # # # Aggregates predictions by majority voting
# # # # RandomForestClassifier in scikit-learn
# # # Regression:
# # # # Aggregates predictions through averaging
# # # # RandomForestRegressor in scikit-learn

# # Random Forests Regressor in sklearn
# Basic imports
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
# Set seed for reproducibility
SEED = 1

# Split dataset into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=SEED
)

# Instantiate a random forests regressor 'rf' 400 estimators
rf = RandomForestRegressor(
    n_estimators=400,
    min_sample_leaft=0.12,
    random_state=SEED
)

# Fit 'rf' to the training set
rf.fit(X_train, y_train)
# Predict the test set labels 'y_pred'
y_pred = rf.predict(X_test)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred) ** (1/2)

# Print the test set RMSE
print('Test set RMSE of rf: {:.2f}'.format(rmse_test))

# # Feature Importance
# # # Tree-based methods: enable measuring the importance of each feature in prediction.
# # # In sklearn:
# # # # how much the tree nodes use a particular feature (weighted average) to reduce impurity
# # # # accessed using the attribute feature_importance_

# # Feature Importance in sklern
import pandas as pd
import matplotlib.pyplot as plt

# Create a pd.Series of features importances
importances_rf = pd.Series(rf.feature_importances_, index= X.columns)

# Sort importances_rf
sorted_importances_rf = importances_rf.sort_values()

# Make horizontal bar plot
sorted_importances_rf.plot(kind='barh', color='lightgreen')
plt.show();
"""