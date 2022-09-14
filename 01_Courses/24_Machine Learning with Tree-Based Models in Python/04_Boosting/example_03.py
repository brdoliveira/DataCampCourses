"""
# Stochastic Gradient Boosting (SGB)

# # Gradient Boosting: Cons
# # # GB involves an exhaustive search procedure.
# # # Each CART is trained to find the best split points and features.
# # # May lead to CARTs using the same split points and maybe the same features.

# # Stochastic Gradient Boosting
# # # Each tree is trained an a random subset of rows of the training data.
# # # The sampled instances (40% - 80% of the training set) are sampled without replacement.
# # # Features are samples (without replacement) when choosing split points.
# # # Result: further ensemble diversity.
# # # Effect: adding further variance to the ensemble of trees.

# # Stochastic Gradient Boosting in sklearn (auto dataset)
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

# Instantiate a stochastic GradientBoostingRegressor 'sgbt'
sgbt = GradientBoostingRegressor(
    max_depth=1,
    subsample=0.8,
    max_features=0.2,
    n_estimators=300,
    random_state=SEED
)

# Fit 'sgbt' to the training set
sgbt.fit(X_train,y_train)

# Predict the test set labels
y_pred = sgbt.predict(X_test)

# Evaluate test set RMSE 'rmse_test'
rsme_test = MSE(y_test, y_pred)**(1/2)

# Print 'rmse_test'
print('Test set RMSE: {:.2f}'. format(rmse_test))
"""