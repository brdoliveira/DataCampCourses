"""
# Decision-Tree for Regression

# # Regression-Tree in scikit-learn

# Import DecisionTreeRegression
from sklearn.tree import DecisionTreeRegressor
# Import train_test_split
from sklearn.model_selection import train_test_split
# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE
# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=3
)
# Instantiate a DecisionTreeRegression 'dt'
dt = DecisionTreeRegression(
    max_depth=4,
    min_samples_leaf=0.1,
    random_state=3
)
# Fit 'dt' to the traning-set
df.fit(X_train,y_train)
# Predict test-set labels
y_pred = dt.predict(X_test)
# Compute test-set MSE
mse_dt = MSE(y_test, y_pred)
# Compute test-set RMSE
rmse_dt = mse_dt**(1/2)
# Print rmse_dt
print(rmse_dt)
"""