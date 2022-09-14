"""
# Tuning a CART's hyperparameters

# # Hyperparameters
# # # Machine learning model:
# # # parameters: learned from data
# # # # CART example: split-point of a node, split-feature of a node, ...
# # # hyperparametes: not learned from data, set prior to training
# # # # CART example: max_depth, min_samples_leaf, splitting criterion ...

# # What is hyperparameter tuning?
# # # Problem: search for a set of optimal hyperparameters for a learning algorithm.
# # # Solution: find a set of optimal hyperparameters that results in an optimal model.
# # # Optimal model: yields an optimal score.
# # # Score: in sklearn defaults to accuracy (classification) and R^2 (regression).
# # # Cross validation is used to estimate the generalization performance.

# # Why tune hyperparameters?
# # # In sklearn, a model's default hyperparameters are not optimal for all problems.
# # # Hyperparameters should be tuned to obtain the best model performance.

# # Approaches to hyperparameter tuning
# # # Grid Search
# # # Random Search
# # # Bayesian Optimization
# # # Genetic Algorithms
# # # ...

# # Grid search cross validation
# # # Manually set a grid of discrete hyperparameter values.
# # # Set a metric for scoring model perfomance.
# # # Search exhaustivelly through the grid.
# # # For each set of hyperparameters. evaluate each model's CV score.
# # # The optimal hyperparameters are those of the model achieving the best CV score.

# # Grid search cross validation: example
# # # Hyperparameters grids:
# # # # max_depth = {2,3,4}. 
# # # # min_samples_leaf = {0.05,0.1}
# # # hyperparameter space = { (2,0.05), (2,0.1), (3,0.05), ...}
# # # CV score = {score(2,0.05), ...}
# # # optimal hyperparameters = set of hyperparameters corresponding to the best CV score.

# # Inspecting the hyperparameters of a CART in sklearn
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# Set seed to 1 for reproducibility
SEED = 1

# Instantiate a DecisionTreeClassifier 'dt'
dt = DecisionTreeClassifier(random_state=SEED)

# Print out 'dt's hyperparameters
print(dt.get_params())

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV
# Define the grid of hyperparameters 'params_dt'
# Define the grid of hyperparameters 'params_dt'
params_dt = {
              'max_depth': [3, 4, 5, 6],
              'min_samples_leaf': [0.04, 0.06, 0.08],
              'max_features': [0.2, 0.4,0.6, 0.8]
            }

# Instantiate a 10-fold CV grid search object 'grid_dt'
grid_dt = GridSearchCV(estimator=dt, param_grid=params_dt, scoring='accuracy', cv=10, n_jobs=-1)

# Fit 'grid_dt' to the training data
grid_dt.fit(X_train, y_train)

# Extract best hyperparameters from 'grid_dt'
best_hyperparams = grid_dt.best_params_
print('Best hyerparameters:\n', best_hyperparams)

# Extract best CV score from 'grid_dt'
best_CV_score = grid_dt.best_score_
print('Best CV accuracy'.format(best_CV_score))

# Extract best model from 'grid_dt'
best_model = grid_dt.best_estimator_

# Evaluate test set accuracy
test_acc = best_model.score(X_test,y_test)

# Print test set accuracy
print("Test set accuracy of best model: {:.3f}".format(test_acc))
"""