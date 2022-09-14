"""
# Boosting
# # Boosting: Ensemble method combining several weak learners to form a strong learner.
# # Weak learner: Model doing slightky better than random guessing.
# # Example of weak learner: Decision stump (CART whose maximum depth is 1)
# # Train an ensemble of predictors sequentially.
# # Each predictor tries to correct its predecessor.
# # Most popular boosting methods:
# # # AdaBoost,
# # # Gradient Boosting.

# # AdaBoost
# # # Stands for Adaptive Boosting.
# # # Each predictor pays more attention to the instances wrongly predicted by its predecessor.
# # # Achivied by changing the weights of training instances.
# # # Each predictor is assigned a coefficient.
# # # depends on the predictor's training error.

# # AdaBoost: Prediction
# # # Classification:
# # # # Weighted majority voting.
# # # # In sklearn: AdaBoostClassifier.
# # # Regression:
# # # # Weighted average.
# # # # In sklearn: AdaBoostRegressor.

# # AdaBoost Classification in sklearn (Breast Cancer dataset)
# Import models and utility functions
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

# Set seed for reproducibility
SEED = 1

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.3,
    stratify=y,
    random_state=SEED
)

# Instantiate a classification-tree 'dt'
dt = DecisionTreeClassifier(max_depth=1, random_state=SEED)

# Instantiate an AdaBoost classifier 'adab_clf'
adb_clf = AdaBoostClassifier(base_estimator=dt, n_estimators=100)

# Fit 'adb_clf' to the training set
adb_clf.fit(X_train,y_train)

# Predict the test set probabilities of positive class
y_pred_proba = adb_clf.predict_proba(X_test)[:,1]

# Evaluate test-set roc_auc_score
adb_clf_roc_auc_score = roc_auc_score(y_test, y_pred_proba)

# Print adb_clf_roc_auc_score
print('ROC AUC score: {:.2f}'.format(adb_clf_roc_auc_score))

"""