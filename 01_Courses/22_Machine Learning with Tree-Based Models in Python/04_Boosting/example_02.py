"""
# Gradient Boosting (GB)

# # Gradient Boosted Trees
# # # Sequential correction of predecessor's errors.
# # # Does not tweak the weights of training instances.
# # # Fit each predictor is trained using its predecessor's residual errors as labels.
# # # Gradient Boosted Trees: a CART is used as a base learner.

# # Gradient Boosted Trees: Prediction
# # # Regression:
# # # # In sklearn: GradientBoostingRegressor.
# # # Classification:
# # # # In sklearn: GradientBoostingClassifier.

# # Gradient Boosting in sklearn (auto dataset)
# Import models and utility functions
from sklearn.ensemble import GradientBoostingRegressor
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

# Instantiate a GradientBoostingRegressor 'gbt'
gbt = GradientBoostingRegressor(n_estimators=300, max_depth=1, random_state=SEED)

# Fit 'gbt' to the training set
gbt.fit(X_train,y_train)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred)**(1/2)

# Print the test set RMSE
print('Test set RMSE: {:.2f}'.format(rmse_test))
"""