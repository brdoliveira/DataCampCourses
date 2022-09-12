"""
# Decision-Tree for Classification

# # Classification-tree
# # # Sequence of if-else questions about individual features.
# # # Objective: infer class labels.
# # # Able to capture non-linear relationships between features and labels.
# # # Don't require feature scaling (ex: Standardization, ...)

# # Classification-tree in scikit-learn
# # # Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
# # # Import train_test_split
from sklearn.model_selection import train_test_split
# # # Import accuracy_score
from sklearn.metrics import accuracy_score
# # # Split the dataset into 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    statify=y,
    random_state=1       
)
# # # Instantiate dt
dt = DecisionTreeClassifier(max_depth=2, random_state=1)
# # # Fit dt to the training set
dt.fit(X_train,y_train)
# # # Predict the test set labels
y_pred = dt.predict(X_test)
# # # Evaluate the test-set accuracy
accuracy_score(y_test, y_pred)

# # Decision Regions
# # # Decision region: region in the feature space where all instances are assigned to one class label.
# # # Decision Boundary: surface separating different decision regions.
"""